import numpy as np
import pandas as pd
import os

#Zwraca listę plików o danym rozszerzeniu w danej lokalizacji
def get_list_of_files_in_directory(path, ext):
    files = []
    filenames = []
    for r,d,f in os.walk(path):
        for file in f:
            if ext in file:
                files.append(os.path.join(r,file))
                filenames.append(os.path.join(f,file))

    return files

def get_filename_from_path(path, ext):

    head, tail = os.path.split(path)
    return tail

def get_rim_id_from_filename(filename):
   
    short_filename = filename.split('.')
    len = short_filename.size()

    rim_number = short_filename[len-4-1:len-1]

    pass









