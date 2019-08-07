import numpy as np
from f_Functions import *
from f_ImageFunctions import *
import time


#Wybór trybu pracy
print('Wybierz tryb pracy: \n', '1 - Automatyczne oznaczanie zdjęć \n', '2 - Reczne oznaczanie zdjęć \n', '3 - koniec programu \n')
mode = input('Twoj wybor: ')
end_flag = False

#Warunek zakończenia pracy
if ((mode != 1 and mode != 2)):
    end_flag = True
start_time = time.time()



while(not end_flag):

    if mode == 1: #Jeśli tryb automatyczny
    
        path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia zmniejszone 320x240'
        file_list = get_list_of_files_in_directory(path, '.bmp')
        wrong_bb = []

        x_width_old = 0.0
        y_height_old = 0.0

        for i in file_list:


            img = load_image(i)
            img_prepared = prepare_image(img, 3)
            circles = find_circle(img_prepared)
            x_center, y_center, x_width, y_height = make_bounding_box(img, img_prepared, circles)

            rim_id = get_rim_id_from_filename(i)
            text_path = generate_text_file_name(i)
            save_file(text_path, rim_id, x_center, y_center, x_width, y_height)
    
            if (x_width > (x_width_old * 1.2)) or (y_height > (y_height_old * 1.2)):
                print(i, '\n')
                wrong_bb.append(i)

            x_width_old = x_width
            y_height_old = y_height

        save_wrong_bb('wrong_bb.txt',wrong_bb) #Zapis informacji o potencjalnie złych BoundingBoxach
        end_flag = True

    elif(mode == 2): #Jeśli tryb ręczny

        wrong_bbs = read_wrong_bb('wrong_bb.txt') #Odczytaj plik z danymi do oznaczenia
        for i in wrong_bbs:
            img = load_image(i)
            img_prepared = prepare_image(img, 3)
            clone = img_prepared.clone()
            roi = manual_mode(clone)
            x_center_norm, y_center_norm, x_width_norm, y_height_norm = make_bounding_box_manual(img, img_prepared, roi)
            rim_id = get_rim_id_from_filename(i)
            text_path = generate_text_file_name(i)
            save_file(text_path, rim_id, x_center, y_center, x_width, y_height)


        end_flag = True



    end_time = time.time()
    time_of_execution = end_time - start_time
    print('Czas wykonania programu: ', time_of_execution)

    
pass