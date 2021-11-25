# -*- coding: utf-8 -*-
# @Time   : 2021/6/24 14:29
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : text_diff_1.py

import difflib


def diff_get_html(txt1, txt2):
    """对比两个文件内容的不同并以html的格式返回"""
    with open(fn1, 'r', encoding='utf-8') as f1:
        content1 = f1.readlines()
    with open(fn2, 'r', encoding='utf-8') as f2:
        content2 = f2.readlines()
    df = difflib.HtmlDiff()
    return df.make_file(content1, content2)

def diff_get_bool(txt1, txt2):
    with open(txt1, 'r', encoding='utf-8') as f1:
        content1 = f1.readlines()
    with open(txt2, 'r', encoding='utf-8') as f2:
        content2 = f2.readlines()
    if content1 == content2:
        print('完全一致')
    else:
        max_line = max(len(content1), len(content2))
        for i in range(max_line):
            if content1[i] != content2[i]:
                print('第', i ,'行')
                print(content1[i])
                print(content2[i])
                print()
        # print('有不同')


if __name__ == '__main__':
    fn1 = '/Users/Beyoung/Desktop/Projects/corpus/语料1/gujin.txt'
    fn2 = '/Users/Beyoung/Desktop/Projects/corpus/cleaned/gujin.txt'
    # res = diff_get_html(fn1, fn2)
    # with open ('text_diff/' + fn1.split('/')[-1][:-4] + '_diff_res_2.html', 'w') as f:
    #     f.write(res)
    # print(res)
    diff_get_bool(fn1, fn2)
