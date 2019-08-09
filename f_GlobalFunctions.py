import numpy as np
from f_Functions import *
from f_ImageFunctions import *
from f_DatasetShuffle import *
import time
import os

def yolo_v3(mode, source_folder, dest_label_file, wrong_label_file, train_set_path, train_set_file, test_set_path, test_set_file):

    global end_flag

    if mode == '1': #Jeśli tryb automatyczny
        initialize_file(dest_label_file)
        initialize_file(wrong_label_file)

        file_list = get_list_of_files_in_directory(source_folder, '.bmp')
        wrong_bb = []

        x_width_old = 0.0
        y_height_old = 0.0

        for i in file_list:


            img = load_image(i)
            img_prepared = prepare_image(img, 3)
            circles = find_circle(img_prepared)
            x_center, y_center, x_width, y_height = make_bounding_box(img, img_prepared, circles)

            rim_id = get_rim_id_from_filename(i)
            #text_path = generate_text_file_name(i)
               
            if (x_width > (x_width_old * 1.2)) or (y_height > (y_height_old * 1.2)):
                print(i, '\n')
                save_wrong_bb(wrong_label_file, i) #Zapis informacji o potencjalnie złych BoundingBoxach
            else:
                save_file_yolo(dest_label_file, i, rim_id, x_center, y_center, x_width, y_height)

            x_width_old = x_width
            y_height_old = y_height

        end_flag = True

    elif(mode == '2'): #Jeśli tryb ręczny

        wrong_bbs = read_wrong_bb(wrong_label_file) #Odczytaj plik z danymi do oznaczenia
        for i in wrong_bbs:
            img = load_image(i)
            img_prepared = prepare_image(img, 3)
            roi = manual_mode(img)
            x_center_norm, y_center_norm, x_width_norm, y_height_norm = make_bounding_box_manual(img, img_prepared, roi)
            rim_id = get_rim_id_from_filename(i)
            #text_path = generate_text_file_name(i)
            save_file_yolo(dest_label_file, i, rim_id, x_center_norm, y_center_norm, x_width_norm, y_height_norm) #Zapis wyników


        end_flag = True #Flaga konca pracy


    elif (mode == '3'):
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


    end_time = time.time()
    time_of_execution = end_time - start_time
    print('Czas wykonania programu: ', time_of_execution)


def tensorflow_object_detection(mode, source_folder, dest_label_file, wrong_label_file, train_set_path, train_set_file, test_set_path, test_set_file):
    global end_flag

    if mode == '1': #Jeśli tryb automatyczny
        initialize_file(dest_label_file)
        initialize_file(wrong_label_file)
        write_header_csv(dest_label_file)

        file_list = get_list_of_files_in_directory(source_folder, '.bmp')
        wrong_bb = []

        x_width_old = 0.0
        y_height_old = 0.0

        for i in file_list:


            img = load_image(i)
            img_prepared = prepare_image(img, 3)
            circles = find_circle(img_prepared)
            x_center, y_center, x_width, y_height = make_bounding_box(img, img_prepared, circles)

            rim_id = get_rim_id_from_filename(i)
            class_id = generate_class_label_by_id(rim_id)
            img_width, img_height = get_image_size(i)
            #text_path = generate_text_file_name(i)
               
            if (x_width > (x_width_old * 1.2)) or (y_height > (y_height_old * 1.2)):
                print(i, '\n')
                save_wrong_bb(wrong_label_file, i) #Zapis informacji o potencjalnie złych BoundingBoxach
            else:

                save_file_tf(dest_label_file, i, img_width, img_height, class_id, x_center, y_center, x_width, y_height)

            x_width_old = x_width
            y_height_old = y_height

        end_flag = True

    elif(mode == '2'): #Jeśli tryb ręczny

        wrong_bbs = read_wrong_bb(wrong_label_file) #Odczytaj plik z danymi do oznaczenia
        for i in wrong_bbs:
            img = load_image(i)
            img_prepared = prepare_image(img, 3)
            roi = manual_mode(img)
            x_center_norm, y_center_norm, x_width_norm, y_height_norm = make_bounding_box_manual(img, img_prepared, roi)
            rim_id = get_rim_id_from_filename(i)
            #text_path = generate_text_file_name(i)
            save_file_yolo(dest_label_file, i, rim_id, x_center_norm, y_center_norm, x_width_norm, y_height_norm) #Zapis wyników


        end_flag = True #Flaga konca pracy


    elif (mode == '3'):
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


    end_time = time.time()
    time_of_execution = end_time - start_time
    print('Czas wykonania programu: ', time_of_execution)

