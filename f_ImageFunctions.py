import cv2 as cv
import numpy as np
import copy

refPt = []
crooping = False

def load_image(path):
    return cv.imread(path)
pass

#Oblicza wartość okna dla filtru
def get_kernel_size(kernel):

    if kernel%2 == 0:
        return kernel + 1
    else:
        return kernel

#Zwraca rozmiar zdjęcia
def get_image_size(img_path):

    image = load_image(img_path)
    width, height = image.shape

    return width,height

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
    image_height, image_width = img.shape
    big_circles = cv.HoughCircles(new_img, cv.HOUGH_GRADIENT, 1, 600, 40,20, 20, 80) #Konfiguracja dla rozdzielczości 640x480
    #big_circles = cv.HoughCircles(new_img, cv.HOUGH_GRADIENT,  1, 600, 70,20, 1, 10) #Konfuguracja dla rozdzielczości 320x240
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

    left_top_x = int((x_cord - radius) * 0.95) # Wyszukiwanie boków BoundingBoxa - lewy górny
    left_top_y = int((y_cord - radius) * 0.95)
    left_bottom_x = int((x_cord - radius) * 0.95)# Wyszukiwanie boków BoundingBoxa - lewy dolny
    left_bottom_y = int((y_cord + radius) * 0.95)

    right_top_x = int((x_cord + radius) * 1.03) # Wyszukiwanie boków BoundingBoxa - prawy górny
    right_top_y = int((y_cord - radius) * 1.03)
    right_bottom_x = int((x_cord + radius) * 1.03) # Wyszukiwanie boków BoundingBoxa - prawy dolny
    right_bottom_y = int((y_cord + radius) * 1.03)



    img_temp = img_color

    cv.rectangle(img_temp, (left_top_x, left_top_y), (right_bottom_x, right_bottom_y), (0,0,255),1,4)
    cv.imshow("test_win", img_temp)
    cv.waitKey(100)


    return left_top_x,left_top_y,right_bottom_x,right_bottom_y

def make_bounding_box_manual(img_color, img_gray, rect_points):

    img_normalized = normalize_image(img_gray) #Normalizacja obrazu w skali szarości
    image_height, image_width = img_gray.shape #Rozmiar obrazu

    left_top = rect_points[0]
    right_bottom = rect_points[1]
    

    return left_top[0],left_top[1],right_bottom[0],right_bottom[1]



def mouse_click(event, x, y, flags, param):

    global refPt
    if (event == cv.EVENT_LBUTTONDOWN):
        refPt = [(x, y)]
        cropping = True
 
	# check to see if the left mouse button was released
    elif (event == cv.EVENT_LBUTTONUP):
        refPt.append((x, y))
        cropping = False


 
def manual_mode(img):

    
    global refPt
    refPt.clear()
    cv.namedWindow("Manual")
    cv.setMouseCallback("Manual", mouse_click)
    img_backup = copy.copy(img)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    while True:
        cv.imshow("Manual", img)
        key = cv.waitKey(1) & 0xFF
 
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            refPt.clear()
            img = img_backup
 
        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            cv.destroyAllWindows()
            break

        if(len(refPt)==2):
            cv.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)

    if len(refPt) == 2:
        img_roi = img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        cv.imshow("ROI",img_roi)
        cv.waitKey(0)
        roi = refPt

        cv.destroyAllWindows()
        return roi
    else:
        print('Error')
        exit






    




