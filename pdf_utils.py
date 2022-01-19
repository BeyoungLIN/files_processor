# -*- coding: utf-8 -*-
# @Time   : 2022/1/6 23:15
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : pdf_cut.py

from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import time

import PyPDF4
import fitz
import pikepdf
from PIL import Image


# 将每一页转化为图片并保存
def pdf_image(pdf_name, Gray=True):
    img_paths = []
    pdf = fitz.Document(pdf_name)
    for i, pg in enumerate(range(0, pdf.pageCount)):
        page = pdf[pg]  # 获得每一页的对象
        trans = fitz.Matrix(3.0, 3.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        # pm.writePNG(dir_name + os.sep + base_name[:-4] + '_' + '{:0>3d}.png'.format(pg + 1))  # 保存图片
        # if not os.path.exists(pdf_name[:-4]):
        #     os.makedirs(pdf_name[:-4])

        img_folder_name = pdf_name.split('/')[-1][:-4]
        # print(os.path.dirname(pdf_name), img_folder_name)
        img_folder_pth = os.path.join(os.path.dirname(pdf_name), img_folder_name)
        if not os.path.exists(img_folder_pth):
            os.mkdir(img_folder_pth)
        print(img_folder_pth)
        # img_path = os.path.join(img_folder_pth, pdf_name[:-4] + '_' + str(pg + 1) + '.jpg')
        img_path = img_folder_pth + '/' + pdf_name.split('/')[-1][:-4] + '_' + str(pg + 1) + '.jpg'
        print(img_path)
        # print(pdf_name[:-4], pdf_name[:-4] + '_' + str(pg + 1) + '.jpg')
        pm.writePNG(img_path)  # 保存图片
        img_paths.append(img_path)

        if Gray:  # 是否转为灰度
            img = Image.open(img_path)
            # img.show()
            low = img.convert('L')
            low.save(img_path)

            '''
            这种模式转换的灰度图片size比较大
            img = cv2.imread(img_path, 0)
            # cv2.imshow("img", img)
            cv2.imwrite(img_path, img)
            '''
    pdf.close()
    return img_paths


def cut_pdf(start_page, end_page, ip_pdf_pth, op_pdf_pth=''):
    # 开始页
    # start_page = 0

    # 截止页
    # end_page = 5
    if op_pdf_pth == '':
        op_pdf_pth = ip_pdf_pth[:-4] + '_cut.pdf'
    output = PdfFileWriter()
    pdf_file = PdfFileReader(open(ip_pdf_pth, "rb"))
    pdf_pages_len = pdf_file.getNumPages()

    # 保存input.pdf中的1-5页到output.pdf
    for i in range(start_page - 1, end_page):
        output.addPage(pdf_file.getPage(i))

    outputStream = open(op_pdf_pth, "wb")
    output.write(outputStream)


def cut_pdf_img(sp, ep, ipdf_pth, opdf_pth=''):

    if opdf_pth == '':
        opdf_pth = ipdf_pth[:-4] + '_cut.pdf'
    cut_pdf(sp, ep, ipdf_pth, opdf_pth)
    pdf_image(opdf_pth, Gray=True)


if __name__ == '__main__':
    # cut_pdf(8, 370, '/Users/Beyoung/Desktop/Projects/corpus/（1-3）K877.5-2014-清华大学藏战国竹简（壹-叁）文字编-李学勤沈建华贾连翔.pdf')
    # cut_pdf_img(7, 376, '/Users/Beyoung/Desktop/Projects/corpus/（1-3）K877.5-2014-清华大学藏战国竹简（壹-叁）文字编-李学勤沈建华贾连翔.pdf')  # 1-3 √
    # cut_pdf_img(9, 355, '/Users/Beyoung/Desktop/Projects/corpus/（4-6）K877.5-2017-清华大学藏战国竹简（肆-陆）文字编-李学勤贾连翔沈建华.pdf')  # 4-6 √
    # cut_pdf_img(164, 229, '/Users/Beyoung/Desktop/Projects/corpus/（7）K877.5-2017-清华大学藏战国竹简7-清华大学出土文献研究与保护中心.pdf')  # 7  148-156 差8页 √
    cut_pdf_img(190, 274, '/Users/Beyoung/Desktop/Projects/corpus/（9）K877.5-2019-清华大学藏战国竹简9-清华大学出土文献研究与保护中心.pdf')  # 9
    # cut_pdf_img(140, 218, '/Users/Beyoung/Desktop/Projects/corpus/清华十.pdf')  # 10
