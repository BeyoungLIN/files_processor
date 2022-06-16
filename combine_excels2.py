# -*- coding: utf-8 -*-
# @Time   : 2021/6/21 00:30
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : combine_excels2.py

import os

import pandas as pd

# 文件路径
# file_dir = r'input root path'
file_dirs = [
    # '/Users/Beyoung/Library/Mobile Documents/com~apple~CloudDocs/20软微/党团公务/新增党员信息/attachments',
    # '/Users/Beyoung/Library/Mobile Documents/com~apple~CloudDocs/20软微/党团公务/新增党员信息/attachments (1)',
    '/Users/Beyoung/Library/Mobile Documents/com~apple~CloudDocs/20软微/党团公务/2022新增党员/'
]
new_list = []

for file_dir in file_dirs:
    # 构建新的表格名称
    new_filename = file_dir + '/new_file.xls'
    # 找到文件路径下的所有表格名称，返回列表
    file_list = os.listdir(file_dir)

    for file in file_list:
        print(file)
        if file.endswith('.xlsx'):
            # 重构文件路径
            file_path = os.path.join(file_dir, file)
            # 将excel转换成DataFrame
            dataframe = pd.read_excel(file_path)
            # 保存到新列表中
            new_list.append(dataframe)

# 多个DataFrame合并为一个
df = pd.concat(new_list)
# 写入到一个新excel表中
df.to_excel(new_filename, index=False)
