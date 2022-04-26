# -*- coding: utf-8 -*-
# @Time   : 2022/4/24 20:07
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : combinepics2pdf.py
import os

import cv2
import numpy as np
import tqdm
from PIL import Image
# img1_path = r"C:\Users\user\Desktop\picture\old\07724.jpg"
# img2_path = r"C:\Users\user\Desktop\picture\new\07724.jpg"
# img3_path = r"C:\Users\user\Desktop\picture\old\07371.jpg"
# img4_path = r"C:\Users\user\Desktop\picture\new\07371.jpg"
# img5_path = r"C:\Users\user\Desktop\picture\old\01514.jpg"
# img6_path = r"C:\Users\user\Desktop\picture\new\01514.jpg"


# import fitz.fitz
# import os
#
#
# # 将pdf转换为图片
# def pdf_to_image(pdfPath, imagePath):
#     pdfDoc = fitz.open(pdfPath)
#     for pg in range(pdfDoc.pageCount):
#         page = pdfDoc[pg]
#         pix = page.getPixmap(alpha=False)  # 默认是720*x尺寸
#         if not os.path.exists(imagePath):
#             os.makedirs(imagePath)
#         pix.writePNG(imagePath + '/' + 'images_%s.jpg' % pg)  # 将图片写入指定的文件夹内

#
# # 将pdf转换为txt文字
# def pdf_to_text(pdfPath):
#     doc = fitz.open(pdfPath)
#     for page in doc:
#         text = page.getText()
#         print(text)
#
#
# # 将图片转为pdf
# def img_to_pdf(imgPath):
#     doc = fitz.open()
#     for path in imgPath:
#         img = fitz.open(path)  # 打开图片
#         pdfbytes = img.convertToPDF()  # 使用图片创建单页的 PDF
#         imgpdf = fitz.open("pdf", pdfbytes)
#         doc.insertPDF(imgpdf)
#     doc.save('D:\桌面\\实验.pdf')


# if __name__ == '__main__':
#     imgPaths = []
#     imgPath = "D:\桌面\\图片\\{}.jpg"
#     for i in range(1, 5):
#         imgPaths.append(imgPath.format(i))
#     img_to_pdf(imgPaths)


def get_pic_pth_ls(rootfolder, pic_ls):
    pic_pth_ls = []
    for pic_name in pic_ls:
        if pic_name.endswith('.jpg'):
            pic_pth_ls.append(os.path.join(rootfolder, pic_name))
    return pic_pth_ls


def divi_pic(pri_ls, row, line):
    # result = []
    # row = 2
    # line = 2
    # if len(pri_ls) !=
    if len(pri_ls) % (row * line) != 0:
        pad = row * line - (len(pri_ls) % (row * line))
        for _ in range(pad):
            pri_ls.append(pri_ls[-1])
    page_list = []
    for page in range(len(pri_ls) // (row * line)):
        row_ls = []
        for y in range(0, row):  # 控制行
            line_ls = []
            for x in range(0, line):  # 控制列
                line_ls.append(pri_ls.pop(0))
            row_ls.append(line_ls)
            # if x == 0:
        page_list.append(row_ls)
    # print(page_list)
    return page_list


def pic_compose(page_list, root):
    pdf_folder = root.split('/')[-1] + '_combine'
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
    # all_p = len(page_list)
    # page = 0
    for pn, p in enumerate(tqdm.tqdm((page_list[:]))):
        # page += 1
        # print(f'{page} / {all_p} {round(page / all_p, 2)}')
        # print(page_list[0][0])
        for rn, r in enumerate(p):
            for ln, l in enumerate(r):
                if ln == 0:
                    # print(l)
                    img = cv2.imread(l)
                    img = cv2.resize(img, (1680, 1050))
                    img_tmp = img
                    if pn == len(page_list) - 1 and rn != 0 and r[0] == p[rn - 1][-1]:

                        img = np.zeros(img.shape)

                        img[img == 0] = 255  # 0 -> 255
                else:
                    img = cv2.imread(l)
                    img = cv2.resize(img, (1680, 1050))
                    if pn == len(page_list) - 1 and r[ln] == r[ln - 1]:
                        img = np.zeros(img.shape)

                        img[img == 0] = 255  # 0 -> 255
                    img_tmp = np.vstack((img_tmp, img))
            if rn == 0:
                rimg_tmp = img_tmp
            else:
                rimg_tmp = np.hstack((rimg_tmp, img_tmp))
        name = f"{pdf_folder.split('/')[-1]}_{pn}"
        cv2.imwrite(f"{pdf_folder}/{name}.jpg", rimg_tmp)
    # img1 = cv2.imread(img1_path)
    # # print(np.shape(img1)) # 或者用img1.shape   (h,w,c)   (1080,1920,3)
    # img1 = cv2.resize(img1, (1920, 1080))
    # img2 = cv2.imread(img2_path)
    # img2 = cv2.resize(img2, (1920, 1080))
    # img3 = cv2.imread(img3_path)
    # img3 = cv2.resize(img3, (1920, 1080))  # resize(img,(w,h),interpolation=cv2.INTER_CUBIC)
    # img4 = cv2.imread(img4_path)
    # img4 = cv2.resize(img4, (1920, 1080))
    # img5 = cv2.imread(img5_path)
    # img5 = cv2.resize(img5, (1920, 1080))
    # img6 = cv2.imread(img6_path)
    # img6 = cv2.resize(img6, (1920, 1080))
    #
    # img_tmp1 = np.hstack((img1, img2))
    # print(np.shape(img_tmp1))
    # img_tmp2 = np.hstack((img3, img4))
    # print(np.shape(img_tmp2))
    # img_tmp3 = np.hstack((img5, img6))
    # print(np.shape(img_tmp3))
    # img_tmp4 = np.vstack((img_tmp1, img_tmp2))
    # img = np.vstack((img_tmp4, img_tmp3))
    # cv2.imwrite(r"C:\Users\user\Desktop\picture\stack.jpg", img)
    return pdf_folder


def get_pdf_pic_ls(pdf_folder):
    pdf_pic_pth_ls = []
    pdf_pic_ls = os.listdir(pdf_folder)
    # pdf_pic_ls = filter(lambda x: x.endswith('.jpg'), pdf_pic_ls_)   #将jpg文件读进来，可改为jng等格式
    pdf_pic_ls.sort(key=lambda arr: (int(arr.split('_')[-1][:-4])))
    for pic_name in pdf_pic_ls:
        if pic_name.endswith('.jpg'):
            pdf_pic_pth_ls.append(os.path.join(pdf_folder, pic_name))
    return pdf_pic_pth_ls


def creat_pdf(pdf_folder, pdf1_filename):
    pdf_pic_pth_ls = get_pdf_pic_ls(pdf_folder)
    # print(pdf_pic_pth_ls)
    list1 = []
    # pic_ls.sort(key=lambda arr: (int(arr.split('-')[0]), int(arr.split('_')[-1][:-4])))
    # for each_img_pth in tqdm.tqdm(pdf_pic_pth_ls[len(pdf_pic_pth_ls)//2:]):
    for each_img_pth in tqdm.tqdm(pdf_pic_pth_ls[:len(pdf_pic_pth_ls)//2]):
        # 得到完整的图片路径
        # each_img_full_path = os.path.join(pictures_src_path, each_img)
        # print(each_img_full_path)
        images = Image.open(each_img_pth)
        list1.append(images)
    im1 = list1[0]
    del list1[0]
    print(len(list1))
    im1.save(pdf1_filename, "PDF", save_all=True, append_images=list1)


if __name__ == '__main__':
    # root = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂_screenshot_30'
    # root = 'Unity2018教程2D入门 01安装软件&导入素材_screenshot_30'
    root = 'Unity2018教程2D入门_带弹幕_screenshot'
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
