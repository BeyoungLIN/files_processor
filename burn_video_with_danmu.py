# -*- coding: utf-8 -*-
# @Time   : 2022/4/26 21:09
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : burn_video_with_danmu.py
import os

import tqdm


def add_srt():
    return


def run_ass_combine(video_pth, ass_pth, op_pth):
    video_pth = video_pth.replace(' ', '\\ ').replace('&', '\\&')
    ass_pth = ass_pth.replace(' ', '\\ ').replace('&', '\\&')
    op_pth = op_pth.replace(' ', '\\ ').replace('&', '\\&')
    # com = f'ffmpeg -i 6-06.动画效果Anima-1080P\ 高清-AVC.mp4 -vf ass=../Unity2018教程2D入门\ 01安装软件\&导入素材_new/6-06.动画效果Anima-1080P\ 高清-AVC.ass -vcodec libx265 -acodec copy ./6-06.动画效果Anima-1080P\ 高清-AVC_2带弹幕.mp4'
    com = f'ffmpeg -i {video_pth} -vf ass={ass_pth} -vcodec libx265 -acodec copy {op_pth}'
    print(com)
    # os.system('conda deactivate')
    os.system(com)
    return


def get_batch_ls(video_root):
    video_ls = []
    files = os.listdir(video_root)
    for file in files:
        if file.endswith('.mp4') and not file.endswith('带字幕.mp4'):
            video_ls.append(file)
    return video_ls


def get_paths(name):
    # video_pth = 'Unity2018教程2D入门 01安装软件&导入素材/3-03.图层layer&角-1080P 高清-AVC_2带字幕.mp4'
    # ass_pth = 'Unity2018教程2D入门_final/danmu/3-03.图层layer&角-1080P 高清-AVC_make.ass'
    # op_pth = 'Unity2018教程2D入门_final/combine_video/3-03.图层layer&角-1080P 高清-AVC_带弹幕.mp4'
    # video_pth = os.path.join('Unity2018教程2D入门 01安装软件&导入素材/', name)
    # ass_pth = 'Unity2018教程2D入门_final/danmu/3-03.图层layer&角-1080P 高清-AVC_make.ass'
    # op_pth = 'Unity2018教程2D入门_final/combine_video/3-03.图层layer&角-1080P 高清-AVC_带弹幕.mp4'
    # name = 1-01.安装软件&导入素材-1080P 高清-AVC.mp4
    video_pth = os.path.join('Unity2018教程2D入门 01安装软件&导入素材/', name)
    ass_pth = os.path.join('Unity2018教程2D入门_final/danmu/', name[:-4] + '_make.ass')
    op_pth = os.path.join('Unity2018教程2D入门_final/combine_video/', name[:-4] + '_带弹幕.mp4')
    return video_pth, ass_pth, op_pth


def sort_method(ori_ls):
    # new_ls = []
    # ori_ls.sort(key=lambda arr: (int(arr.split('_')[-1][:-4])))
    ori_ls.sort(key=lambda arr: (int(arr.split('-')[0])))
    return ori_ls


if __name__ == '__main__':
    # for
    video_root = 'Unity2018教程2D入门 01安装软件&导入素材/'
    video_ls = get_batch_ls(video_root)
    video_ls = sort_method(video_ls)

    for i in tqdm.tqdm(video_ls[:10]):
        print(i)
        video_pth, ass_pth, op_pth = get_paths(i)
        run_ass_combine(video_pth, ass_pth, op_pth)
    # video_pth = 'Unity2018教程2D入门 01安装软件&导入素材/3-03.图层layer&角-1080P 高清-AVC_2带字幕.mp4'
    # ass_pth = 'Unity2018教程2D入门_final/danmu/3-03.图层layer&角-1080P 高清-AVC_make.ass'
    # op_pth = 'Unity2018教程2D入门_final/combine_video/3-03.图层layer&角-1080P 高清-AVC_带弹幕.mp4'
    # run_ass_combine(video_pth, ass_pth, op_pth)
    # add_srt()
