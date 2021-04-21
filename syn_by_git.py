# -*- coding: utf-8 -*-
# @Time   : 2021/4/14 09:30
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : syn_by_git.py

import os

root_path = 'fakepages_data/book_pages/'
folders = os.listdir(root_path)

for folder in folders:
    if os.path.isdir(os.path.join(root_path, folder)):
        for num in range(100):
            file_name = 'book_page_' + str(num) + '.jpg'
            file_path = os.path.join(root_path, folder, 'imgs_v', file_name)
            try:
                os.system('git add ' + file_path)
            except:
                print('error: ' + file_path)
