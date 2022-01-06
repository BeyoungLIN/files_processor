# -*- coding: utf-8 -*-
# @Time   : 2021/12/29 20:05
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : cut_pic.jpg.py

import cv2
import math
import os
# import numpy as np


def cut_pic(pth='', pic_no=2):
    img = cv2.imread(pth)
    img_gray = cv2.imread(pth, 0)
    h, w = img_gray.shape
    # cv2.imshow('img', img_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    pic_h = math.ceil(float(h) / pic_no)
    y2 = 0
    for img_i in range(pic_no):
        x1, y1, x2, y2 = 0, y2, w, min(h, y2 + pic_h)
        y_move = 0
        while True:
            line_p = img_gray[y2 + y_move if y2 + y_move < h else h-1, 0:w]
            line_dict = {}
            for i in line_p:
                if line_p[i] not in line_dict:
                    line_dict[line_p[i]] = 1
                else:
                    line_dict[line_p[i]] += 1
            # print(line_dict)
            max_v = max(line_dict.values())
            if max_v >= w * 0.8:
                y2 += y_move
                y2 += 2
                img_part = img[y1: y2, x1: x2]
                cv2.imwrite(os.path.splitext(pth.split('/')[-1])[0] + '_' + str(img_i) + '.jpg', img_part)
                break
            else:
                y_move += 1
        if y2 >= h - 1:
            break


if __name__ == '__main__':
    '''
    把程序放在图片所在目录, 在cut_pic函数内输入图片路径及想要切开的图片数即可
    '''
    pth = ''
    try:
        cut_pic(pth, pic_no=2)
    except ModuleNotFoundError as e:
        os.system('pip install opencv-python')
        cut_pic(pth, pic_no=2)



