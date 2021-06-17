# -*- coding: utf-8 -*-
# @Time   : 2021/6/17 01:00
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : get_size_pic.py

from test_api_v0_ import ajust_boxes, test_one_adv
import os

root_dir = '/disks/sde/beyoung/files_processor/宝庆'
files = os.listdir(root_dir)
error = []
for file in files:
    if file.endswith('.jpg'):
        file_path = os.path.join(root_dir, file)
        try:
            ajust_boxes(file_path, dbg=False)
            test_one_adv(file_path, mod='adv')
        except:
            error.append(file)
print(error)
