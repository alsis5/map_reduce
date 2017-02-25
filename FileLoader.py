#!/usr/bin/python
# -*- coding: utf-8 -*-

class FileLoader:
    def __init__(self):
        pass
    def loadFile (self, file):
        with open(file) as f:
            content = f.readlines()
        # TODO: erase new lines
        content = [x.strip('\n') for x in content]
        [strip.decode('utf8') for strip in content]
        return content

    def readFileByChunks(self, path, block_size=1024):
        with open(path, 'rb') as f:
            while True:
                content = f.readline()

                if content:
                    #content = [x.strip('\n') for x in content]
                    #print content
                    yield content
                else:
                    return
