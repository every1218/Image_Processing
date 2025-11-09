import cv2
import numpy as np

def rgb(img):
    b, g, r = cv2.split(img)
    cv2.imshow('Red Channel', r)
    cv2.imshow('Green Channel', g)
    cv2.imshow('Blue Channel', b)

def hsi(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    # HSI의 I는 HSV의 V와 유사하게 사용됩니다.
    cv2.imshow('Hue Channel', h)
    cv2.imshow('Saturation Channel', s)
    cv2.imshow('Intensity Channel', v)

def lab(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(lab)
    cv2.imshow('L Channel', l)
    cv2.imshow('a Channel', a)
    cv2.imshow('b Channel', b)

def ycrcb(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    cv2.imshow('Y Channel', y)
    cv2.imshow('Cr Channel', cr)
    cv2.imshow('Cb Channel', cb)

img = cv2.imread('images/image2.jpg')

while True:
    cv2.imshow('Original Image', img)
    key = cv2.waitKey(0) & 0xFF

    cv2.destroyAllWindows()
    cv2.imshow('Original Image', img)


    if key == ord('1'):
        rgb(img)
    elif key == ord('2'):
        hsi(img)
    elif key == ord('3'):
        lab(img)
    elif key == ord('4'):
        ycrcb(img)
    elif key == ord('5'):
        break
    else:
        pass

cv2.destroyAllWindows()

