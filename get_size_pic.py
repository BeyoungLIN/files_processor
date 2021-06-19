# -*- coding: utf-8 -*-
# @Time   : 2021/6/17 01:00
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : get_size_pic.py

import os

from test_api_v0_ import ajust_boxes, test_one_adv



def get_double_folder_linesize(root_path):
    # root_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2'
    error_pics = []
    dirs = os.listdir(root_path)
    for dire in dirs:
        dir_path = os.path.join(root_path, dire)
        # print(dir_path)
        if os.path.isdir(dir_path):
            dir_path_2 = os.path.join(dir_path)
            files = os.listdir(dir_path_2)
            for file in files:
                if os.path.splitext(file)[1].lower() in IMG_EXT:
                    file_path = os.path.join(dir_path_2, file)
                    try:
                        ajust_boxes(file_path, dbg=False)
                        test_one_adv(file_path, mod='adv')
                    except:
                        error_pics.append(file)
            print(error_pics)


def get_single_folder_linesize(root_dir):
    # root_dir = '/disks/sde/beyoung/files_processor/宝庆'
    files = os.listdir(root_dir)
    error = []
    for file in files:
        if file.endswith('.jpg'):
            file_path = os.path.join(root_dir, file)
            # try:
            ajust_boxes(file_path, dbg=False)
            test_one_adv(file_path, mod='adv')
            # except:
            #     error.append(file)
    print(error)

IMG_EXT = {'.jpg', '.png', '.tif', '.tiff', '.bmp', '.gif'}
root_path = '/disks/sde/beyoung/files_processor/OCR测试图像2/寒山诗集（字大工整）'
# get_single_folder_linesize(root_path)
single_file = '/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_rectify/6060.凤岗李氏宗谱[桐庐]_3_rectify.jpg'
ajust_boxes(single_file, dbg=False)
test_one_adv(single_file, mod='adv')
