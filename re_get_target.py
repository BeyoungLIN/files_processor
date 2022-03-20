# -*- coding: utf-8 -*-
# @Time   : 2022/3/20 11:50
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : re_get_target.py

import re
pth = "/Users/Beyoung/Desktop/Projects/ben's crawler/geek/算法训练营2021版-代码模板.html"
with open(pth, 'r') as w:
    con = w.read()

p_pic = re.compile(r'!\[\]\((.*?)\){')
pics = p_pic.findall(con)

print(pics)

#
# pth_ls = [
#     # '/Users/Beyoung/Desktop/Projects/corpus/卷一（鄒司奧）的副本.md',
#     '/Users/Beyoung/Desktop/Projects/oracle/bamboo_doc/卷一（鄒司奧）的副本.md',
#     '/Users/Beyoung/Desktop/Projects/corpus/清华简1——7/清華簡1~7/卷二（刁筱蓉）.md'
#     ]
#     # pth = '/Users/Beyoung/Desktop/Projects/corpus/卷一（鄒司奧）的副本.md'
#     for pth in pth_ls:
#         with open(pth, 'r') as f:
#             # content = f.read()
#             lines = f.readlines()
#         # print(lines[:20])
#         # pattern_pic = r'(.*?)media/(.*?)'
#         # pattern_label = r'(.*?)media/(.*?)'
#         p_pic = re.compile(r'!\[\]\((.*?)\){')
#         p_label = re.compile(r'"}(.*?)[!\n]')
#         p_sub_char = re.compile(r'(.*?)[!]')
#         char = '一'
#         for line_no, line in enumerate(lines[:]):
#             if line == '\n':
#                 continue
#             if 'media' not in line:
#                 char = line.strip()
#                 char = char.replace('\\', '')
#                 print(char)
#                 sav_char_pth = f'res/{char}'
#                 if not os.path.exists(sav_char_pth):
#                     os.makedirs(sav_char_pth)
#             else:
#                 pics = p_pic.findall(line)
#                 lables = p_label.findall(line)
#                 sub_char = p_sub_char.findall(line)
#                 print(pics)
#                 print(lables)
#                 print(sub_char)
#                 print()
#                 if len(pics) == 1 and len(lables) == 1 and lables[0] == '':
#                     if sub_char[0] != '':
#                         print(0)
#                         com1 = f'cp {pics[0]} ./res/{char}/{sub_char[0]}.png'
#                         os.system(com1)
#                     else:
#                         print(1)
#                         com1 = f'cp {pics[0]} ./res/{char}/{char}_{line_no}.png'
#                         os.system(com1)
#                 else:
#                     for i in range(len(pics)):
#                         print(3)
#                         label = lables[i]
#                         label = label.replace(' ', '')
#                         pic = pics[i]
#                         if label == '':
#                             label = f'{char}_{line_no}'
#                         com1 = f'cp {pics[i]} ./res/{char}/{label}.png'
#                         os.system(com1)