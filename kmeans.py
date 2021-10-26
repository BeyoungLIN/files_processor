# -*- coding: utf-8 -*-
# @Time   : 2021/10/4 16:28
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : kmeans.py

from sklearn.cluster import KMeans
import numpy as np
# x = np.random.random(10000)
x = [45, 51, 52, 53, 53, 54, 55, 62, 64, 72, 77, 77, 77, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81]
a = np.asarray(x)
y = a.reshape(-1,1)
km = KMeans()
km.fit(y)
km.cluster_centers_
