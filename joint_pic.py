# -*- coding: utf-8 -*-
# @Time   : 2021/4/11 21:01
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : joint_pic.py

import os

from PIL import Image


def joint_vertical(ims_list, res_name):  # 传递一个ims列表和保存名
    # 获取当前文件夹中所有JPG图像
    # im_list = [Image.open(fn) for fn in listdir() if fn.endswith('.jpg')]
    ims = [Image.open(img) for img in ims_list]

    # 图片转化为相同的尺寸
    # height1 =

    # ims = []
    # for i in im_list:
    #     new_img = i.resize((1480, 990), Image.BILINEAR)
    # ims.append(new_img)

    # 单幅图像尺寸
    width, height = ims[0].size

    # 创建空白长图
    new_img = Image.new(ims[0].mode, (width, height * len(ims)))
    '''
    todolist:
    1. 对于不同尺寸的图片进行兼容
    2. 对图片数量进行兼容
    '''

    # 拼接图片
    for i, im in enumerate(ims):
        new_img.paste(im, box=(0, i * height))

        # 保存图片
        new_img.save(res_name)


if __name__ == '__main__':
    # imgs = []
    # pic1 = '/Users/Beyoung/Desktop/Projects/DB/Dingxiu_1_demo_results_res18的副本/000001_db.jpg'
    # pic2 = '/Users/Beyoung/Desktop/Projects/DB/Dingxiu_1_demo_results_res18的副本/000001.jpg'

    for id_num in range(636, 637):
        imgs = []
        img_name = str(id_num).zfill(6)
        folder_path1 = '/Users/Beyoung/Desktop/Projects/DB/Dingxiu_2_demo_results_res18'
        folder_path2 = '/Users/Beyoung/Desktop/Projects/DB/Dingxiu_2_demo_results_newdb'
        pic1 = os.path.join(folder_path1, img_name + '.jpg')
        pic2 = os.path.join(folder_path2, img_name + '.jpg')

        imgs.append(pic1)
        imgs.append(pic2)
        res_path = '/Users/Beyoung/Desktop/Projects/DB/joint/Dingxiu2/'
        joint_vertical(imgs, os.path.join(res_path, img_name + '_joint.jpg'))

