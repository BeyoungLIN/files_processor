# -*- coding: utf-8 -*-
# @Time   : 2022/1/6 23:15
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : pdf_cut.py

from PyPDF2 import PdfFileWriter, PdfFileReader


def cut_pdf(ip_pdf_pth, op_pdf_pth, start_page, end_page):
    # 开始页
    # start_page = 0

    # 截止页
    # end_page = 5

    output = PdfFileWriter()
    pdf_file = PdfFileReader(open("input.pdf", "rb"))
    pdf_pages_len = pdf_file.getNumPages()

    # 保存input.pdf中的1-5页到output.pdf
    for i in range(start_page, end_page + 1):
        output.addPage(pdf_file.getPage(i))

    outputStream = open("output.pdf", "wb")
    output.write(outputStream)

if __name__ == '__main__':
    cut_pdf('/Users/Beyoung/Desktop/Projects/corpus/（1-3）K877.5-2014-清华大学藏战国竹简（壹-叁）文字编-李学勤沈建华贾连翔.pdf', )
