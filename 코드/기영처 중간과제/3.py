import cv2
import numpy as np

img = cv2.imread('images/bit_test.jpg')
logo = cv2.imread('images/logo.jpg')

width = int(input("가로에 들어갈 개수를 입력하시오: "))
height = int(input("세로에 들어갈 개수를 입력하시오: "))

# 로고크기 조정
bg_h, bg_w, _ = img.shape
logo_h = bg_h // height
logo_w = bg_w // width
resized_logo = cv2.resize(logo, (logo_w, logo_h))

new_img = img.copy()

for i in range(height):
    for j in range(width):
        temp_y = i * logo_h
        temp_x = j * logo_w

        space = new_img[temp_y:temp_y + logo_h, temp_x:temp_x + logo_w]

        # 검정 제거 마스크
        black = np.all(resized_logo == [0, 0, 0], axis=-1).astype(np.uint8) * 255
        mask = cv2.bitwise_not(black)

        new_logo = cv2.bitwise_and(resized_logo, resized_logo, mask=mask)
        temp = cv2.bitwise_and(space, space, mask=cv2.bitwise_not(mask))

        sum_img = cv2.add(temp, new_logo)

        new_img[temp_y:temp_y + logo_h, temp_x:temp_x + logo_w] = sum_img

cv2.imshow('image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
