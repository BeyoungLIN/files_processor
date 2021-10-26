# -*- coding: utf-8 -*-
# @Time   : 2021/10/7 19:50
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : 检测纯黑图片.py

import cv2
import numpy as np
# 导入模块
from PIL import Image

# 打开图像
path = '/Users/Beyoung/Desktop/Projects/files_processor/apic18171.jpg'
im = Image.open("/Users/Beyoung/Desktop/Projects/files_processor/apic18171.jpg")
img = np.array(im)
# 调用getbbox()
box = im.getbbox()
# 输出
print(box)

list_colors = im.getcolors()
# 输出
print(list_colors)

img_cv = cv2.imread(path)  # 读取数据
thresh, img_bi = cv2.threshold(img_cv, 130, 255, cv2.THRESH_BINARY)
img_opencv_np = np.array(img_bi)  # opencv转为ndarray数组
# count = cv2.countNonZero(path)
print(img_opencv_np)
count = np.count_nonzero(img_opencv_np)
print(count)
