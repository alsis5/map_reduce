class FileLoaders:
    def __init__(self):
        pass
    def loadFile (self, file):
        with open(file) as f:
            content = f.readlines()
        # TODO: erase new lines
        content = [x.strip('\n') for x in content]
        [strip.decode('utf8') for strip in content]
        return content

    def loadFileByChunks (self, file, chunksize):
        pass
        
