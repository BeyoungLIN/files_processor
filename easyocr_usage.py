# -*- coding: utf-8 -*-
# @Time   : 2022/2/22 21:25
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : easyocr_usage.py

import os
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import sys

sys.path.append(r"../oracle/utils.py")
# import utils.

# IMAGE_PATH = '../oracle/result/甲骨文字編-李宗焜_cut_cor_1_ot_whole_pic_table_0_5.jpg'
# IMAGE_PATH = '../oracle/result/甲骨文字編-李宗焜_cut_cor_1_ot_whole_pic_table_0_6.jpg'
# IMAGE_PATH = '../oracle/result/甲骨文字編-李宗焜_cut_cor_1_ot_whole_pic_table_0_7.jpg'
IMAGE_PATH = '../oracle/result/甲骨文字編-李宗焜_cut_cor_102_ot_whole_pic_table_0.jpg'

# reader = easyocr.Reader(['ch_tra', 'en'])
reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext(IMAGE_PATH, paragraph="False")
print(result)
boxes = []
for res in result:
    boxes.append(res[0])
    print(res[0])
print(boxes)
