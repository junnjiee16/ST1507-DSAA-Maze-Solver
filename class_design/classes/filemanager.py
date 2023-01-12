import os
import sys

# filemanager object, handles file I/O
class FileManager:
    def readFile(filename):
        # get the directory of the absolute path leading to the script it is running on (so it will be correct when another script imports this)
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        print(path)

        # join the directory path with the filename
        abs_file_path = os.path.join(path, filename)

        # check if file exists
        if os.path.exists(abs_file_path):
            with open(abs_file_path) as f:
                content = f.read()

                print(content)        
                return content
