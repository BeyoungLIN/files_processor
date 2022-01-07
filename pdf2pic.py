# -*- coding: utf-8 -*-
# @Time   : 2021/5/28 22:54
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : pdf2pic.py

import os
import time

import PyPDF4
import fitz
import pikepdf
from PIL import Image


# 对pdf文件进行简单的解密
def jiemi(pdfpath):
    new_pdfpath = pdfpath[:-4] + '_new' + pdfpath[-4:]

    fp = open(pdfpath, "rb+")
    pdfFile = PyPDF4.pdf.PdfFileReader(fp)

    # pdf 解密
    if pdfFile.isEncrypted:
        pdf = pikepdf.open(pdfpath, password='')
        pdf.save(new_pdfpath)
    return new_pdfpath


# 将每一页转化为图片并保存
def pdf_image(pdf_name, Gray=False):
    img_paths = []
    pdf = fitz.Document(pdf_name)
    for i, pg in enumerate(range(0, pdf.pageCount)):
        page = pdf[pg]  # 获得每一页的对象
        trans = fitz.Matrix(3.0, 3.0).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        # pm.writePNG(dir_name + os.sep + base_name[:-4] + '_' + '{:0>3d}.png'.format(pg + 1))  # 保存图片
        # if not os.path.exists(pdf_name[:-4]):
        #     os.makedirs(pdf_name[:-4])

        img_path = pdf_name[:-4] + '_' + str(pg + 1) + '.jpg'
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


def roots2pdf(root_list):
    for root in root_list:
        start_time = time.time()
        pdf_image(root, Gray=True)
        # sin_folders(root)
        end_time = time.time()
        used_time = end_time - start_time
        print(root + '\n处理时间', used_time)


def jpgs2pdf(ori_img_path, save_path):
    # img_path = 'D:/test'
    doc = fitz.open()

    # 循环path中的文件，可import os 然后用 for img in os.listdir(img_path)实现
    # 这里为了让文件以1，2，3的形式进行拼接，就偷懒循环文件名中的数字。
    for i in range(1, 99):
        img = 'img' + str(i) + '.jpg'
        img_file = ori_img_path + '/' + img
        imgdoc = fitz.open(img_file)
        pdfbytes = imgdoc.convertToPDF()
        pdf_name = str(i) + '.pdf'
        imgpdf = fitz.open(pdf_name, pdfbytes)
        doc.insertPDF(imgpdf)
    doc.save(save_path)
    doc.close()


# 另一个算法, 可能会小一点?
# ! /usr/local/bin/python3
# -*- coding: utf-8 -*-
def combine2Pdf(folderPath, pdfFilePath):
    files = os.listdir(folderPath)
    pngFiles = []
    sources = []
    for file in files:
        if 'png' in file:
            pngFiles.append(folderPath + file)
    pngFiles.sort()
    output = Image.open(pngFiles[0])
    pngFiles.pop(0)
    for file in pngFiles:
        pngFile = Image.open(file)
        if pngFile.mode == "RGB":
            pngFile = pngFile.convert("RGB")
        sources.append(pngFile)
    output.save(pdfFilePath, "pdf", save_all=True, append_images=sources)

if __name__ == '__main__':
    root_list = [
        # '/Users/Beyoung/Desktop/Projects/AC_OCR/國家圖書館藏敦煌遺書_001.pdf',
        # '/Users/Beyoung/Desktop/Projects/AC_OCR/2563[函368].pdf',
        # '/Users/Beyoung/Desktop/Projects/AC_OCR/纂図互註荀子3.pdf',
        # '/disks/sde/beyoung/files_processor/6059.桐南凤岗李氏宗谱：三十二卷：[桐庐]',
        '/Users/Beyoung/Desktop/Projects/corpus/（1-3）K877.5-2014-清华大学藏战国竹简（壹-叁）文字编-李学勤沈建华贾连翔.pdf'
    ]
    roots2pdf(root_list)


# if __name__ == "__main__":
#     folder = "/Users/weiyang/Desktop/pngFiles/"
#     pdfFile = "/Users/weiyang/Desktop/contract.pdf"
#     combine2Pdf(folder, pdfFile)

# if __name__ == '__main__':
#     img_path = '/Users/Beyoung/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/287670ac417cbf6320066bb73d21dc16/Message/MessageTemp/a3b2a1373f6c459b14d2c5ae746f7cc1/File/thsis_image'
#     pdf_save_path = '/Users/Beyoung/Library/Mobile Documents/com~apple~CloudDocs/papers/组内毕业论文/**.pdf'
#     jpgs2pdf(img_path, pdf_save_path)
#