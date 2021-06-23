# -*- coding: utf-8 -*-
# @Time   : 2021/6/17 01:00
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : get_size_pic.py

from copy_files_4ocr import *
from extract_json import *
from test_api_v0 import ajust_boxes, test_one_adv
import time

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
                        test_one_adv(file_path, mod='mix')
                    except:
                        error_pics.append(file)
            print(error_pics)


def get_single_folder_linesize(root_dir):
    # root_dir = '/disks/sde/beyoung/files_processor/宝庆'
    files = os.listdir(root_dir)
    error = []
    flag = 0
    for file in files:
        if os.path.splitext(file)[1].lower() in IMG_EXT:
            file_path = os.path.join(root_dir, file)
            try:
                ajust_boxes(file_path, dbg=False)
                test_one_adv(file_path, mod='adv')
                test_one_adv(file_path, mod='mix')
                read_json_2txt(file_path[:-4] + '_resapi_mix.json.txt')
                flag += 1
            except:
                error.append(file)
    print('处理文件数:', flag)
    print(error)


IMG_EXT = {'.jpg', '.png', '.tif', '.tiff', '.bmp', '.gif'}
# root_path = '/disks/sde/beyoung/files_processor/OCR测试图像2'
root_path = '/disks/sde/beyoung/files_processor/金陵诗徵44巻_gray_pure'

root_list = [
    '/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_rectify',
    '/disks/sde/beyoung/files_processor/集_rectify',
    '/disks/sde/beyoung/files_processor/金陵诗徵44巻_gray_pure',
    '/disks/sde/beyoung/files_processor/6059.桐南凤岗李氏宗谱：三十二卷：[桐庐]',
]

# for root in root_list:
#     start_time = time.time()
#     get_single_folder_linesize(root)
#     # sin_folders(root)
#     source_path = os.path.join(root, 'output')
#     files = os.listdir(source_path)
#     target_path = root + '_res'
#     if not os.path.exists(target_path):
#         os.makedirs(target_path)
#     for file in files:
#         if os.path.isfile(os.path.join(source_path, file)):
#             os.system('cp ' + os.path.join(source_path, file) + ' ' + os.path.join(target_path, file))
#     end_time = time.time()
#     used_time = end_time - start_time
#     print(root + '\n处理时间', used_time)

get_single_folder_linesize(root_path)
# single_file = '/disks/sde/beyoung/files_processor/OCR测试图像2_old/史记1.jpg'
# ajust_boxes(single_file, dbg=False)
# test_one_adv(single_file, mod='mix')
