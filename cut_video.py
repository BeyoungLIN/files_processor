# -*- coding: utf-8 -*-
# @Time   : 2022/4/12 13:55
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : cut_video.py

import os
import cv2
import argparse

import tqdm


def batch_cut(ip_path, op_path, resize_ratio=0.2):
    """
    本函数可以将ip_path下所有tif结尾图片的长宽缩成原本的0.2, 并保存在op_path中
    :param ip_path:
    :param op_path:
    :param resize_ratio:
    :return:
    """
    #批量缩放
    # resize_ratio = 0.2
    if not os.path.exists(op_path):
        os.makedirs(op_path)

    for filename in tqdm.tqdm(os.listdir(ip_path)):
        if filename.endswith('_带弹幕.mp4'):
        # if filename.endswith('14-14 Patrol Randomly 随机巡逻点-1080P 高清-AVC.mp4'):
            name = filename[:-4]
            video_pth = os.path.join(ip_path, filename)
            print(video_pth)
            vc = cv2.VideoCapture(video_pth)  # 读取视频文件，修改为自己的文件名
            c = 0
            print("------------")
            if vc.isOpened():
                # print("yes")
                rval, frame = vc.read()
            else:
                rval = False
                print("false")

            timeF = 30  # 视频帧计数间隔

            while rval:  # 循环读取视频
                rval, frame = vc.read()
                # print(c, timeF, c % timeF)
                if (c % timeF == 0):
                    # print("write...")
                    # cv2.imwrite(f"{op_path}photo_{}.jpg".format(c), frame)  # 修改为自己的文件夹
                    cv2.imwrite(os.path.join(op_path, f"{name}_{c}.jpg"), frame)  # 修改为自己的文件夹
                    # print("success!")
                c = c + 1
            cv2.waitKey(1)
            vc.release()
            print("==================================")


def batch_rename(path):
    # 批量重命名
    for filename in os.listdir(path):
        im = cv2.imread(filename)
        name = filename.split('.')
        # print(name[1])
        if name[1] == "tif":
            os.rename(os.path.join(path, filename), os.path.join(path, name[0] + '.tif'))


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip_path", type=str, help="原路径")
    parser.add_argument("--op_path", type=str, help="压缩后输出路径")
    parser.add_argument("--resize_ratio", type= int, default=0.2, help="压缩比例")
    args = parser.parse_args()
    args.ip_path = 'Unity2018教程2D入门_final/combine_video'
    args.op_path = 'Unity2018教程2D入门_带弹幕_screenshot'
    batch_cut(args.ip_path, args.op_path, args.resize_ratio)

