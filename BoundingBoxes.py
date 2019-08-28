from f_GlobalFunctions import *
import time
import os

mode = '0'
end_flag = False
#Wybór środowiska do przygotowania zdjęć
print('Wybierz tryb działania aplikacji:\n1 - YOLOv3\n2 - Data Augmentation\n ')
enviroment = input('Twoj wybor: ')

if(enviroment == '1'):
    print('Wybierz tryb pracy: \n', '1 - Oznaczanie zdjęć \n', '2 - Podział na zbiory uczący i testujący \n')
    mode = input('Twoj wybor: ')
   

#Warunek zakończenia pracy
if (enviroment != '1' and enviroment != '2'):
    end_flag = True

if ((enviroment == '1') and (mode != '1' and mode != '2')):
    end_flag = True
    

start_time = time.time()
path = ''



start_time = 0
while(not end_flag):

    if(enviroment == '1'):
        path = input('Sciezka do folderu ze zdjeciami: ')
        dest_file_path = path + "\\labels.txt"
        wrong_bb_path = path + "\\wrong_bb.txt"
        train_set_path = path + "\\train"
        test_set_path = path + "\\test"

        train_set_file = train_set_path + "\\train.txt"
        test_set_file = test_set_path + "\\test.txt"

        start_time = time.time()
        yolo_v3(mode, path, dest_file_path, wrong_bb_path, train_set_path, train_set_file, test_set_path, test_set_file)
        end_flag = True

    elif(enviroment == '2'):
        path_to_txt = input('Sciezka do pliku txt z listą zdjec: ')
        dest_folder = input('Sciezka do folderu docelowego z kopiami: ')
        dest_file = input('Sciezka do pliku z annotacjami dla kopii: ')
        num_of_copies = input('Liczba kopii danego zdjecia: ')
        translation_ratio = input('Wspolczynnik przesunięcia: ')
        start_time = time.time()
        data_augmentation(path_to_txt, dest_folder, dest_file, int(num_of_copies), float(translation_ratio))
        #end_flag = True
    else:
        start_time = time.time()
        print('Wybrano zły tryb pracy. Program zostanie zakończony.')
        end_flag = True


    end_time = time.time()
    time_of_execution = end_time - start_time
    print('Czas wykonania programu: ', time_of_execution)