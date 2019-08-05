import cv2 as cv
import numpy as np
import copy

def load_image(path):
    return cv.imread(path)
pass

def get_kernel_size(kernel):

    if kernel%2 == 0:
        return kernel + 1
    else:
        return kernel


def blur_image(img, kernel_size):

    kernel_size = get_kernel_size(kernel_size)
    return cv.medianBlur(img, kernel_size)

def nothing(x):
    pass

def find_circle(img, kernel_size):

    new_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    big_circles = cv.HoughCircles(new_img, cv.HOUGH_GRADIENT, 1, 600, 40,20, 20, 80)
    for i in big_circles[0,:]:
        cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)

    #cv.imshow("okno",img)
    #cv.waitKey(0)


    return big_circles[0]

def make_bounding_box(img, circle):

    #left_top_x, left_top_y, right_bottom_x, right_bottom_y = 0

    x_cord = circle[0,0]
    y_cord = circle[0,1]
    radius = circle[0,2]

    left_top_x = int((x_cord - radius) * 0.95)
    left_top_y = int((y_cord - radius) * 0.95)
    right_bottom_x = int((x_cord + radius) * 1.05)
    right_bottom_y = int((y_cord + radius) * 1.05)

    ##p1 = cv.Point(left_top_x, left_top_y)
    ##p2 - cv.Point(right_bottom_x, right_bottom_y)

    cv.rectangle(img, (left_top_x, left_top_y),(right_bottom_x, right_bottom_y), (0,255,0) , 1, 4)

    cv.imshow("Bb", img)
    cv.waitKey(0)







