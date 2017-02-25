#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import FileLoader
import threading
import time
import DataProcessor

reduce_dict = dict()

def reduce (partial_count,lock=None):
    lock.acquire()
    global reduce_dict
    for word in partial_count:
        if word in reduce_dict:
            reduce_dict[word]+=partial_count[word]
        else:
            reduce_dict[word]=partial_count[word]
    lock.release()

def mapping (strip = None, lock = None, dp=None):
    if strip is not None:
        strip = dp.cleanStrip (strip)
        if (len(strip) > 0): # remove empty lines
            word_count_dictionary = dict()
            words = strip.split()
            #print "Strip len:", len(strip), strip
            for word in words:
                if word in word_count_dictionary:
                    word_count_dictionary[word]+=1
                else:
                    word_count_dictionary[word]=1
            reduce(word_count_dictionary, lock)

def printResult (result):
    sortednames=sorted(result.keys(), key=lambda x:x.lower())
    for word in sortednames:
        print "\t", result[word], word

def main ():
    print "----------------------------\n----\tMap Reduce\t----\n----------------------------"
    args = sys.argv;
    number_of_arguments = len (args)
    if number_of_arguments <= 1:
        print "Usage: python main.py [text file]"
    else:
        fl = FileLoader.FileLoader()
        dp = DataProcessor.DataProcessor()
        for file in args[1:]:
            initial_time = time.time()
            global reduce_dict
            reduce_dict = dict()
            for content_array in fl.readFileByChunks(file, block_size=512, num_of_chunks=8):
                mapping_threads = []
                for strip in content_array:
                    lock = threading.Lock()
                    args = {"strip": strip, "lock": lock, "dp": dp}
                    thread = threading.Thread(kwargs = args ,target=mapping)
                    mapping_threads.append(thread)
                    thread.start()
                for thread in mapping_threads:
                    thread.join()

            #printResult (reduce_dict)
            print "Input file:", file
            print "Total words:", len(reduce_dict)
            print "Elapsed time:",time.time()-initial_time

if __name__ == "__main__":
    main()
