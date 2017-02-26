#!/usr/bin/python
# -*- coding: utf-8 -*-
# Map reduce algorith implementation to generate text document word histograms
__author__ = "Albert Soto i Serrano (NIU 1361153)"
__email__ = "albert.sotoi@e-campus.uab.cat"
__version__ = "1.2.2"

# Imports
import sys
import FileLoader
import time
import DataProcessor
from multiprocessing import Process, Manager
import multiprocessing
# Global dictionary where the reducing phase will converge
reduce_dict = dict()

# Reduction phase: receives a partial count of words and updates the result dictionary
# Notice that python dictionary by itself accomplishes the sorting and merging phases,
# so there is no need to remove/sort duplicated data as python dictionary is
# a hashing structure.
def reduce (partial_count):
    global reduce_dict
    for word in partial_count:
        if word in reduce_dict:
            reduce_dict[word]+=partial_count[word]
        else:
            reduce_dict[word]=partial_count[word]
# Mapping phase: receives a splitted chunk of the text file and generates a
# pair of word:count dictionary
def mapping (strip = None, dp=None, results=None):
    if strip is not None:
        strip = dp.cleanStrip (strip)
        if (len(strip) > 0): # remove empty lines
            word_count_dictionary = dict()
            words = strip.split()
            for word in words:
                if word in word_count_dictionary:
                    word_count_dictionary[word]+=1
                else:
                    word_count_dictionary[word]=1
            results.append(word_count_dictionary)

# Print the results alphanumerically
def printResult (result):
    sortednames=sorted(result.keys(), key=lambda x:x.lower())
    for word in sortednames:
        print "\t", result[word], word

def main ():
    args = sys.argv;
    number_of_arguments = len(args)
    if number_of_arguments <= 1:
        print "Usage: python main.py [text file]"
    else:
        fl = FileLoader.FileLoader()
        dp = DataProcessor.DataProcessor()
        manager = Manager()
        for file in args[1:]:
            initial_time = time.time()
            global reduce_dict
            reduce_dict = dict()
            map_processes = []
            partial_results = manager.list()
            for content_chunks in fl.readFileByChunks(file, block_size=102400, num_of_chunks=multiprocessing.cpu_count()):
                for strip in content_chunks:
                    process = Process(target=mapping, args=(strip, dp, partial_results))
                    map_processes.append(process)
                    process.start()
            for process in map_processes:
                process.join()
            for partial_result in partial_results:
                reduce(partial_count=partial_result)

            print file+":"
            printResult (reduce_dict)
            #print "Total words:", len(reduce_dict)
            #print "Elapsed time:",time.time()-initial_time

if __name__ == "__main__":
    main()
