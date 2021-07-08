# -*- coding: utf-8 -*-
# @Time   : 2021/7/5 22:36
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : inverse.py

import cv2

src_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/pkuocrtest-20210705/00049.tif'
src = cv2.imread(src_path, 1)
print(src.shape)
src = cv2.resize(src, (round(1/4 * src.shape[1]), round(1/4 * src.shape[0])))
# src = cv2.resize(src, (176, 704))
Img = 255 - src
print(Img.shape)
# cv2.imshow("Img",Img)
# cv2.imshow("src",src)
# cv2.waitKey(0)
cv2.imwrite(src_path[:-4] + '_inverse.tif', Img)
