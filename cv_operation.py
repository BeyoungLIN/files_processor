# -*- coding: utf-8 -*-
# @Time   : 2021/11/30 18:59
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : cv_operation.py

import cv2 as cv
import numpy as np
import os

def contrast_1(img):
    alpha = 0.99
    beta = 30
    img = np.uint8(np.clip((alpha * img + beta), 0, 255))
    return img


def contrast_2(img, c, b): # C 是对比度，b 是亮度
    # cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)  # 给图片显示的窗口命名为input image
    h, w = img.shape
    blank = np.zeros([h, w], img.dtype)
    # contrast_brightness_demo(src, 1.2, 100)
    img = cv.addWeighted(img, c, blank, 1 - c, b)  # 改变像素的API
    return img



def gray(img):
    # img = Image.open(img_path)
    # img.show()
    # low = img.convert('L')
    # low.save(img_path)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img

'''
https://www.jiqizhixin.com/articles/2019-03-22-10
'''

if __name__ == '__main__':
    pic_list = [
        '/Users/Beyoung/Desktop/Projects/corpus/ZHSY000025-000296fortest/ZHSY000025-000296.tif',
        '/Users/Beyoung/Desktop/Projects/corpus/ZHSY000025-000296fortest/ZHSY000025-000269.tif',
        '/Users/Beyoung/Desktop/Projects/corpus/ZHSY000025-000296fortest/ZHSY000025-000265.tif',
        '/Users/Beyoung/Desktop/Projects/corpus/ZHSY000025-000296fortest/ZHSY000025-000261.tif',
        '/Users/Beyoung/Desktop/Projects/corpus/ZHSY000025-000296fortest/ZHSY000025-000258.tif',
        '/Users/Beyoung/Desktop/Projects/corpus/ZHSY000025-000296fortest/ZHSY000025-000243.tif',
    ]
    for pic in pic_list:
        pic_op_pth = os.path.splitext(pic)[0] + '_op' + os.path.splitext(pic)[-1]
        src = cv.imread(pic)
        src = gray(src)
        src = contrast_2(src, 1.2, 0)
        cv.imwrite(pic_op_pth, src)
        # cv.imshow("con-bri-demo", dst)
        # cv.waitKey(0)  # 等待下一步指令
        # cv.destroyAllWindows()  # 为了能正常关闭所有的绘图窗口。
