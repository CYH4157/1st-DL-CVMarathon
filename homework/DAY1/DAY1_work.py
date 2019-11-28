# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:25:21 2019

@author: 1903012
"""
import matplotlib.pyplot as plt 
import cv2
import numpy as np


img_path = './lena.png'
#img_path = "lena.png"

# 以彩色圖片的方式載入
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 以灰階圖片的方式載入
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# 注意，openCV 通道排列為 BGR，這個套件通道排序不同
# openCV 套件內的 RBG 分離套件
#b,g,r = cv2.split(img)

# Numpy 分離通道，創建3個跟影像大小的空矩陣

b = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
g = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
r = np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
 
b[:,:] = img[:,:,0]  #  b 通道的分量數據
g[:,:] = img[:,:,1]  #  g 通道的分量數據
r[:,:] = img[:,:,2]  #  r 通道的分量數據


# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    # 顯示彩圖
#    cv2.imshow('RGB', img)
    cv2.imshow('r', r)
    cv2.imshow('g', g)
    cv2.imshow('b', b)
#    cv2.imshow('rg', rg)

    # 顯示灰圖
#    cv2.imshow('gray', img_gray)

    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break