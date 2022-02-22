# -*- coding: utf-8 -*-
# @Time   : 2022/1/21 20:56
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : read_json.py


import datetime
import json
import os
import time
from datetime import timedelta
import pprint


def read_json(jsonPath):
    jsonfile = open(jsonPath)
    json_list = json.load(jsonfile)
    # print(json_list[0])
    # print(type(json_list))
    
    return json_list

def show_json(jsonPath, show_none=0):
    jsonfile = open(jsonPath)
    json_list = json.load(jsonfile)
    # json_list = json_list.sort()
    # json_list = sorted(json_list)
    # print(len(json_list))
    print(len(json_list))
    
    return 

json_pth = '/Users/Beyoung/Desktop/Projects/comms/120/网易游戏雷火校园招聘_复制.json'
json_list = read_json(json_pth)[:30]
# print(len(json_list))
# json_list.sort()
# json_list = show_json(json_pth)
pprint.pprint(json_list)