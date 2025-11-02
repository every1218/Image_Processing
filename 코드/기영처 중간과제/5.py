import numpy as np
import cv2

def my_resize(image, dsize, fx=0.0, fy=0.0):
    h, w, c = image.shape

    if dsize == (0, 0) and fx > 0 and fy > 0:
        new_w = int(w * fx)
        new_h = int(h * fy)
    elif dsize != (0, 0) and fx == 0.0 and fy == 0.0:
        new_w, new_h = dsize
    else:
        print("에러")
        return None

    logo = np.zeros((new_h, new_w, c), dtype=image.dtype)

    for y in range(new_h):
        for x in range(new_w):
            old_x = int(x * (w / new_w))
            old_y = int(y * (h / new_h))

            old_x = min(old_x, w - 1)
            old_y = min(old_y, h - 1)

            logo[y, x] = image[old_y, old_x]

    return logo


image = cv2.imread("images/wirte_test.jpg", cv2.IMREAD_COLOR) # 원본 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 ")

img2 = cv2.resize(image, (400,300), fx=0.0, fy=0.0, interpolation = cv2.INTER_NEAREST)
img3 = my_resize(image, (400,300), fx=0.0, fy=0.0)

cv2.imshow("opencvresize", img2)
cv2.imshow("userresize", img3)

cv2.waitKey()
