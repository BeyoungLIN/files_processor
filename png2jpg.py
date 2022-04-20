# -*- coding: utf-8 -*-
# @Time   : 2022/4/20 00:24
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : png2jpg.py

from PIL import Image
import cv2 as cv
import os


def PNG_JPG(PngPath):
    img = cv.imread(PngPath, 0)
    w, h = img.shape[::-1]
    infile = PngPath
    outfile = os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    # img = img.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=100)
            os.remove(PngPath)
        else:
            img.convert('RGB').save(outfile, quality=100)
            os.remove(PngPath)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误", e)


if __name__ == '__main__':
    PNG_JPG(r"/Users/Beyoung/Downloads/lby.png")