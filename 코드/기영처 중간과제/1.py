import cv2
import numpy as np

#1. 일본
def japan_flag():
    blue, green, red = 0, 0, 255

    img = np.full((400, 600, 3), 255, dtype=np.uint8)
    height, width, _ = img.shape
    center_x, center_y = width // 2, height // 2
    radius = height // 3

    cv2.namedWindow('Japan')
    cv2.createTrackbar('Blue', 'Japan', 0, 255, lambda x: None)
    cv2.createTrackbar('Green', 'Japan', 0, 255, lambda x: None)
    cv2.createTrackbar('Red', 'Japan', 255, 255, lambda x: None)
    cv2.setTrackbarPos('Blue', 'Japan', blue)
    cv2.setTrackbarPos('Green', 'Japan', green)
    cv2.setTrackbarPos('Red', 'Japan', red)


    while True:
        img.fill(255)
        blue = cv2.getTrackbarPos('Blue', 'Japan')
        green = cv2.getTrackbarPos('Green', 'Japan')
        red = cv2.getTrackbarPos('Red', 'Japan')

        for y in range(height):
            for x in range(width):
                if (x - center_x) ** 2 + (y - center_y) ** 2 < radius ** 2:
                    img[y, x] = [blue, green, red]

        cv2.imshow('Japan', img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyWindow('Japan')

#2. 체코
def czech_flag():
    height, width = 400, 600
    img= np.zeros((height, width, 3), dtype=np.uint8)

    img[0:height // 2, :] = [255, 255, 255] # 위쪽 흰색
    img[height // 2:height, :] = [0, 0, 255] # 아래쪽 빨강

    # 왼쪽 파랑
    center_x = width // 2
    center_y = height // 2

    for y in range(height):
        if y < center_y: #윗 삼각형
            limit = (center_x / center_y) * y
        else: #아래 삼각형
            limit = (center_x / (height - center_y)) * (height - y)

        for x in range(int(limit)):
            img[y, x] = [255, 0, 0]

    cv2.imshow('Czech', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Czech')


#3. 알제리
def algeria_flag():
    height, width = 400, 600
    green = [0, 150, 0]
    red = [0, 0, 255]
    white = [255, 255, 255]

    img = np.full((height, width, 3), white, dtype=np.uint8)

    center_x = width // 2
    center_y = height // 2
    out_radius = int(height * 0.25)
    in_radius = int(out_radius * 0.8)
    in_x = center_x + int(out_radius * 0.2)

    # 왼쪽 초록
    img[:, 0:width // 2] = green

    # 초승달) 빨간색 원
    cv2.circle(img, (center_x, center_y), out_radius, red, -1)

    # 초승달) 안쪽 흰색 원
    cv2.circle(img, (in_x, center_y), in_radius, white, -1, lineType=cv2.LINE_AA)

    # 초승달) 안쪽 원의 왼쪽 초록색
    inner_circle_mask = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(inner_circle_mask, (in_x, center_y), in_radius, 255, -1, lineType=cv2.LINE_AA)

    for y in range(height):
        for x in range(width):
            if inner_circle_mask[y, x] == 255 and x < center_x:
                img[y, x] = green


    # 별)
    out_r = int(height * 0.12)  # 별 밖 반지름
    in_r = int(out_r * 0.4)  # 별 안 반지름
    star_x = center_x + int(out_radius * 0.45)
    star_y = center_y - int(out_r * 0.2)

    start_dig = 80  # 시작각도
    star_arr = []
    for i in range(5):
        # 바깥쪽 꼭짓점
        out_dig = np.deg2rad(start_dig + i * 72)
        out_x = int(star_x + out_r * np.cos(out_dig))
        out_y = int(star_y - out_r * np.sin(out_dig))
        star_arr.append([out_x, out_y])

        # 안쪽 꼭짓점
        in_dig = np.deg2rad(start_dig + 36 + i * 72)
        in_x = int(star_x + in_r * np.cos(in_dig))
        in_y = int(star_y - in_r * np.sin(in_dig))
        star_arr.append([in_x, in_y])

    result = np.array(star_arr, dtype=np.int32)

    cv2.fillPoly(
        img=img,
        pts=[result],
        color=red,
        lineType=cv2.LINE_AA
    )

    cv2.imshow('Algeria', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Algeria')


#4. 한국
def korean_flag():
    # 막대기
    def draw_bar(img, pt, w, bars):
        pt = np.array(pt, np.int32)
        for bar in bars:
            (x, y), h = pt, w * 6

            # 기본막대
            cv2.rectangle(img, (x, y, w, h), (0, 0, 0), -1)

            # 끊어진 막대
            if bar == 0:
                y = y + w * 3 - w // 4
                h = w // 2
                cv2.rectangle(img, (x, y, w, h), (255, 255, 255), -1)

            pt += (int(w * 1.5), 0)

    size = 200
    out_r, in_r = size//2, size//4
    center, canvas = size * 2, size * 4

    img = np.full((canvas, canvas, 3), 255, np.uint8)
    blue, red = (255, 0, 0), (0, 0, 255)

    # 태극 문양
    cv2.ellipse(img, (center, center), (out_r, out_r), 0, 0, 180, blue, -1)
    cv2.ellipse(img, (center, center), (out_r, out_r), 180, 0, 180, red, -1)
    cv2.ellipse(img, (center + out_r - in_r, center), (in_r, in_r), 180, 0, 180, blue, -1)
    cv2.ellipse(img, (center - in_r, center), (in_r, in_r), 0, 0, 180, red, -1)

    # 막대
    left_pt = (center - size * (18 + 8) / 24, center - in_r)
    right_pt = (center + size * (18 + 0) / 24, center - in_r)
    bar_w = size // 12  #

    # 1. 건곤
    draw_bar(img, left_pt, bar_w, (1, 1, 1)) #건
    draw_bar(img, right_pt, bar_w, (0, 0, 0)) #곤
    angle_deg = cv2.fastAtan2(2, 3)
    rot_matrix1 = cv2.getRotationMatrix2D((center, center), -angle_deg * 2, 1)
    img = cv2.warpAffine(img, rot_matrix1, (canvas, canvas))

    #2. 감리
    draw_bar(img, left_pt, bar_w, (1, 0, 1))  #감
    draw_bar(img, right_pt, bar_w, (0, 1, 0))  #리
    rot_matrix2 = cv2.getRotationMatrix2D((center, center), angle_deg, 1)
    img = cv2.warpAffine(img, rot_matrix2, (canvas, canvas))

    result = img[center - size:center + size,
    center - out_r * 3:center + out_r * 3]

    cv2.imshow('Korean', result)
    cv2.waitKey(0)
    cv2.destroyWindow('Korean')

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if 0 <= y < main_h // 2:
            if 0 <= x < main_w // 2:
                japan_flag()
            elif main_w // 2 <= x < main_w:
                czech_flag()
        elif main_h // 2 <= y < main_h:
            if 0 <= x < main_w // 2:
                algeria_flag()
            elif main_w // 2 <= x < main_w:
                korean_flag()


# 메인 화면
main_img = np.full((300, 400, 3), 255, dtype=np.uint8)
main_h, main_w, _ = main_img.shape

# 메인화면 십자가 선
cv2.line(main_img, (main_w // 2, 0), (main_w // 2, main_h), (0, 0, 0), 1)
cv2.line(main_img, (0, main_h // 2), (main_w, main_h // 2), (0, 0, 0), 1)

# 텍스트
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(main_img, 'Japan', (main_w // 4 - 40, main_h // 4), font, 1, (0, 0, 0), 2)
cv2.putText(main_img, 'Czech', (main_w * 3 // 4 - 40, main_h // 4), font, 1, (0, 0, 0), 2)
cv2.putText(main_img, 'Algeria', (main_w // 4 - 50, main_h * 3 // 4), font, 1, (0, 0, 0), 2)
cv2.putText(main_img, 'Korea', (main_w * 3 // 4 - 40, main_h * 3 // 4), font, 1, (0, 0, 0), 2)

cv2.imshow('Flags', main_img)
cv2.setMouseCallback('Flags', mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()