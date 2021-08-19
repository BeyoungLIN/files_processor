# -*- coding: utf-8 -*-
# @Time   : 2021/8/16 11:48
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : draw_gram.py

import matplotlib.pyplot as plt


# 获取列表的第二个元素
def takeSecond(elem):
    return int(elem[0])


def gram(x_list, y_list):
    # plt.plot([1,2,3,4],[1,4,9,11])
    plt.plot(x_list, y_list)
    plt.xticks(range(0, 24, 1))
    # plt.yticks(range(0, 22, 2))
    plt.ylabel('some numbers')
    plt.show()


data = [('13', 41) ,
('12', 35) ,
('22', 32) ,
('17', 31) ,
('14', 26) ,
('18', 24) ,
('19', 21) ,
('16', 19) ,
('23', 18) ,
('00', 17) ,
('20', 17) ,
('21', 17) ,
('15', 14) ,
('11', 11) ,
('01', 8) ,
('10', 7) ,
('02', 4) ,
('09', 4) ,
('08', 1) ,
('03', 1) ,
('24', 17) ,
        ]

data.sort(key=takeSecond)

x_s = []
y_s = []

for item in data:
    x_s.append(int(item[0]))
    y_s.append(int(item[1]))
# x_s.sort()
# y_s.sort()

gram(x_s, y_s)
