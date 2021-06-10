# -*- coding: utf-8 -*-
# @Time   : 2021/6/8 08:37
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : run_double_folders_draw_box.py

from test_api_v0_test import *
import os
import time
IMG_EXT = {'.jpg', '.png', '.tif', '.tiff', '.bmp', '.gif'}

def run_double_folders():
    dir_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2'
    dirs = os.listdir(dir_path)
    AttributeError_pics = []
    otherError_pics = []
    num = 0
    strart_time = time.time()
    for dir in dirs:
        # print(dir)
        if os.path.isdir(os.path.join(dir_path, dir)):
            if not dir == 'output':
                files = os.listdir(os.path.join(dir_path, dir))
                # print(files)
                for file in files:
                    if os.path.splitext(file)[1].lower() in IMG_EXT:
                        num += 1
                        # try:
                        # pth_img = readPILImg(os.path.join(dir_path, dir, file))
                        pth_img = os.path.join(dir_path, dir, file)
                        ajust_boxes(pth_img, dbg=False)
                        # except:
                        #     AttributeError_pics.append(file)
                        #     print(file)
                        end_time = time.time()
                        used_time = end_time - strart_time
                        rest_time = used_time / num * (len(files) - num)
                        print(str(round(num / len(files) * 100, 2)) + '% rest_time: ', rest_time)

    print('AttributeError_pics:\n', AttributeError_pics)

dir_path = '/disks/sde/beyoung/files_processor/宝庆'
files = os.listdir(dir_path)
AttributeError_pics = []
otherError_pics = []
num = 0
strart_time = time.time()

for file in files:
    if os.path.splitext(file)[1].lower() in IMG_EXT:
        num += 1
        # try:
        # pth_img = readPILImg(os.path.join(dir_path, dir, file))
        pth_img = os.path.join(dir_path, file)
        ajust_boxes(pth_img, dbg=False)
        # except:
        #     AttributeError_pics.append(file)
        #     print(file)
        end_time = time.time()
        used_time = end_time - strart_time
        rest_time = used_time / num * (len(files) - num)
        print(str(round(num / len(files) * 100, 2)) + '% rest_time: ', rest_time)

print('AttributeError_pics:\n', AttributeError_pics)