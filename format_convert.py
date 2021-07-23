# -*- coding: utf-8 -*-
# @Time   : 2021/7/19 22:54
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : format_convert.py

import os

from PIL import Image


def gif2jpg(input, output):
    gif_file = input
    img = Image.open(gif_file)
    # print(img.mode, img.format)  # P  和  GIF
    img = img.convert('RGB')
    # print(img.mode, img.format)
    img.save(output)

    # img2 = Image.open('223.jpg')
    # print(img2.format)  # JPEG
    return


PIC_SET = ['.gif', '.tif', '.jpg', '.jepg']
path = '/Users/Beyoung/Desktop/Projects/ER/dataset/ER007/228_41142'
op_path = path + '_jpg'
if not os.path.exists(op_path):
    os.mkdir(op_path)
files = os.listdir(path)
for file in files:
    if os.path.splitext(os.path.join(path, file))[-1].lower() in PIC_SET:
        # if file.startswith('.gif'):
        print(os.path.join(path, file)[:-4] + '.jpg')
        gif2jpg(os.path.join(path, file), os.path.join(op_path, file)[:-4] + '.jpg')
