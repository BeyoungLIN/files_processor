# -*- coding: utf-8 -*-
# @Time   : 2022/3/16 17:29
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : screenshot_web2.py

import os

import shutil

from selenium import webdriver

import time

import random

try:

    driver = webdriver.Chrome(r"/Users/Beyoung/Downloads/chromedriver 2")  ## 自己现在并放到指定目录，需要自己修改

    picture_url = "https://www.runoob.com/cplusplus/cpp-polymorphism.html"

    driver.get(picture_url)

    driver.maximize_window()

    print(dir(driver))

    time.sleep(1)

    driver.get_screenshot_as_file('./web.png')

    print("%s：截图成功！！！" % picture_url)

    driver.close()

except BaseException as msg:
    print(msg)
