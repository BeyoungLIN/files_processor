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

line_width = [61, 61, 37, 45, 65, 85, 51, 36, 46, 67, 75, 46, 42, 70, 61, 41, 35, 67, 67, 45, 31, 47, 35, 66, 31, 31, 36, 85, 30, 31, 27, 67, 41, 41, 70, 41, 52, 47, 42, 66, 45, 42, 52, 45, 41, 45, 32, 77, 40, 40, 77, 87, 36, 40, 60, 42, 41, 67, 46, 45, 37, 41, 51, 56, 41, 42, 61]
line_width_new = []
for i in line_width:
    i_new = round(i/5, 0) * 5
    # print(i_new)
    line_width_new.append(i_new)
line_width_new.sort()
print(line_width_new)


count_plot(line_width_new)