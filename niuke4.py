# -*- coding: utf-8 -*-
# @Time   : 2022/6/16 19:43
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : niuke4.py
import time

import requests
import json
import os
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

symbol_list = ["\\", "/", "<", ":", "*", "?", "<", ">", "|", "\"", "&amp;"]


def replaceTitle(title):
    for i in symbol_list:
        if title.find(str(i)) != -1:
            title = title.replace(str(i), " ")

    return title


def getDetail_Url(tmp_path, json_str):
    discussPosts = json_str['data']['discussPosts']
    for discussPost in discussPosts:
        title = discussPost['postTitle']
        detail_url = "https://www.nowcoder.com/discuss/" + str(discussPost['postId'])
        detail_response = requests.get(url=detail_url, headers=headers)
        getDetailData(tmp_path, title, detail_response)


def getDetailData(tmp_path, title, detail_response):
    detailData = BeautifulSoup(detail_response.text, "html.parser")
    div_data = detailData.find(class_="post-topic-main").find_all("div")
    title = replaceTitle(title)
    print("正在保存" + tmp_path + ":" + title)
    with open(tmp_path + "/" + title + ".txt", 'w', encoding='utf-8') as f:
        for i in div_data:
            try:
                if i['class'].count('clearfix') != 0:
                    break
            except:
                pass
            tmp_text = i.text.strip('\n').strip().replace('\n\n', '\n').replace('\n\n', '\n')
            # while ('\n\n' in tmp_text):
            #     tmp_text = tmp_text.replace('\n\n', '\n')
            # if tmp_text:
            print(tmp_text)
            f.write(tmp_text + "\n")
    f.close()


path = "../面试相关/牛客游戏研发"

if __name__ == '__main__':
    # url = "https://www.nowcoder.com/discuss/experience/json?token=&tagId=639&companyId=0&phaseId=0&order=3&query=&page=1"
    url = "https://www.nowcoder.com/discuss/experience/json?token=&tagId=1194&companyId=0&phaseId=0&order=3&query=&page=1"

    for i in range(0, 100):
        url = url + str(i)
        if not os.path.exists(path):
            os.mkdir(path)
        tmp_path = path + "/第" + str(i) + "页面试题"
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        response = requests.get(url=url, headers=headers)
        json_str = json.loads(response.text)
        getDetail_Url(tmp_path, json_str)
        time.sleep(10)
