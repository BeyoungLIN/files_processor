# -*- coding: utf-8 -*-
# @Time   : 2022/4/16 01:43
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : mini_test.py

from lxml import etree
import requests

from Levenshtein import ratio as ED
# def get_resource_html(url):
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
#     }
#     res = requests.get(url, headers=headers).text
#     res.encode('utf-8')
#     return res
#
#
# def parse_html_douban(html):
#     et = etree.HTML(html)
#     movie_list = et.xpath('//ol[@class="grid_view"]/li')
#     for movie in movie_list:
#         movie_ranking = movie.xpath('.//div[@class="pic"]/em/text()')[0]
#         movie_title = movie.xpath('.//div[@class="info"]//span[1]/text()')[0]
#         with open('movie.csv', 'a+', encoding='utf-8') as fw:
#             fw.write(f"{movie_ranking},{movie_title}\n")
#     return
#
# def main():
#     url = "https://movie.douban.com/top250"
#     html = get_resource_html(url)
#     parse_html(html)
#
# if __name__ == '__main__':
#     main()

# with open('/Users/Beyoung/Desktop/Projects/corpus/cuhk2022/res/ocr-result542.txt') as f1:
with open('/Users/Beyoung/Desktop/Projects/corpus/cuhk2022/res/ocr-result (1).txt') as f1:
    c1 = f1.read()

with open('/Users/Beyoung/Desktop/Projects/corpus/cuhk2022/Testing materials/txt/output.txt') as f2:
    c2 = f2.read()

# core = ED(c1, c2)
print(ED(c1, c2))