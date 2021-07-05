# -*- coding: utf-8 -*-
# @Time   : 2021/7/5 22:36
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : inverse.py

import cv2
src=cv2.imread("/Users/Beyoung/Desktop/Projects/AC_OCR/pkuocrtest-20210705/00047.tif",1)
print(src.shape)
Img=255-src
print(Img.shape)
# cv2.imshow("Img",Img)
# cv2.imshow("src",src)
# cv2.waitKey(0)
cv2.imwrite('/Users/Beyoung/Desktop/Projects/AC_OCR/pkuocrtest-20210705/00047_inverse.tif',Img)