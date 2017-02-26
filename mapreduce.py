#!/usr/bin/python
# -*- coding: utf-8 -*-
# Map reduce algorith implementation to generate text document word histograms
__author__ = "Albert Soto i Serrano (NIU 1361153)"
__email__ = "albert.sotoi@e-campus.uab.cat"
__version__ = "1.3.1"

import sys
import FileLoader
import time
import DataProcessor
from multiprocessing import Process, Manager
import multiprocessing

# Global dictionary where the reducing phase will converge
reduce_dict = dict()

def processArgs (args):
    letter_flag = False
    join_flag = False
    args_to_remove = []
    for arg in args:
        if arg == "-l":
            letter_flag = True
            args_to_remove.append(arg)
        elif arg == "-j":
            join_flag = True
            args_to_remove.append(arg)
        else:
            pass
    [args.remove(arg) for arg in args_to_remove]
    return letter_flag, join_flag


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
def mapping (strip = None, dp=None, results=None, letter_flag=False):
    if strip is not None:
        strip = dp.cleanStrip (strip)
        if (len(strip) > 0): # remove empty lines
            word_count_dictionary = dict()
            words = strip.split()
            if letter_flag == False:
                for word in words:
                    if word in word_count_dictionary:
                        word_count_dictionary[word]+=1
                    else:
                        word_count_dictionary[word]=1
            else:
                for word in words:
                    for letter in word:
                        if letter in word_count_dictionary:
                            word_count_dictionary[letter]+=1
                        else:
                            word_count_dictionary[letter]=1

            results.append(word_count_dictionary)

# Print the results alphanumerically
def printResult (result):
    sortednames=sorted(result.keys(), key=lambda x:x.lower())
    for word in sortednames:
        print "\t", result[word], word

def main ():
    args = sys.argv;
    letter_flag, join_flag = processArgs (args)
    number_of_arguments = len(args)
    if number_of_arguments <= 1:
        print "Usage: python main.py [text file] \nOptional flags:\n\t-l : letter histogram\n\t-j : join multiple files histogram"
    else:
        fl = FileLoader.FileLoader()
        dp = DataProcessor.DataProcessor()
        manager = Manager()
        global reduce_dict
        if join_flag == True:
            reduce_dict = dict()
        for file in args[1:]:
            initial_time = time.time()
            if join_flag == False:
                reduce_dict = dict()
            map_processes = []
            partial_results = manager.list()
            for content_chunks in fl.readFileByChunks(file, block_size=4*1024*1024, num_of_chunks=1):
                for strip in content_chunks:
                    process = Process(target=mapping, args=(strip, dp, partial_results, letter_flag))
                    map_processes.append(process)
                    process.start()
            print len(map_processes)
            for process in map_processes:
                process.join()
            for partial_result in partial_results:
                reduce(partial_count=partial_result)

            if join_flag == False:
                print file+":"
                printResult (reduce_dict)
                #print "Total words:", len(reduce_dict)
                #print "Elapsed time:",time.time()-initial_time
        if join_flag == True:
            print str([arg for arg in args[1:]])+":"
            printResult (reduce_dict)

if __name__ == "__main__":
    main()
