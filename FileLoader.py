#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Albert Soto i Serrano (NIU 1361153)"
__email__ = "albert.sotoi@e-campus.uab.cat"
import string

class FileLoader:
    def __init__(self):
        pass
    def loadFile (self, file):
        with open(file) as f:
            content = f.readlines()
        content = [x.strip('\n') for x in content]
        [strip.decode('utf8') for strip in content]
        return content

    def readFileByChunks(self, path, block_size=102400, num_of_chunks=4):
        with open(path) as f:
            while True:
                content_array = []
                for i in range(num_of_chunks):
                    content = f.read(block_size)
                    flag = False
                    while content[-1:] not in string.whitespace: #end of word
                        flag = True
                        nextf = f.read(1)
                        if nextf:
                            content+=nextf
                        else:
                            break
                    if content:
                        if flag:
                            if nextf:
                                content_array.append(content)
                        else:
                            content_array.append(content)
                    else:
                        if i > 0:
                            yield content_array
                        else:
                            f.close()
                            return
                yield content_array
