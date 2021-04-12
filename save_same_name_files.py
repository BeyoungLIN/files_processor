# -*- coding: utf-8 -*-
# @Time   : 2021/4/11 20:14
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : save_same_name_files.py

import os


def name_add_tag(srcpath, targetpath):
    files = os.listdir(srcpath)
    # 遍历
    for file in files:
        full_srcfile_path = os.path.join(srcpath, file)  # 完整文件路径
        file_name = file[:-4]  # 提取文件名
        # full_tarfile_path = os.path.join(targetpath, file)
        # print(file_name)
        if full_srcfile_path.endswith('.jpg'):
            os.system('cp ' + full_srcfile_path + ' ' + targetpath + '/' + file_name + '_db.jpg')
            print('cp ' + full_srcfile_path + ' ' + targetpath + '/' + file_name + '_db.jpg')

    return


if __name__ == '__main__':
    path1 = '/Users/Beyoung/Desktop/Projects/DB/Dingxiu_1_demo_results_newdb'
    path2 = '/Users/Beyoung/Desktop/Projects/DB/Dingxiu_1_demo_results_res18的副本'

    name_add_tag(path1, path2)
