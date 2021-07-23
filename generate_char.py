# -*- coding: utf-8 -*-
# @Time   : 2021/7/18 11:14
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : generate_char.py

from PIL import Image, ImageFont, ImageDraw
from fontTools.ttLib import TTFont


def processGlyphNames(GlyphNames):
    res = set()
    for char in GlyphNames:
        if char.startswith('uni'):
            char = char[3:]
        elif char.startswith('u'):
            char = char[1:]
        else:
            continue
        if char:
            try:
                char_int = int(char, base=16)
            except ValueError:
                continue
            try:
                char = chr(char_int)
            except ValueError:
                continue
            res.add(char)
    return res


def generation_single_char(char, ttf):
    image = Image.new('RGB', (128, 128), (255, 255, 255))  # 设置画布大小及背景色
    iwidth, iheight = image.size  # 获取画布高宽
    font = ImageFont.truetype(ttf, 128)  # 设置字体及字号
    draw = ImageDraw.Draw(image)

    fwidth, fheight = draw.textsize(char, font)  # 获取文字高宽

    fontx = (iwidth - fwidth - font.getoffset(char)[0]) / 2
    fonty = (iheight - fheight - font.getoffset(char)[1]) / 2

    draw.text((fontx, fonty), char, 'black', font)
    # image.show()
    image.save('/Users/Beyoung/Desktop/Projects/ER/dataset/chars_set/' + char + '.jpg')  # 保存图片


if __name__ == '__main__':
    ttf_path = '/Users/Beyoung/Desktop/Projects/ER/dataset/ER007/方正楷体/FZKaiS-Extended.TTF'
    # ttf_path = 'charset/ZhongHuaSong/FZSONG_ZhongHuaSongPlane00_2020051520200519101119.TTF'
    fontPlane00 = TTFont(ttf_path)
    # fontPlane00 = TTFont(os.path.join(src_fonts_dir, 'FZSONG_ZhongHuaSongPlane00_2020051520200519101119.TTF'))
    # fontPlane02 = TTFont(os.path.join(src_fonts_dir, 'FZSONG_ZhongHuaSongPlane02_2020051520200519101142.TTF'))

    charSetPlane00 = processGlyphNames(fontPlane00.getGlyphNames())
    # print(charSetPlane00)
    for ch in charSetPlane00:
    # char = '爱'
        generation_single_char(ch, ttf_path)
