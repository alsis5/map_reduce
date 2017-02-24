#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import FileLoader
import threading

reduce_dict = dict()

def cleanStrip (strip):

    clean_strip = strip.lower()
    clean_strip = clean_strip.replace(".", "")
    clean_strip = clean_strip.replace(",", "")
    clean_strip = clean_strip.replace("\n", " ")
    clean_strip = clean_strip.replace("\t", " ")
    clean_strip = clean_strip.replace("à", "a")
    clean_strip = clean_strip.replace("À", "a")
    clean_strip = clean_strip.replace("È", "e")
    clean_strip = clean_strip.replace("è", "e")
    clean_strip = clean_strip.replace("É", "e")
    clean_strip = clean_strip.replace("é", "e")
    clean_strip = clean_strip.replace("Í", "i")
    clean_strip = clean_strip.replace("í", "i")
    clean_strip = clean_strip.replace("Ó", "o")
    clean_strip = clean_strip.replace("ó", "o")
    clean_strip = clean_strip.replace("Ò", "o")
    clean_strip = clean_strip.replace("ò", "o")
    clean_strip = clean_strip.replace("ç", "c")
    clean_strip = clean_strip.replace("\xc2\xb7", "·")
    clean_strip = clean_strip.replace("!", "")
    clean_strip = clean_strip.replace(":", "")
    clean_strip = clean_strip.replace("?", "")
    clean_strip = clean_strip.replace(";", "")

    return clean_strip

def reduce (lock, partial_count):
    global reduce_dict
    lock.acquire()
    #reduce_dict.update(word_count_dictionary)
    #print word_count_dictionary
    for word in partial_count:
        if word in reduce_dict:
            reduce_dict[word]+=partial_count[word]
        else:
            reduce_dict[word]=partial_count[word]
    lock.release()

def mapping (strip = None, lock = None):
    if strip is not None:
        word_count_dictionary = dict()
        words = strip.split()
        #print "Strip len:", len(strip), strip
        for word in words:
            if word in word_count_dictionary:
                word_count_dictionary[word]+=1
            else:
                word_count_dictionary[word]=1

        reduce(lock, word_count_dictionary)

def printResult (result):
    sortednames=sorted(result.keys(), key=lambda x:x.lower())
    for word in sortednames:
        print "\t", result[word], word

def main ():
    print "Map reduce"
    args = sys.argv;
    number_of_arguments = len (args)
    if number_of_arguments <= 1:
        print "Usage: python main.py [text file]"
    else:
        for file in args[1:]:
            fl = FileLoader.FileLoaders()
            content = fl.loadFile(file) #Conent sould be loaded by chunks
            # Fer pretractament de les dades a fora
            # posar totes les paraules en minuscules
            # esborrar caracters com guionet
            #content = [ content.remove(strip) if len(strip) <= 0 else strip for strip in content] #TODO s'esta menjant l'ultima linia, revisar si hi ha un
            # salt de linia o algun altre element en comptes d'una linia buida

            lock = threading.Lock()
            for strip in content:
                strip = cleanStrip (strip)
                mapping_threads = []

                # remove empty lines
                if (len(strip) > 0):
                    args = {"strip": strip, "lock": lock}
                    # Aqui hauria de tirar un thread per cada linia
                    thread = threading.Thread(kwargs = args ,target=mapping)
                    mapping_threads.append(thread)
                    thread.start()
            for thread in mapping_threads:
                thread.join()

            global reduce_dict
            printResult (reduce_dict)

if __name__ == "__main__":
    main()
