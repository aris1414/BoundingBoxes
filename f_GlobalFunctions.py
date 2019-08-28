import numpy as np
from f_Functions import *
from f_ImageFunctions import *
from f_DatasetShuffle import *
from f_DataAug import *
import time
import os

def yolo_v3(mode, source_folder, dest_label_file, wrong_label_file, train_set_path, train_set_file, test_set_path, test_set_file):

    global end_flag

    if(mode == '1'): #Jeśli tryb ręczny

        list_of_images = get_list_of_files_in_directory(source_folder, '.BMP')

        for i in list_of_images:
            img = load_image(i)
            img_prepared = prepare_image(img, 3)
            print(i,'\n')
            roi = manual_mode(img)
            x_center_norm, y_center_norm, x_width_norm, y_height_norm = make_bounding_box_manual(img, img_prepared, roi)
            rim_id = get_rim_id_from_filename(i)
            #text_path = generate_text_file_name(i)
            save_file_yolo(dest_label_file, i, rim_id, x_center_norm, y_center_norm, x_width_norm, y_height_norm) #Zapis wyników


        end_flag = True #Flaga konca pracy


    elif (mode == '2'):
        train_folder_exist = os.path.exists(train_set_path)
        test_folder_exist = os.path.exists(test_set_path)

        if train_folder_exist == False:
            os.mkdir(train_set_path, 0o777)
        if test_folder_exist == False:
            os.mkdir(test_set_path, 0o777)       


        label_list = read_label_file(dest_label_file) #Zaczytanie danych po procesie oznaczania
        splited_list = process_label_list(label_list) #Odseparowanie ścieżki do pliku 
        num_of_files = len(splited_list)

        if num_of_files > 0:
            pass
            print('Podaj wspolczynnik danych uczacych: \n')
            ratio = input('Ratio: ')
            train_amount, test_amount = divide_by_ratio(num_of_files,float(ratio))

            print('Zbior uczacy bedzie zawieral ',train_amount, 'zdjec\n')
            print('Zbior testowy bedzie zawieral ',test_amount, 'zdjec\n')

            train_indexes = generate_train_dataset_indexes(num_of_files, train_amount)
            test_indexes = generate_test_dataset_indexes(num_of_files, train_indexes)

            copy_image_files(splited_list, train_indexes, train_set_path, test_indexes, test_set_path)
            copy_label_data(splited_list, label_list,train_indexes, train_set_path, train_set_file, test_indexes, test_set_path, test_set_file)

        end_flag = True



def data_augmentation(path_to_txt,dest_folder, dest_file, num_of_copies, transform_ratio):

    label_list = []
    label_list = read_label_file(path_to_txt) #Zaczytanie danych po procesie oznaczania

    dest_folder_exist = os.path.exists(dest_folder) #Sprawdza czy istnieje folder docelowy, jeśli nie to go tworzy

    if dest_folder_exist == False:
        os.mkdir(dest_folder, 0o777)

    for i in label_list:

        path, tail = split_record(i) #Odseparowanie sciezki do pliku od BB
        bbox_int, class_id = convert_bbox(tail) #Konwersja informacji o BB na ndArray
        img = load_image(path) #Ładowanie obrazu bazowego

        for j in range(0,num_of_copies):

            translate = RandomTranslate(transform_ratio,False) #Konstruktor przekształcenia

            img_copy = copy.copy(img) #Kopie obrazow i BBoxów
            bbox_copy = copy.copy(bbox_int)

            new_img, new_bbox = translate(img_copy, bbox_copy) #Translacja
            old_filename = get_filename_from_path(path)
            old_filename_without_ext = old_filename.split('.')

            new_filename = old_filename_without_ext[0] + '_copy_' + str(j) # Nazwa pliku wyjsciowego
            new_path = dest_folder + '\\' + new_filename

            new_image_path = new_path + '.bmp'

            cv.imwrite(new_image_path, new_img) #Zapis zdjecia do pliku
            save_file_yolo(dest_file, new_image_path, class_id, new_bbox[0][0], new_bbox[0][1], new_bbox[0][2], new_bbox[0][3])


            
            
        

        


       



        pass

        
