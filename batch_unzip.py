# -*- coding: utf-8 -*-
# @Time   : 2022/4/12 13:55
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : cut_video.py

import os
import cv2
import argparse


def batch_unzip(ip_path, op_path):
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

    for filename in os.listdir(ip_path):
        if filename.endswith('.tip'):
            print(ip_path + filename)
            zip_pth = os.path.join(ip_path, filename)
            os.system(f'unzip {zip_pth} -d {op_path}')


def batch_cp(ip_path, op_path):
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

    for curDir, dirs, files in os.walk(ip_path):
        for file in files:
            if file.endswith(".tif"):
                zip_pth = os.path.join(curDir, file)
                print(os.path.join(curDir, file))
                # print(ip_path + filename)
                os.system(f'cp {zip_pth} {op_path}')

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
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--ip_path", type=str, help="原路径")
    # parser.add_argument("--op_path", type=str, help="压缩后输出路径")
    # parser.add_argument("--resize_ratio", type=int, default=0.2, help="压缩比例")
    # args = parser.parse_args()
    ip_path = '/disks/sdb/euphoria/Shuju_AnCn'
    op_path = '/disks/sdb/euphoria/Shuju_AnCn_total'
    # batch_unzip(args.ip_path, args.op_path)
    batch_cp(ip_path, op_path)

