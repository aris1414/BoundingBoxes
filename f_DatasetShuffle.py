import pandas as pd
import numpy as np
import os
import copy
import random
from shutil import copyfile

#Wyznacza liczbe zdjęć w zbiorach testujących i uczących na podstawie zadanego stosunku

def divide_by_ratio(num_of_files, train_ratio):

   train_amount = int(num_of_files * train_ratio)
   test_amount = num_of_files - train_amount

   return train_amount, test_amount

#Generuje losowe indeksy plików
def generate_train_dataset_indexes(num_of_files, train_amount):

    train_indexes = []

    train_indexes = random.sample(range(0,num_of_files - 1), train_amount)

    return train_indexes

#Generuje losowe indeksy dla zbioru testującego
def generate_test_dataset_indexes(num_of_files, train_indexes):

    test_indexes = []
    for i in range(0,(num_of_files - 1)):
        exist = check_that_file_in_train_dataset(i, train_indexes)

        if exist:
            break
        else:
            test_indexes.append(i)

    return test_indexes
    

#Sprawdza czy dany indeks istnieje w zbiorze testującym
def check_that_file_in_train_dataset(target, train_indexes):

    for i in train_indexes:
        if(target == i):
            return True
        else:
            return False



# Zmienia rozszerzenie pliku z bmp na txt
def change_extension(file_path):

    path_changed = file_path
    path_changed.replace('.bmp','.txt')
    return path_changed


#Tworzy zbiory plików
def make_datasets(list_of_files, train_indexes, train_path, test_indexes, test_path):

    for i in train_indexes:
        temp_path = list_of_files[i]
        path_changed = change_extension(temp_path)
        
        copyfile(temp_path, train_path)
        copyfile(path_changed, train_path)

    for j in test_indexes:

        temp_path = list_of_files[i]
        path_changed = change_extension(temp_path)

        copyfile(temp_path, test_path)
        copyfile(path_changed, test_path)

