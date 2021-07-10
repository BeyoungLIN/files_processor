# -*- coding: utf-8 -*-
# @Time   : 2021/7/9 09:32
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : extract_html.py

import os
import re

from selectolax.parser import HTMLParser


def get_pure_text_selectolax(html):
    tree = HTMLParser(html)

    if tree.body is None:
        return None

    for tag in tree.css('script'):
        tag.decompose()
    for tag in tree.css('style'):
        tag.decompose()

    text = tree.body.text(separator='\n')
    print(text)
    return text


def get_content_re(content, type=None):
    # with open(html_path, 'r') as h:
    #     content = h.read()
    content = content.replace('slinespan', 'S')
    content = content.replace('linespan', 'L')

    # pat = r"<div class=('L'>.*?)</div>"
    # results = re.findall(pat, content)
    # print(results)

    pat = r"<div class=('[LS]'>.*?)<"
    results = re.findall(pat, content)
    for i in results:
        i = i.replace('\'', '')
        if (i != 'L>') and (i != 'L>&nbsp;'):
            print('<' + i)
            # print(i)


def find_slinespan_re(html_path, type=None):
    with open(html_path, 'r', encoding='ISO-8859-1') as h:
        content = h.read()
    # content = content.replace('slinespan', 'S')
    # content = content.replace('linespan', 'L')

    # pat = r"<div class=('L'>.*?)</div>"
    # results = re.findall(pat, content)
    # print(results)

    pat = r"<div class=('slinespan'>.*?)<"
    results = re.findall(pat, content)

    if len(results) > 100:
        # print(results)
        # print(html_path)
        if dir_path in books_dic:
            books_dic[dir_path] += 1
        else:
            books_dic[dir_path] = 1
        path = '/Users/Beyoung/Desktop/Projects/AC_OCR/temp/dingxiu_small_test'
        # os.system('cp ' + html_path[:-4] + 'png ' + path)
    # for i in results:
    #     i = i.replace('\'', '')
    #     if (i != 'L>') and (i !='L>&nbsp;'):
    #         print('<' + i)
    # print(i)


if __name__ == '__main__':
    IMG_EXT = {'.jpg', '.png', '.tif', '.tiff', '.bmp', '.gif'}
    # html_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/Dingxiu_old/0A0EE6A7278D4FA3B4F38193A8AE55B5/000001.html'
    # with open(html_path, 'r') as h:
    #     content = h.read()
    # get_pure_text_selectolax(content)

    # find_slinespan_re('/Users/Beyoung/Desktop/Projects/AC_OCR/Dingxiu_old/0A0EE6A7278D4FA3B4F38193A8AE55B5/000001.html')

    # 遍历查找小字多的页面
    # html_folder = '/Users/Beyoung/Desktop/Projects/AC_OCR/Dingxiu_old/'
    html_folder = '/disks/sdb/projs/AncientBooks/data/DingXiu'
    dirs = os.listdir(html_folder)
    books_dic = {}
    flag = 0
    # print(flag)
    if flag < 10:
        # print(flag)
        for dir in dirs:
            dir_path = os.path.join(html_folder, dir)
            flag += 1
            if os.path.isdir(dir_path):
                files = os.listdir(dir_path)
                # print(dir_path)
                for file in files:
                    # if os.path.splitext(file)[1].lower() in IMG_EXT:
                    if os.path.splitext(file)[1].lower() == '.html':
                        file_path = os.path.join(dir_path, file)
                        find_slinespan_re(file_path)
                        # print(flag)
    print(sorted(books_dic.items(), key=lambda kv: (kv[1], kv[0])))
    # print(books_dic)

    # with open(html_path, 'r') as h:
    #     content = h.read()
    # print(get_pure_text_selectolax(content))
    #
    # import requests
    # from bs4 import BeautifulSoup
    # import re
    # import os.path
    #
    # user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
    # headers = {'User-Agent': user_agent}
    #
    # session = requests.session()
    # page = session.get("http://www.xicidaili.com/nn/1", headers=headers)
    # soup = BeautifulSoup(page.text, 'lxml')  # 这里没有装lxml的话,把它去掉用默认的就好
    #
    # # 匹配带有class属性的tr标签
    # taglist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
    # for trtag in taglist:
    #     tdlist = trtag.find_all('td')  # 在每个tr标签下,查找所有的td标签
    #     print
    #     tdlist[1].string  # 这里提取IP值
    #     print
    #     tdlist[2].string  # 这里提取端口值
