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

    rim_number = short_filename[3:6]
    rim_number_int = int(rim_number)

    return rim_number_int

# Generowanie nazwy pliku wyjściowego
def generate_text_file_name(path):

    name_without_ext = path.split('.')
    result = name_without_ext[0] + '.txt'
    return result

#Generuje opis
def generate_class_label_by_id(id):

    class_label = ''
    if id < 10:
        class_label = 'Rim00' + str(id)
    else:
        class_label = 'Rim0' + str(id)

    return class_label

def save_file_yolo(path,img_path,rim_id, bb_center_x, bb_center_y, bb_width, bb_height):

    file = open(path,"a")      
    data_frame = str(img_path) +  ' ' + str(bb_center_x) + ',' + str(bb_center_y) + ',' + str(bb_width) + ',' + str(bb_height) + ',' + str(rim_id) + '\n'
    file.write(data_frame)
    file.close()


def write_header_csv(path):

    file = open(path, "w")
    data_frame = 'filename,width,height,class,xmin,ymin,xmax,ymax\n'
    file.write(data_frame)
    file.close()


def save_file_tf(path,img_path, img_width, img_height, class_name, bb_center_x, bb_center_y, bb_width, bb_height):

    file = open(path,"a")      
    data_frame = str(img_path) +  ',' + str(img_width) + ',' + str(img_height) + ',' + str(class_name) + ',' + str(bb_center_x) + ',' + str(bb_center_y) + ',' + str(bb_width) + ',' + str(bb_height) + '\n'
    file.write(data_frame)
    file.close()



def save_wrong_bb(filename,wrong_bb):

    file = open(filename, "a")
    file.write(str(wrong_bb) + '\n')
    file.close()


def read_wrong_bb(path):

    file = open(path,"r")
    list_of_files = []
    lines = file.read().splitlines()
    for i in lines:
        list_of_files.append(i)
        print(i,'\n')
    file.close()

    return list_of_files


def initialize_file(path):

    file = open(path,"w")
    file.close()











