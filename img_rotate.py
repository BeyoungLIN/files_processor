# -*- coding: utf-8 -*-
# @Time   : 2021/6/17 23:50
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : img_rotate.py


import cv2
import numpy as np

import numpy as np
import cv2


## 图片旋转
# def rotate_bound(image, angle):
#     # 获取宽高
#     (h, w) = image.shape[:2]
#     (cX, cY) = (w // 2, h // 2)
#
#     # 提取旋转矩阵 sin cos
#     M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
#     cos = np.abs(M[0, 0])
#     sin = np.abs(M[0, 1])
#
#     # 计算图像的新边界尺寸
#     nW = int((h * sin) + (w * cos))
#     #     nH = int((h * cos) + (w * sin))
#     nH = h
#
#     # 调整旋转矩阵
#     M[0, 2] += (nW / 2) - cX
#     M[1, 2] += (nH / 2) - cY
#
#     return cv2.warpAffine(image, M, (nW, nH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
#
#
# ## 获取图片旋转角度
# def get_minAreaRect(image):
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     gray = cv2.bitwise_not(gray)
#     thresh = cv2.threshold(gray, 0, 255,
#                            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#     coords = np.column_stack(np.where(thresh > 0))
#     return cv2.minAreaRect(coords)
#
#
# image_path = "/Users/Beyoung/Desktop/Projects/AC_OCR/OCR/6060.凤岗李氏宗谱[桐庐]_8.jpg"
# image = cv2.imread(image_path)
# angle = get_minAreaRect(image)[-1]
# rotated = rotate_bound(image, angle)
#
# cv2.putText(rotated, "angle: {:.2f} ".format(angle),
#             (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
#
# # show the output image
# print("[INFO] angle: {:.3f}".format(angle))
# cv2.imshow("imput", image)
# cv2.imshow("output", rotated)
# cv2.waitKey(0)
#
# pic_file = r'/Users/Beyoung/Desktop/Projects/AC_OCR/OCR/6060.凤岗李氏宗谱[桐庐]_8.jpg'
# im_bgr = cv2.imread(pic_file)  # 读入图像
# im_gray = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2GRAY)  # 转灰度
# im_gray = cv2.GaussianBlur(im_gray, (3, 3), 0)  # 滤波降噪
# im_edge = cv2.Canny(im_gray, 30, 50)  # 边缘检测
# cv2.imshow('Go', im_edge)  # 显示边缘检测结果
# cv2.waitKey(0)


# contours, hierarchy = cv2.findContours(im_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 提取轮廓
# rect, area = None, 0  # 找到的最大四边形及其面积
# for item in contours:
#     hull = cv2.convexHull(item)  # 寻找凸包
#     epsilon = 0.1 * cv2.arcLength(hull, True)  # 忽略弧长10%的点
#     approx = cv2.approxPolyDP(hull, epsilon, True)  # 将凸包拟合为多边形
#     if len(approx) == 4 and cv2.isContourConvex(approx):  # 如果是凸四边形
#         ps = np.reshape(approx, (4, 2))
#         ps = ps[np.lexsort((ps[:, 0],))]
#         lt, lb = ps[:2][np.lexsort((ps[:2, 1],))]
#         rt, rb = ps[2:][np.lexsort((ps[2:, 1],))]
#         a = cv2.contourArea(approx)  # 计算四边形面积
#         if a > area:
#             area = a
#             rect = (lt, lb, rt, rb)
#
# if rect is None:
#     print('在图像文件中找不到棋盘！')
# else:
#     print('棋盘坐标：')
#     print('\t左上角：(%d,%d)' % (rect[0][0], rect[0][1]))
#     print('\t左下角：(%d,%d)' % (rect[1][0], rect[1][1]))
#     print('\t右上角：(%d,%d)' % (rect[2][0], rect[2][1]))
#     print('\t右下角：(%d,%d)' % (rect[3][0], rect[3][1]))
#
# im = np.copy(im_bgr)
# for p in rect:
#     im = cv2.line(im, (p[0] - 10, p[1]), (p[0] + 10, p[1]), (0, 0, 255), 1)
#     im = cv2.line(im, (p[0], p[1] - 10), (p[0], p[1] + 10), (0, 0, 255), 1)
# cv2.imshow('go', im)
# cv2.waitKey(0)
#


import os
import cv2
import math
import random
import numpy as np
from scipy import misc, ndimage
import matplotlib.pyplot as plt

filepath = './'

def rotate(img_path, out_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # 霍夫变换
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 0)
    rotate_angle = 0
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        if x1 == x2 or y1 == y2:
            continue
        t = float(y2 - y1) / (x2 - x1)
        rotate_angle = math.degrees(math.atan(t))
        if rotate_angle > 45:
            rotate_angle = -90 + rotate_angle
        elif rotate_angle < -45:
            rotate_angle = 90 + rotate_angle
    print("rotate_angle : " + str(rotate_angle))
    rotate_img = ndimage.rotate(img, rotate_angle)
    cv2.imwrite(out_path, rotate_img)
    # cv2.imshow("img", rotate_img)
    # cv2.waitKey(0)

def sin_folders(root_path, target_path):
    # target_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/宝庆_uboxes_pics'
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    error_pics = []
    files = os.listdir(root_path)
    # print(files)
    for file in files:
        if file.endswith('.jpg'):
            # try:
            rotate(os.path.join(root_path, file), os.path.join(target_path, file[:-4]+'_rectify.jpg'))
            # except:
            #     error_pics.append(file)
    print(error_pics)

root = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR/6060.凤岗李氏宗谱[桐庐]'
target = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR/6060.凤岗李氏宗谱[桐庐]_rectify'
sin_folders(root, target)
