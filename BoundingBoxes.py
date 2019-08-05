import numpy as np
from f_Functions import *
from f_ImageFunctions import *

path = 'C:\\Users\\robawjo\\Desktop\\Zdjecia zmniejszone 640x480\\Rim003\\Black'
file_list = get_list_of_files_in_directory(path, '.bmp')


for i in file_list:

    get_rim_id_from_filename(i)
    img = load_image(i)
    img_prepared = prepare_image(img, 3)
    circles = find_circle(img_prepared)
    make_bounding_box(img, img_prepared, circles)
pass