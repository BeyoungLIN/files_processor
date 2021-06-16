# -*- coding: utf-8 -*-
# @Time   : 2021/6/16 15:35
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : line_size.py

import collections
import matplotlib.pyplot as plt
import pandas as pd


# x = [0, 1]
# y = [0, 1]
# plt.figure()
# plt.plot(x, y)
# # plt.savefig("easyplot.jpg")


def count_plot(data_list):

    b = collections.Counter(data_list)

    # 转换成字典的格式
    dic = {number: value for number, value in b.items()}
    plt.title = "统计数字出现的次数"
    # 取得key
    x = [i for i in dic.keys()]
    y = []
    # 取得value
    for i in dic.keys():
        y.append(dic.get(i))
    # 转换成dataFrame的格式
    df = pd.DataFrame(y, x)
    # plt.hist(y, align='mid')
    # # 一个图表中画多个图
    # plt.xlabel = "number"
    # plt.ylabel = "count"
    # plt.subplot(221)
    # # 画折线图
    # plt.plot(x, y)
    # plt.subplot(222)
    # #画直方图
    # plt.hist(x)
    # plt.subplot(223)
    # 以dataFrame的格式画图
    df.plot()
    plt.show()

y=[1,1,2,3,4,5]

count_plot(y)