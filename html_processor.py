# -*- coding: utf-8 -*-
# @Time   : 2021/5/13 00:03
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : html_processor.py

import re
import webbrowser

input_file = ''

with open(input_file, 'r') as f:
    lines = f.readlines()

# print(lines)
urls = []
pattern = re.compile(r'href="(.*?)"')
for line in lines:
    res = pattern.findall(line)
    for url in res:
        if url[0:22] == 'https://www.douban.com':
            urls.append(url)
urls = list(set(urls))
urls.sort()
print(len(urls))

for url_i in urls[220:283]:
    webbrowser.open(url_i, new=2, autoraise=True)
    print(url_i)
