# -*- coding: utf-8 -*-
# @Time   : 2021/5/12 08:31
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : split_test.py

import os

folders = '/Users/Beyoung/Desktop/Projects/Fakepages_lastest/configs/'

files = os.listdir(folders)

for file in files:
    print('python generate_specific_book_pages.py --config configs/'+file)
    print('mv data/book_pages data/book_pages_' + file[:-5])
    print()
'''
config = '' \
         'configs/blank_at_right.json' \
         ''
config = config.split('/')[-1][:-5]
# config = config[0, -4]
print(config)
'''
