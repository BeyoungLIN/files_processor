# -*- coding: utf-8 -*-
# @Time   : 2023/6/7 23:52
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : pdf2pic2.py

import fitz

import datetime
import os


# fitz就是pip install PyMuPDF


def pyMuPDF_fitz(pdfPath, imagePath):
    if imagePath == '':
        imagePath = pdfPath.replace('.pdf', '')
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    print("imagePath=" + imagePath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        # zoom_x = 4  # (1.33333333-->1056x816)   (2-->1584x1224)
        # zoom_y = 4
        # mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        # rect = page.rect
        # clip = fitz.Rect(rect.tl + 15, rect.br - 13)
        # pix = page.getPixmap(matrix=mat, alpha=False, clip=clip)
        pix = page.getPixmap()

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.writePNG(imagePath + '/' + 'images_%s.jpg' % pg)  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


if __name__ == "__main__":
    # 1、PDF地址
    # pdfPath = r"D:\图纸识别\中核\设计院CAM系统设计输入\设计院-FD图--1418YCAMYKS62-D.pdf"
    pdfPath = r"/Users/Beyoung/Downloads/转pdf/4.9 庾信.pdf"
    # 2、需要储存图片的目录
    # imagePath = r"/Users/Beyoung/Downloads/4.9 庾信.pdf"
    pyMuPDF_fitz(pdfPath, imagePath='')

