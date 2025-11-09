from types import new_class

import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
new_img = None
img = None


def equal(event, x, y, flags, param):
    global ix, iy, drawing, new_img, img

    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        new_img = img.copy()

        x1, y1 = max(ix - 50, 0), max(iy - 50, 0)
        x2, y2 = min(ix + 50, img.shape[1]), min(iy + 50, img.shape[0])

        roi = img[y1:y2, x1:x2]

        if len(roi.shape) == 2:
            equalized_roi = cv2.equalizeHist(roi)
        else:
            ycrcb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2YCrCb)
            ycrcb_roi[:, :, 0] = cv2.equalizeHist(ycrcb_roi[:, :, 0])
            equalized_roi = cv2.cvtColor(ycrcb_roi, cv2.COLOR_YCrCb2BGR)

        new_img[y1:y2, x1:x2] = equalized_roi
        cv2.rectangle(new_img, (x1, y1), (x2, y2), (0, 255, 0), 2)


img = cv2.imread('images/image1.jpg', cv2.IMREAD_GRAYSCALE)

new_img = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', equal)

while True:
    cv2.imshow('image', new_img)
    key = cv2.waitKey(1) & 0xFF

    if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()