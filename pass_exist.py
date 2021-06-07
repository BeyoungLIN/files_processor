# -*- coding: utf-8 -*-
# @Time   : 2021/5/31 01:08
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : pass_exist.py
import os

dirpath = '/Volumes/ExtremeSSD/金陵诗徵/金陵诗徵44巻_gray'
files = os.listdir(dirpath)
IMG_EXT = {'.jpg', '.png', '.tif', '.tiff', '.bmp', '.gif'}
count = 0
for file in files:
    if os.path.splitext(file)[1].lower() in IMG_EXT:

        if os.path.exists(os.path.join(dirpath, 'output', os.path.splitext(file)[0]) + '_res_recog.txt'):
            pass
        else:
            print(os.path.join(dirpath, 'output', os.path.splitext(file)[0]) + '_res_recog.txt')
            # count += 1
            # print(count)
            pass


