# -*- coding: utf-8 -*-
# @Time   : 2022/4/12 13:55
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : cut_video.py

import cv2

vc = cv2.VideoCapture('111_2.flv')  # 读取视频文件，修改为自己的文件名
c = 0
print("------------")
if vc.isOpened():
    print("yes")
    rval, frame = vc.read()
else:
    rval = False
    print("false")

timeF = 30    # 视频帧计数间隔

while rval:   # 循环读取视频
    rval,frame = vc.read()
    print(c,timeF,c%timeF)
    if (c % timeF == 0):
        print("write...")
        cv2.imwrite("./convert_data/photo_{}.jpg".format(c), frame)  # 修改为自己的文件夹
        print("success!")
    c = c + 1
cv2.waitKey(1)
vc.release()
print("==================================")