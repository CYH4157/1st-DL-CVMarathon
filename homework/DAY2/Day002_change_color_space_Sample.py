import cv2

img_path = './lena.png'

# 以彩色圖片的方式載入
#img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 改變不同的 color space
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_LAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img_HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    cv2.imshow('bgr', img)
    cv2.imshow('hsv', img_hsv)
    cv2.imshow('LAB', img_LAB)
    cv2.imshow('HLS', img_HLS)
    
    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break