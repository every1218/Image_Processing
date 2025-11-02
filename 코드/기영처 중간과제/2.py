import cv2
import numpy as np
from scipy.optimize import newton

img1 = cv2.imread('images/add1.jpg')
img2 = cv2.imread('images/add2.jpg')

height, width, _ = img1.shape
img2 = cv2.resize(img2, (width, height))

cv2.namedWindow('dst')
cv2.createTrackbar('Image1', 'dst', 50, 100, lambda x: None)
cv2.createTrackbar('Image2', 'dst', 50, 100, lambda x: None)

while True:
    w1 = cv2.getTrackbarPos('Image1', 'dst') / 100.0
    w2 = cv2.getTrackbarPos('Image2', 'dst') / 100.0
    new_img= cv2.addWeighted(img1, w1, img2, w2, 0)

    h, w, _ = new_img.shape
    result = np.zeros((h, w * 3, 3), dtype=np.uint8)
    result[:, :w] = img1
    result[:, w:w * 2] = new_img
    result[:, w * 2:] = img2

    cv2.imshow('dst', result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
