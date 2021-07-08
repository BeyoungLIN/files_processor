# -*- coding: utf-8 -*-
# @Time   : 2021/6/24 14:29
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : text_diff_1.py

import difflib


def diff(fn1, fn2):
    """对比两个文件内容的不同并以html的格式返回"""
    with open(fn1) as f1: content1 = f1.readlines()
    with open(fn2) as f2: content2 = f2.readlines()
    df = difflib.HtmlDiff()
    return df.make_file(content1, content2)


if __name__ == '__main__':
    fn1 = '/Users/Beyoung/Desktop/Projects/AC_OCR/temp/ZHSY000116-000009_res_recog_adv.txt'
    fn2 = '/Users/Beyoung/Desktop/Projects/AC_OCR/temp/ZHSY000116-000009_gray_res_recog_adv.txt'
    res = diff(fn1, fn2)
    with open (fn1[:-4] + '_diff_res_2.html', 'w') as f:
        f.write(res)
    print(res)
