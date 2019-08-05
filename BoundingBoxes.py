import numpy as np
from f_Functions import *
from f_ImageFunctions import *
import time


start_time = time.time()

path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia zmniejszone 640x480\\Test2\\Orange'
file_list = get_list_of_files_in_directory(path, '.bmp')


for i in file_list:


    img = load_image(i)
    img_prepared = prepare_image(img, 3)
    circles = find_circle(img_prepared)
    x_center, y_center, x_abs, y_abs = make_bounding_box(img, img_prepared, circles)

    rim_id = get_rim_id_from_filename(i)
    text_path = generate_text_file_name(i)

    save_file(text_path, rim_id, x_center, y_center, x_abs, y_abs)

    pass

end_time = time.time()

time_of_execution = end_time - start_time

print('Czas wykonania programu: ', time_of_execution)
pass