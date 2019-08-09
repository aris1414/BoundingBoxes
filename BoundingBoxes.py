from f_GlobalFunctions import *
import time
import os

#Wybór środowiska do przygotowania zdjęć
print('Wybierz model dla którego chcesz przygotowac dane:\n1 - YOLOv3\n2 - Tensorflow object_detection\n')
enviroment = input('Twoj wybor: ')


#Wybór trybu pracy
print('Wybierz tryb pracy: \n', '1 - Automatyczne oznaczanie zdjęć \n', '2 - Reczne oznaczanie zdjęć \n', '3 - Podział na zbiory uczacy i testujący \n')
mode = input('Twoj wybor: ')
end_flag = False

#Warunek zakończenia pracy
if (enviroment != '1' and enviroment != '2'):
    end_flag = True

if ((mode != '1' and mode != '2' and mode != '3')):
    end_flag = True
start_time = time.time()

#path = 'C:\\Users\\robawjo\\Desktop\\Black_Big'
#dest_file_path = 'C:\\Users\\robawjo\\Desktop\\Black_Big\\labels.txt'
#wrong_bb_path ='C:\\Users\\robawjo\\Desktop\\Black_Big\\wrong_bb.txt'
#train_set_path = 'C:\\Users\\robawjo\\Desktop\\Black_Big\\train_set'
#test_set_path = 'C:\\Users\\robawjo\\Desktop\\Black_Big\\test_set'
#train_set_file = 'C:\\Users\\robawjo\\Desktop\\Black_Big\\train_set\\train.txt'
#test_set_file = 'C:\\Users\\robawjo\\Desktop\\Black_Big\\test_set\\test.txt'

path = 'C:\\Users\\robawjo\\Desktop\\Black_Big1'
dest_file_path = 'C:\\Users\\robawjo\\Desktop\\Black_Big1\\labels.csv'
wrong_bb_path ='C:\\Users\\robawjo\\Desktop\\Black_Big1\\wrong_bb.txt'
train_set_path = 'C:\\Users\\robawjo\\Desktop\\Black_Big1\\train_set'
test_set_path = 'C:\\Users\\robawjo\\Desktop\\Black_Big1\\test_set'
train_set_file = 'C:\\Users\\robawjo\\Desktop\\Black_Big1\\train_set\\train.csv'
test_set_file = 'C:\\Users\\robawjo\\Desktop\\Black_Big1\\test_set\\test.csv'

start_time = 0
while(not end_flag):

    if(enviroment == '1'):
        start_time = time.time()
        yolo_v3(mode, path, dest_file_path, wrong_bb_path, train_set_path, train_set_file, test_set_path, test_set_file)
        end_flag = True

    elif(enviroment == '2'):
        start_time = time.time()
        tensorflow_object_detection(mode, path, dest_file_path, wrong_bb_path, train_set_path, train_set_file, test_set_path, test_set_file)
        end_flag = True

    else:
        start_time = time.time()
        print('Wybrano zły tryb pracy. Program zostanie zakończony.')
        end_flag = True


    end_time = time.time()
    time_of_execution = end_time - start_time
    print('Czas wykonania programu: ', time_of_execution)