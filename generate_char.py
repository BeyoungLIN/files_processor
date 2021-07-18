# -*- coding: utf-8 -*-
# @Time   : 2021/7/18 11:14
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : generate_char.py

from PIL import Image, ImageFont, ImageDraw

image = Image.new('RGB', (250, 250), (255, 255, 255))  # 设置画布大小及背景色
iwidth, iheight = image.size  # 获取画布高宽
font = ImageFont.truetype('consola.ttf', 110)  # 设置字体及字号
draw = ImageDraw.Draw(image)

fwidth, fheight = draw.textsize('22', font)  # 获取文字高宽

fontx = (iwidth - fwidth - font.getoffset('22')[0]) / 2
fonty = (iheight - fheight - font.getoffset('22')[1]) / 2

draw.text((fontx, fonty), '22', 'black', font)
image.save('1.jpg')  # 保存图片
