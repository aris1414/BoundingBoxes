import numpy as np
from f_Functions import *
from f_ImageFunctions import *
import time


start_time = time.time()

path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia zmniejszone 320x240\\Rim001'
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
    
    if (x_width > (x_width_old * 1.3)) or (y_height > (y_height_old * 1.3)):
        print(i, '\n')
        wrong_bb.append(i)

    x_width_old = x_width
    y_height_old = y_height


end_time = time.time()
time_of_execution = end_time - start_time
print('Czas wykonania programu: ', time_of_execution)

save_wrong_bb('wrong_bb.txt',wrong_bb) #Zapis informacji o potencjalnie złych BoundingBoxach
pass