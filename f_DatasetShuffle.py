import pandas as pd
import numpy as np
import os
import copy
import random
import shutil
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
    for i in range(0,(num_of_files)):
        exist = check_that_file_exist_in_train_dataset(i, train_indexes)

        if exist==True:
            pass
        else:
            test_indexes.append(i)

    return test_indexes
    

#Sprawdza czy dany indeks istnieje w zbiorze testującym
def check_that_file_exist_in_train_dataset(target, train_indexes):

    i = 0
    train_size = len(train_indexes)

    while(i<train_size):

        if(train_indexes[i] == target):
            return True
        else:
            pass
        i = i + 1

    return False



#Tworzy zbiory plików
def copy_image_files(list_of_files, train_indexes, train_path, test_indexes, test_path):

    for i in train_indexes:
        temp_path = list_of_files[i]    
        shutil.copy2(temp_path, train_path)

    for j in test_indexes:

        temp_path2 = list_of_files[j]
        shutil.copy2(temp_path2, test_path)

def copy_label_data(list_of_files, list_of_labels, train_indexes, train_label_path, test_indexes, test_label_path):

    for i in train_indexes:
        append_label_to_file(train_label_path, list_of_labels[i])

    for j in train_indexes:
        append_label_to_file(test_label_path, list_of_labels[j])

def read_label_file(path):


    file = open(path,"r")
    list_of_labels = []
    lines = file.read().splitlines()
    for i in lines:
        list_of_labels.append(i)
        #print(i,'\n')
    file.close()

    return list_of_labels

def process_label_list(list_of_labels):

    splited_list = []
    for i in list_of_labels:

        head,tail = i.split(' ')
        splited_list.append(head)
    return splited_list

def append_label_to_file(path, data):

    file = open(path,"a")
    new_line = data + '\n'
    file.write(new_line)
    file.close()
