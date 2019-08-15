from f_GlobalFunctions import *
import time
import os

#Wybór środowiska do przygotowania zdjęć
print('Wybierz model dla którego chcesz przygotowac dane:\n1 - YOLOv3\n2 - Tensorflow object_detection\n 3 - Data Augmentation\n ')
enviroment = input('Twoj wybor: ')


#Wybór trybu pracy
print('Wybierz tryb pracy: \n', '1 - Automatyczne oznaczanie zdjęć \n', '2 - Reczne oznaczanie zdjęć \n', '3 - Podział na zbiory uczacy i testujący \n')
mode = input('Twoj wybor: ')
end_flag = False

#Warunek zakończenia pracy
if (enviroment != '1' and enviroment != '2' and enviroment != '3'):
    end_flag = True

if ((mode != '1' and mode != '2' and mode != '3')):
    end_flag = True
start_time = time.time()


path = input('Sciezka do katalogu ze zdjeciami: ')
dest_file_path = path + "\\labels.txt"
wrong_bb_path = path + "\\wrong_bb.txt"
train_set_path = path + "\\train_set"
test_set_path = path + "\\test_set"

train_set_file = train_set_path + "\\train.txt"
test_set_file = test_set_path + "\\test.txt"


#path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia_czarne_full_1024_768'
#dest_file_path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia_czarne_full_1024_768\\labels.txt'
#wrong_bb_path ='C:\\Users\\robawjo\\Desktop\\Zdjecia_czarne_full_1024_768\\wrong_bb.txt'
#train_set_path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia_czarne_full_1024_768\\train_set'
#test_set_path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia_czarne_full_1024_768\\test_set'
#train_set_file = 'C:\\Users\\robawjo\\Desktop\\Zdjecia_czarne_full_1024_768\\train_set\\train.txt'
#test_set_file = 'C:\\Users\\robawjo\\Desktop\\Zdjecia_czarne_full_1024_768\\test_set\\test.txt'

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

    elif(enviroment == '3'):
        pass
        end_flag = True
    else:
        start_time = time.time()
        print('Wybrano zły tryb pracy. Program zostanie zakończony.')
        end_flag = True


    end_time = time.time()
    time_of_execution = end_time - start_time
    print('Czas wykonania programu: ', time_of_execution)