# -*- coding: utf-8 -*-
# @Time   : 2022/4/26 23:21
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : video2danmu2pdf_pinepline.py

from burn_video_with_danmu import get_batch_ls, run_ass_combine
from combinepics2pdf import get_pic_pth_ls, divi_pic, pic_compose, creat_pdf
import os

if __name__ == '__main__':
    # root = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂_screenshot_30'
    # root = 'Unity2018教程2D入门 01安装软件&导入素材_screenshot_30/'
    root = 'Unity2018教程2D入门_screenshot_30'
    pic_ls = os.listdir(root)
    # pic_ls.sort(key=lambda arr: (arr[:2], int(arr[2:])))
    pic_ls.sort(key=lambda arr: (int(arr.split('-')[0]), int(arr.split('_')[-1][:-4])))
    # print(pic_ls)
    row = 2
    line = 2

    pic_ls = get_pic_pth_ls(root, pic_ls)
    print('divd pic')
    page_list = divi_pic(pic_ls, row, line)
    print('pic_compose')
    pdf_folder = pic_compose(page_list, root)
    # pdf_folder = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂_screenshot_30_combine'
    # pdf_folder = 'Unity2018教程2D入门 01安装软件&导入素材_screenshot_30/'
    # pdf_pic_ls = get_pdf_pic_ls(pdf_folder)
    pdf1_filename = 'u2课件_fps30_4page_0_8.pdf'
    print('creat pdf')
    creat_pdf(pdf_folder, pdf1_filename)