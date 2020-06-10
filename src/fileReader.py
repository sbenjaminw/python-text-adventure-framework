
#   Line reader.
#   Reads each chapter .txt file
class FileReader:

    #   Reads a file.
    def ExecuteReader(self, fpath):
        linesInFile = [""]
        
        theFile = open(fpath, "r")
        
        for line in theFile:
            linesInFile.append(line)
        
        theFile.close()
        
        return linesInFile