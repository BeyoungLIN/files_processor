# -*- coding: utf-8 -*-
# @Time   : 2021/6/20 02:44
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : copy_4conditions.py
import os


def sin_folders(root_path, source_path, target_path):
    error_pics = []
    # target_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/宝庆_uboxes_pics'
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    files = os.listdir(root_path)

    for i in range(135):
        file = '6060.凤岗李氏宗谱[桐庐]_' + str(i) + '_rectifyrec_uboxes_size.jpg'
        if file not in files:
            ori_file = '6060.凤岗李氏宗谱[桐庐]_' + str(i) + '_rectify.jpg'
            error_pics.append(ori_file)
            os.system('cp ' + os.path.join(source_path, ori_file) + ' ' + os.path.join(target_path, ori_file))
            # except:
            #     error_pics.append(file)
    print(error_pics)


# 页面提取自－集韵（述古堂影宋钞本_ 上海古籍）上_页面_071_res_recog_adv.txt
# 页面提取自－集韵（述古堂影宋钞本_ 上海古籍）上_页面_071rec_uboxes_size.jpg
source = '/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_rectify'
root = '/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_rectify_size_pic/'
# '6060.凤岗李氏宗谱[桐庐]_1_rectify.jpg'
# '6060.凤岗李氏宗谱[桐庐]_133_rectifyrec_uboxes_size.jpg'
target = '/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_error'
# sin_folders(root, target)
sin_folders(root, source, target)
