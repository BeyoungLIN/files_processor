# -*- coding: utf-8 -*-
# @Time   : 2021/6/8 13:26
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : copy_files_4ocr.py


import os
import time


def dul_folders(root_path, target_path=None):
    # source_path = '/Volumes/ExtremeSSD/金陵诗徵/金陵诗徵44巻_gray/output'
    # root_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2'
    # target_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2_size_pic'
    if not target_path:
        target_path = root_path + '_res'

    if not os.path.exists(target_path):
        os.mkdir(target_path)

    error_pics = []
    dirs = os.listdir(root_path)
    for dire in dirs:
        dir_path = os.path.join(root_path, dire)
        # print(dir_path)
        if os.path.isdir(dir_path):
            dir_path_2 = os.path.join(dir_path, 'output')
            files = os.listdir(dir_path_2)
            if not os.path.exists(os.path.join(target_path, dire)):
                os.mkdir(os.path.join(target_path, dire))
            for file in files:
                # if (file.endswith('recog_adv.txt')) or (file.endswith('rec_uboxes_size.jpg')):
                if os.path.isfile(os.path.join(dir_path_2, file)):
                    # os.system('cp ' + os.path.join(source_path, file) + ' ' + os.path.join(target_path, file))
                    # try:
                    os.system('cp ' + os.path.join(dir_path_2, file) + ' ' + os.path.join(target_path, dire, file))
                    # except:
                    #     error_pics.append(file)
    print(error_pics)


def sin_folders(root_path, target_path=None):
    # target_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/宝庆_uboxes_pics'
    if not target_path:
        target_path = root_path + '_res'

    root_path = os.path.join(root_path, 'output')

    if not os.path.exists(target_path):
        os.mkdir(target_path)

    # root_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/宝庆/output'
    error_pics = []
    files = os.listdir(root_path)
    # for file in files:
    # dir_path = os.path.join(root_path, dire)
    # # print(dir_path)
    # if os.path.isdir(dir_path):
    #     dir_path_2 = os.path.join(dir_path, 'output')
    #     files = os.listdir(dir_path_2)
    # print(files)
    for file in files:
        # if (file.endswith('recog_adv.txt')) or (file.endswith('rec_uboxes_size.jpg')):
        if os.path.isfile(os.path.join(root_path, file)):
            # try:
            os.system('cp ' + os.path.join(root_path, file) + ' ' + os.path.join(target_path, file))
            # except:
            #     error_pics.append(file)
    print(error_pics)

def copy_file(root_list):
    # 页面提取自－集韵（述古堂影宋钞本_ 上海古籍）上_页面_071_res_recog_adv.txt
    # 页面提取自－集韵（述古堂影宋钞本_ 上海古籍）上_页面_071rec_uboxes_size.jpg
    # root = '/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_rectify/output'
    # root = '/disks/sde/beyoung/files_processor/OCR测试图像2'
    # root = '/disks/sde/beyoung/files_processor/金陵诗徵44巻_gray_pure'
    # root = '/disks/sde/beyoung/files_processor/集'
    # target = '/disks/sde/beyoung/files_processor/宝庆/output_size+pic'
    # target = '/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_rectify_size_pic'

    for root in root_list:
        start_time = time.time()
        # source_path = os.path.join(root, 'output')
        # files = os.listdir(source_path)
        # target_path = root + '_res'
        # if not os.path.exists(target_path):
        #     os.makedirs(target_path)
        # for file in files:
        # if file.endswith('_mix.json.txt'):
        sin_folders(root)
        end_time = time.time()
        used_time = end_time - start_time
        print(root + '\n处理时间', used_time)

    # sin_folders(root)
    # dul_folders(root)

if __name__ == '__main__':
    root_list = [
        # '/disks/sdd/beyoung/data/國家圖書館藏敦煌遺書_001',
        # '/disks/sdd/beyoung/data/2563[函368]',
        # '/disks/sdd/beyoung/data/纂図互註荀子3',
        # '/disks/sde/beyoung/files_processor/6059.桐南凤岗李氏宗谱：三十二卷：[桐庐]',
        '/disks/sdd/beyoung/data/测试7.5',
        '/disks/sdd/beyoung/data/pkuocrtest-20210705',
    ]

    copy_file(root_list)