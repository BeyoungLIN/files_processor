# -*- coding: utf-8 -*-
# @Time   : 2021/10/4 16:59
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : dbscan.py

import numpy as np
from sklearn.cluster import DBSCAN
# 加载数据
# data=np.loadtxt("788points.txt",delimiter=",")
# data = [45, 51, 52, 53, 53, 54, 55, 62, 64, 72, 77, 77, 77, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81]
# data = np.array(data)
# data = data.reshape(-1, 1)
data = np.loadtxt("/Users/Beyoung/Desktop/Projects/data/788points.txt", delimiter=",")
print(data)
# 构造一个ϵ=2,MinPts=15的聚类器，距离使用欧式距离
estimator=DBSCAN(eps=2,min_samples=15,metric='euclidean')
# 聚类数据
estimator.fit(data)
# 输出聚类都类别（-1代表异常点）
print(estimator.labels_)