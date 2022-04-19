# -*- coding: utf-8 -*-
# @Time   : 2022/4/6 22:53
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : newcode_crawler.py

import pymysql
import requests
from lxml import html
import datetime
import time
import re
# import multiprocessing

class SpiderNKW(object):


    def spider(self, sn):
        '''nkw'''
        url = 'https://www.nowcoder.com/ta/review-c/review?page={0}'.format(sn)
        # url = 'https://www.nowcoder.com/ta/review-network/review?page={0}'.format(sn)
        resp = requests.get(url)
        # html文档
        resp = requests.get(url, headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2601.400',
        })
        resp.encoding = 'utf-8'
        rest = resp.text

        print('问题{0}:'.format(sn))
        # 问题
        title = re.findall('<div class="final-question">(.*?)</div>', rest, re.S)
        title = title[0]
        title = re.sub('(<p>)||(</p>)||<div>', '', title)
        title=title.strip().replace("'","\'")
        print(title)

        # 答案
        answer = re.findall('<div class="design-answer-box">(.*?)<div class="final-action clearfix">', rest, re.S)
        # print(answer[0])
        # answer=str(answer)
        answer = answer[0]
        answer = re.sub('(<div>)||(</div>)||(<br>)||(<p>)||(<br/>)||(</p>)||(<span>)||(</span>)', '', answer)

        content = answer.strip().replace("\'",'')
        print(content)

        # answer_after=re.sub('<div>','',answer)
        # answer_after=re.sub('\\\\n','',answer_after)
        # print(answer_after.strip())

        # ##把数据插入到mysql数据库中
        # conn = self.get_conn()
        # cursor = conn.cursor()
        # sql = "INSERT INTO `interview_question`(`title`, `content`, `created_at`,`url`) VALUES('{title}', '{content}', '{created_at}','{url}')".format(
        #     title=title, content=content, created_at=datetime.datetime.now(),url=url)
        #
        # print(sql)
        # # cursor.execute(sql)
        # # conn.commit()
        #
        # cursor.close()
        # conn.close()

    def get_conn(self):
        '''获取mysql数据库连接'''
        # try:
        conn = pymysql.connect(
            db='news',
            host='localhost',
            user='root',
            password='123456',
            charset='utf8'
            )
        # except:
        #     print('wrong')
            # pass
        return conn


if __name__ == '__main__':
    spider = SpiderNKW()

    #引入多进程
    # pool = multiprocessing.Pool(2)

    ##通过循环将页数传到url
    for page in range(1, 20):
        s = ''
        try:
            spider.spider(page)
        except:
            continue

