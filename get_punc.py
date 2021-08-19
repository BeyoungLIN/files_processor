# -*- coding: utf-8 -*-
# @Time   : 2021/8/13 00:50
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : get_api.py.py

# r=requests.get(url='https://www.baidu.com/')
# print(r.status_code)
# print(requests.post(url, content))

import argparse
import json
import time

import requests

parser = argparse.ArgumentParser()

# parser.add_argument('--text_file', type=str, default='punc_test.txt', help='directory to save samples')

if __name__ == '__main__':
    time.sleep(5)
    with open ('/disks/sde/beyoung/files_processor/temp/output/WechatIMG4930_res_recog_adv.txt', 'r') as f1:
        content = f1.readlines()
    with open('/disks/sde/beyoung/files_processor/temp/output/WechatIMG4930_res_recog_adv.txt', 'r') as f2:
        content_full = f2.read()
    for con in content:
        con = con.replace('<M>', '').replace('</M>', '').replace('\n', '')
        print(con)
    time.sleep(1)
    print('=' * 20 )
    print()
    time.sleep(1)
    content_full = content_full.replace('<M>', '').replace('</M>', '').replace('\n', '')
    print(content_full)
    print('=' * 20 )
    with open('punc_test.txt','r') as f:
        lines = f.readlines()
    # content = []

    # for line in lines:
    #     # line = line.split('|')[0]
    #     # print(line)
    #     dict = {"src": line}
    #     content.append(dict)
        # print(content)

        url = "https://punct.gj.cool/punct/test"
        headers = {'content-type': 'application/json'}
        # requestData = [{"src": "曲禮者。古禮篇之名。禮記多以簡端之語名篇。此篇名曲禮者。以篇首引之也。"}]
        requestData = [{"src": content_full}]
        ret = requests.post(url, json=requestData, headers=headers)
        # print(line.replace('\n', ''))
        if ret.status_code == 200:
            text = json.loads(ret.text)
            # print(txt.get('pred_sent') for txt in text)
            for txt in text:
                time.sleep(3)
                print(txt.get('pred_sent'))
            # time.sleep(20)
        # else:
            # print(ret.status_code)
        # print()
        # content = []
        # print(type(text))
