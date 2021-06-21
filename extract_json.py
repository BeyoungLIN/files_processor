# -*- coding: utf-8 -*-
# @Time   : 2021/6/22 00:35
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : extract_json.py

import re


def read_json_2txt(json, txt=None):
    with open(json, 'r') as json_file:
        content = json_file.read()

    pattern = re.compile(r'"text": "(.*)",\n')
    result = pattern.findall(content)

    if not txt:
        txt = json[:-9] + '.txt'
        # print(txt)
    content_txt = []

    for line in result:
        line_new = line + '\n'
        content_txt.append(line_new)

    with open(txt, 'w') as txt_file:
        txt_file.writelines(content_txt)


if __name__ == '__main__':
    read_json_2txt('/Users/Beyoung/Desktop/Projects/AC_OCR/temp/史记1_resapi_mix.json.txt')
