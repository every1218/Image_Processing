import cv2
import numpy as np
img = cv2.imread('images/repeat.jpg')
width = int(input("가로를 입력하시오: "))
height = int(input("세로를 입력하시오: "))

h, w, _ = img.shape
new_img = np.zeros((h * height, w * width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        for temp_y in range(i*h, (i+1) * h):
            for temp_x in range(j*w, (j+1) * w):
                new_img[temp_y, temp_x] = img[temp_y % h, temp_x % w]

cv2.imshow('image repeat', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
