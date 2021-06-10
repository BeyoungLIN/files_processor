# -*- coding: utf-8 -*-
# @Time   : 2021/6/8 13:26
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : copy_files_4ocr.py


import os

def dul_folders():
    source_path = '/Volumes/ExtremeSSD/金陵诗徵/金陵诗徵44巻_gray/output'
    target_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2_uboxes_pics'

    root_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2'
    error_pics = []
    dirs = os.listdir(root_path)
    for dire in dirs:
        dir_path = os.path.join(root_path, dire)
        # print(dir_path)
        if os.path.isdir(dir_path):
            dir_path_2 = os.path.join(dir_path, 'output')
            files = os.listdir(dir_path_2)
            for file in files:
                if file.endswith('uboxes_g.jpg'):
                    # try:
                    if not os.path.exists(os.path.join(target_path, dire)):
                        os.mkdir(os.path.join(target_path, dire))
                    os.system('cp ' + os.path.join(dir_path_2, file) + ' ' + os.path.join(target_path, dire, file))
                    # except:
                    #     error_pics.append(file)
    print(error_pics)


def sin_folders():
    source_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/宝庆/output'
    target_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/宝庆_uboxes_pics'

    root_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/宝庆/output'
    error_pics = []
    files = os.listdir(root_path)
    # for file in files:
        # dir_path = os.path.join(root_path, dire)
        # # print(dir_path)
        # if os.path.isdir(dir_path):
        #     dir_path_2 = os.path.join(dir_path, 'output')
        #     files = os.listdir(dir_path_2)
    print(files)
    for file in files:
        if file.endswith('uboxes_g.jpg'):
            # try:
            if not os.path.exists(target_path):
                os.mkdir(target_path)
            os.system('cp ' + os.path.join(root_path, file) + ' ' + os.path.join(target_path, file))
            # except:
            #     error_pics.append(file)
    print(error_pics)

sin_folders()