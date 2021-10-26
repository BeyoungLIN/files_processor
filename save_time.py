# -*- coding: utf-8 -*-
# @Time   : 2021/9/13 00:01
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : save_time.py


import datetime

# filetwo = open(r'D:\test.txt', 'a+')

# print('当前年份：' + str(datetime.datetime.now().year), file=filetwo)

# filetwo.close()
# sys_time = rospy.get_time()
ids = 1
with open('Interrupt.txt', 'a', encoding='utf-8') as ef:
    ef.write('log：'+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n' + str(ids))
