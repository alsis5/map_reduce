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

    def readFileByChunks(self, path, block_size=1024, num_of_chunks=10):
        with open(path, 'rb') as f:
            while True:
                content_array = []
                for i in range(num_of_chunks):
                    content = f.read(block_size)
                    while content[-1:] != ' ':
                        nextf = f.read(1)
                        if nextf:
                            content+=nextf
                        else:
                            break
                    if content:
                        content_array.append(content)
                    else:
                        if i > 0:
                            yield content_array
                        else:
                            return

                yield content_array
