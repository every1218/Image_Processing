import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
new_img = None
img = None


def hist(event, x, y, flags, param):
    global ix, iy, drawing, new_img, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        new_img = img.copy()

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(new_img, (ix, iy), (x, y), (0, 255, 0), 2)
        img = new_img.copy()

        x1, y1 = min(ix, x), min(iy, y)
        x2, y2 = max(ix, x), max(iy, y)
        roi = img[y1:y2, x1:x2]

        if roi.size == 0:
            return

        hist = cv2.calcHist([roi], [0], None, [32], [0, 256])

        hist_img = np.full((256, 512, 1), 255, dtype=np.uint8)
        cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

        bin_width = int(round(512 / 32))
        for i in range(32):
            cv2.rectangle(hist_img, (i * bin_width, 255),
                ((i + 1) * bin_width, 255 - int(hist[i])), 0, -1)

        cv2.imshow('histogram', hist_img)
        cv2.imshow('image', new_img)



img = cv2.imread('images/image3.jpg', cv2.IMREAD_GRAYSCALE)

new_img = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', hist)

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF

    if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()

