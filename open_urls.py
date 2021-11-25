# -*- coding: utf-8 -*-
# @Time   : 2021/11/15 11:22
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : open_urls.py

import webbrowser
import codecs
import time


with open("urls.txt") as fp:
    urls = fp.readlines()
for url in urls[0:20]:
    url = url.replace('\n', '')
    time.sleep(5) #打开间隔时间
    webbrowser.open(url) #打开网页
    # print(urls)