import numpy as np
import pandas as pd
import os

#Zwraca listę plików o danym rozszerzeniu w danej lokalizacji
def get_list_of_files_in_directory(path, ext):

    files = []
    for r,d,f in os.walk(path):
        for file in f:
            if ext in file:
                files.append(os.path.join(r,file))

    return files

#Sepracja lokalizacji pliku i jego nazwy
def get_filename_from_path(path):

    head, tail = os.path.split(path)
    return tail

def get_file_path(path):

    head, tail = os.path.split(path)
    return head


#Funkcja wyciąga numer identyfikacyjny felgi na podstawie nazwy pliku
def get_rim_id_from_filename(path):
    
    filename = get_filename_from_path(path)
    splited_filename = filename.split('.')
    short_filename = splited_filename[0]
    length = len(short_filename)

    rim_number = short_filename[length-4-1:length]
    rim_number_int = int(rim_number)

    return rim_number_int

# Generowanie nazwy pliku wyjściowego
def generate_text_file_name(path):

    name_without_ext = path.split('.')
    result = name_without_ext + '.txt'
    return result








