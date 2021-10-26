# -*- coding: utf-8 -*-
# @Time   : 2021/8/5 18:50
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : pic_projection_2.py

'''
(两步一次性完成：水平投影完分割行,直接进行垂直分割单字符,保存单字符)
字符切割步骤：
    1.对图片进行水平投影，找到每一行的上界限和下界限，进行行切割
    2.对切割出来的每一行，进行垂直投影，找到每一个字符的左右边界，进行单个字符的切割
'''
import cv2
import numpy as np


def split(a):  # 获取各行起点和终点
    # b是a的非0元素的下标 组成的数组 (np格式),同时也是高度的值
    b = np.transpose(np.nonzero(a))
    # print(b,type(b))
    # print(a,b.tolist())

    star = []
    end = []
    star.append(int(b[0]))
    for i in range(len(b) - 1):
        cha_dic = int(b[i + 1]) - int(b[i])
        if cha_dic > 1:
            # print(cha_dic,int(b[i]),int(b[i+1]))
            end.append(int(b[i]))
            star.append(int(b[i + 1]))
    end.append(int(b[len(b) - 1]))
    # print(star) # [13, 50, 87, 124, 161]
    # print(end)  # [36, 73, 110, 147,184]
    return star, end


def get_horizontal_shadow(img, img_bi):  # 水平投影+分割
    # 1.水平投影
    h, w = img_bi.shape
    shadow_h = img_bi.copy()  # shadow_h画图用(切记！copy后面还有个())

    a = [0 for z in range(0, h)]  # 初始化一个长度为h的数组，用于记录每一行的黑点个数

    for j in range(0, h):  # 遍历一行
        for i in range(0, w):  # 遍历一列
            if shadow_h[j, i] == 0:  # 发现黑色
                a[j] += 1  # a数组这一行的值+1
                shadow_h[j, i] = 255  # 记录好了就变为白色

    for j in range(0, h):  # 遍历一行 画黑条,长度为a[j]
        for i in range(0, a[j]):
            shadow_h[j, i] = 0

    return a


def get_vertical_shadow(img, img_bi):  # 垂直投影+分割
    # 1.垂直投影
    h, w = img_bi.shape
    shadow_v = img_bi.copy()
    a = [0 for z in range(0, w)]
    # print(a) #a = [0,0,0,0,0,0,0,0,0,0,...,0,0]初始化一个长度为w的数组，用于记录每一列的黑点个数

    print('h = ', h)
    print('w = ', w)
    # 记录每一列的波峰
    for j in range(0, w):  # 遍历一列
        for i in range(0, h):  # 遍历一行
            if shadow_v[i, j] == 0:  # 如果该点为黑点(默认白底黑字)
                a[j] += 1  # 该列的计数器加一计数
                shadow_v[i, j] = 255  # 记录完后将其变为白色
                # print (j)
    for j in range(0, w):  # 遍历每一列
        for i in range((h - a[j]), h):  # 从该列应该变黑的最顶部的点开始向最底部涂黑
            shadow_v[i, j] = 0  # 涂黑

    return a


def character_cut(img, img_bi):  # 字符切割
    # 1.水平投影
    ha = get_horizontal_shadow(img, img_bi)  # 水平投影
    # 2.开始分割
    # step2.1: 获取各行起点和终点
    h_star, h_end = split(ha)
    # step2.2: 切割行[y:y+h, x:x+w]
    for i in range(len(h_star)):  # 就是几行 5  [0 1 2 3 4]
        hs, he = h_star[i], h_end[i]
        img_line = img[hs:he, 0:img.shape[1]]

        # step2.3: 垂直投影
        img_line_gray = cv2.cvtColor(img_line, cv2.COLOR_BGR2GRAY)
        thresh1, img_line_bi = cv2.threshold(img_line_gray, 130, 255, cv2.THRESH_BINARY)
        # cv2.imshow('img_line', img_line)
        # cv2.imshow('img_line_gray', img_line_gray)
        # cv2.imshow('img_line_bi', img_line_bi)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        va = get_vertical_shadow(img_line, img_line_bi)

        # step2.4: 获取各列起点和终点
        v_star, v_end = split(va)
        # step2.5: 切割字符[y:y+h, x:x+w]
        for j in range(len(v_star)):  # 几列
            vs, ve = v_star[j], v_end[j]
            img_char = img_line[0:img_line.shape[0], vs:ve]  # [0:h, vs:ve]
            # step2.6: 保存字符
            save_name = './character/char_' + str(i) + '_' + str(j) + '.jpg'
            # cv2.imwrite(save_name, img_char)
            # cv2.imshow('word', img_char)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()



if __name__ == "__main__":
    # img = cv2.imread('E:\code\OCR\document_zn.png')
    img = cv2.imread('/Users/Beyoung/Desktop/Projects/ER/dataset/ER007/228_41142_jpg/000285.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh, img_bi = cv2.threshold(img_gray, 130, 255, cv2.THRESH_BINARY)

    character_cut(img, img_bi)  # 输入图片 和 二值图, 即可进行字符分割