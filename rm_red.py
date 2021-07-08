# -*- coding: utf-8 -*-
# @Time   : 2021/7/6 15:19
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : rm_red.py

# -*- encoding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image


class SealRemove(object):
    """
    印章处理类
    """

    def remove_red_seal(self, image):
        """
        去除红色印章
        """

        # 获得红色通道
        blue_c, green_c, red_c = cv2.split(image)

        # 多传入一个参数cv2.THRESH_OTSU，并且把阈值thresh设为0，算法会找到最优阈值
        thresh, ret = cv2.threshold(red_c, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 实测调整为95%效果好一些
        filter_condition = int(thresh * 0.95)

        _, red_thresh = cv2.threshold(red_c, filter_condition, 255, cv2.THRESH_BINARY)

        # 把图片转回 3 通道
        result_img = np.expand_dims(red_thresh, axis=2)
        result_img = np.concatenate((result_img, result_img, result_img), axis=-1)

        return result_img

def convert_gray(img_path):
    # print(pdf_name[:-4], pdf_name[:-4] + '_' + str(pg + 1) + '.jpg')
    # if Gray:  # 是否转为灰度
    img = Image.open(img_path)
    # img.show()
    low = img.convert('L')
    low.save(img_path[:-4] + "_gray.png")

    '''
    这种模式转换的灰度图片size比较大
    img = cv2.imread(img_path, 0)
    # cv2.imshow("img", img)
    cv2.imwrite(img_path, img)
        '''
    return

if __name__ == '__main__':
    # image = '/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2021.6.29/入注附音司马温公资治通鉴（有眉批、透字、旁批、点号）/ZHSY000116-000009.tif'
    # img = cv2.imread(image)
    # seal_rm = SealRemove()
    # rm_img = seal_rm.remove_red_seal(img)
    # cv2.imwrite(image[:-4] + "_rm_red.png", rm_img)
    convert_gray('/Users/Beyoung/Desktop/Projects/AC_OCR/OCR测试图像2021.6.29/入注附音司马温公资治通鉴（有眉批、透字、旁批、点号）/ZHSY000116-000009.tif')
