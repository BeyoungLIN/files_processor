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
    # if RESIZE == 1:
    #
    #     height1 =
    #
    #     ims = []
    #     for i in im_list:
    #         new_img = i.resize((1480, 990), Image.BILINEAR)
    #     ims.append(new_img)

    # 单幅图像尺寸
    width, height = ims[0].size

    # 创建空白长图
    new_img = Image.new(ims[0].mode, (width, height * len(ims)))
    '''
    todolist:
    1. 对于不同尺寸的图片进行兼容,选择是否统一格式 if resize = 1
    '''

    # 拼接图片
    for i, im in enumerate(ims):
        new_img.paste(im, box=(0, i * height))

        # 保存图片
        new_img.save(res_name)


if __name__ == '__main__':

    folders_list = [
        '../AC_OCR/models_test/single_test/res18_2.0',
        '../AC_OCR/models_test/single_test/res50_2.0',
        '../AC_OCR/models_test/single_test/res50_3.5',
    ]

    files = os.listdir(folders_list[0])

    for file in files:
        if file.endswith('.jpg'):
            try:
                imgs = []
                # img_name = str(id_num).zfill(6)
                # '''

                for folder in folders_list:
                    pic_name = os.path.join(folder, file)
                    imgs.append(pic_name)
                '''
                folder_path1 = '../AC_OCR/Dingxiu_test/Dingxiu_2/Dingxiu_2_demo_results_res50'
                pic1 = os.path.join(folder_path1, img_name + '.jpg')
                imgs.append(pic1)
                
                folder_path2 = '../AC_OCR/Dingxiu_test/Dingxiu_2/Dingxiu_2_demo_results_newdb'
                pic2 = os.path.join(folder_path2, img_name + '.jpg')
                imgs.append(pic2)
                '''

                res_path = '../AC_OCR/joint_compare/Dingxiu_2/total_res502.0_res503.5_singlePic'
                if not os.path.exists(res_path):
                    os.mkdir(res_path)
                joint_vertical(imgs, os.path.join(res_path, file[:-4] + '_joint.jpg'))

            except:
                print(file)
