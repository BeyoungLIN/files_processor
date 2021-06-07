# -*- coding: utf-8 -*-
# @Time   : 2021/5/31 09:16
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : if_jinling_yi.py

ip_path = '/Volumes/ExtremeSSD/金陵诗徵/金陵诗徵44巻_gray_rec_washed/金陵诗徵44巻_2_res_recog.txt'
with open(ip_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, len(line))
        if line.startswith('一'):
            print('start with yi')
        elif line.startswith('二'):
            print('start with er')
        elif line.startswith('也'):
            print('start with ye')
