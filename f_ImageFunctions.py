import cv2 as cv
import numpy as np
import copy

def load_image(path):
    return cv.imread(path)
pass

#Oblicza wartość okna dla filtru
def get_kernel_size(kernel):

    if kernel%2 == 0:
        return kernel + 1
    else:
        return kernel

#Filtr medianowy
def blur_image(img, kernel_size):

    kernel_size = get_kernel_size(kernel_size)
    return cv.medianBlur(img, kernel_size)

#Normalizacja obrazu w skali szarości
def normalize_image(img):

    return img/255

#Przygotowanie zdjęcia do obróbki
def prepare_image(img, kernel):

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blurred = blur_image(img_gray, kernel)
    #img_normalized = normalize_image(img_blurred)
    return img_blurred

#Wyszukiwanie okręgu
def find_circle(img):

    new_img = img
    big_circles = cv.HoughCircles(new_img, cv.HOUGH_GRADIENT, 1, 600, 40,20, 20, 80)
    for i in big_circles[0,:]:
        cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)

    return big_circles[0]

#Rysowanie BoundingBoxa
def make_bounding_box(img_color, img_gray, circle):

    img_normalized = normalize_image(img_gray) #Normalizacja obrazu w skali szarości
    image_height, image_width = img_gray.shape #Rozmiar obrazu

    x_cord = circle[0,0] #Parametry znalezionego okręgu
    y_cord = circle[0,1]
    radius = circle[0,2] 

    left_top_x = int((x_cord - radius) * 1) # Wyszukiwanie boków BoundingBoxa - lewy górny
    left_top_y = int((y_cord - radius) * 1)
    left_bottom_x = int((x_cord - radius) * 1)# Wyszukiwanie boków BoundingBoxa - lewy dolny
    left_bottom_y = int((y_cord + radius) * 1)

    right_top_x = int((x_cord + radius) * 1) # Wyszukiwanie boków BoundingBoxa - prawy górny
    right_top_y = int((y_cord - radius) * 1)
    right_bottom_x = int((x_cord + radius) * 1) # Wyszukiwanie boków BoundingBoxa - prawy dolny
    right_bottom_y = int((y_cord + radius) * 1)

    x_min_norm = float(left_top_x / image_width) 
    x_max_norm = float(right_top_x / image_width)

    y_min_norm = float(left_top_y / image_height)
    y_max_norm = float(left_bottom_y / image_height)


    x_abs = x_max_norm - x_min_norm #Obliczanie długości boku - oś X   
    y_abs = y_max_norm - y_min_norm  #Obliczanie długości boku - oś Y


    x_center = float(circle[0,0] / image_width) #Środek BoundingBoxa
    y_center = float(circle[0,1] / image_height)

    img_temp = img_color

    cv.rectangle(img_temp, (left_top_x, left_top_y), (right_bottom_x, right_bottom_y), (0,0,255),1,4)
    cv.imshow("test_win", img_temp)
    cv.waitKey(200)


    return x_center, y_center, x_abs, y_abs







