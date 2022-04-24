# -*- coding: utf-8 -*-
# @Time   : 2022/4/22 14:26
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : creat_md.py
import os

root = '/Users/Beyoung/Movies/Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂_screenshot/'
files = os.listdir(root)
pic_ls = []
for file in files:
    if not file.endswith('.jpg'):
        continue
    pic_pth = os.path.join(root, file)
    pic_ls.append(pic_pth)

video_name = ''
content = ''
for pic_pth in pic_ls:
    video_tmp = pic_pth.split('_')[0]
    if video_name != video_tmp:
        pass


