# -*- coding: utf-8 -*-
# @Time   : 2021/10/6 15:43
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : cluster2.py

import collections
import itertools

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN, MeanShift, OPTICS, Birch, AgglomerativeClustering


def list_sort(box_list):
    r = [b['r'] for b in box_list]
    length = [b['r'] - b['l'] for b in box_list]
    r = np.mean(r)
    length = np.mean(length)
    return r + length


def box_sort(box):
    u = box['u']
    d = box['d']
    return (u + d) / 2


def convert_bbox_to_lrud(bbox):
    l = min(bbox[:, 0])
    r = max(bbox[:, 0])
    u = min(bbox[:, 1])
    d = max(bbox[:, 1])
    return l, r, u, d


def cluster_sort(boxes):
    """
    :param boxes:
    :return: cluster then sorted boxes
        l = array[0, 0]
        r = array[1, 0]
        u = array[0, 1]
        d = array[2, 1]
    """
    # boxes_lrud = []
    # for id, box in enumerate(boxes):
    #     l, r, u, d = convert_bbox_to_lrud(box)
    #     boxes_lrud.append({'id': id, 'l': l, 'r': r, 'u': u, 'd': d})
    # # boxes_lrud = [{'l': b[0, 0], 'r': b[1, 0], 'u': b[0, 1], 'd': b[2, 1], 'id': id} for id, b in enumerate(boxes)]
    # '''
    # classified_box_ids = projection_split(shape, boxes_lrud)
    # classified_boxes = []
    # for k in classified_box_ids.keys():
    #     box_ids = classified_box_ids[k]
    #     classified_boxes.append([boxes_lrud[box_id] for box_id in box_ids])
    # '''
    # classified_box_ids = cluster_boxes(boxes_lrud)
    # # print(classified_box_ids)
    # classified_boxes = []
    # for k in classified_box_ids.keys():
    #     box_ids = classified_box_ids[k]
    #     classified_boxes.append([boxes_lrud[box_id] for box_id in box_ids])
    # classified_boxes = sorted(classified_boxes, key=list_sort, reverse=True)
    # new_classifier_boxes = []
    # for box_list in classified_boxes:
    #     new_classifier_boxes.append(sorted(box_list, key=box_sort, reverse=False))
    # new_classifier_boxes = list(itertools.chain.from_iterable(new_classifier_boxes))
    # new_classifier_boxes = [boxes[b['id']] for b in new_classifier_boxes]
    # return new_classifier_boxes
    boxes_lrud = [{'l': b[0, 0], 'r': b[1, 0], 'u': b[0, 1], 'd': b[2, 1], 'id': id} for id, b in enumerate(boxes)]
    print(boxes_lrud)
    classified_box_ids = cluster_boxes(boxes_lrud)
    classified_boxes = []
    for k in classified_box_ids.keys():
        box_ids = classified_box_ids[k]
        classified_boxes.append([boxes_lrud[box_id] for box_id in box_ids])
    classified_boxes = sorted(classified_boxes, key=list_sort, reverse=True)
    new_classifier_boxes = []
    for box_list in classified_boxes:
        new_classifier_boxes.append(sorted(box_list, key=box_sort, reverse=False))
    new_classifier_boxes = list(itertools.chain.from_iterable(new_classifier_boxes))
    new_classifier_boxes = [boxes[b['id']] for b in new_classifier_boxes]
    return new_classifier_boxes


def cluster_boxes4ers(widths, type='AgglomerativeClustering', adv=True):
    w_sorted = sorted(widths, reverse=False)
    switch = {
        'DBSCAN': DBSCAN(min_samples=1, eps=0.08),
        'MeanShift': MeanShift(bandwidth=0.3),
        'OPTICS': OPTICS(min_samples=1, eps=20),
        'Birch': Birch(n_clusters=None),
        'AgglomerativeClustering': AgglomerativeClustering()
    }
    cluster = switch[type]
    # boxes_data = [[b['l'], b['r']] for b in boxes]
    boxes_data = w_sorted
    boxes_data = np.array(boxes_data)
    boxes_data = boxes_data / w_sorted[-1]
    boxes_data = boxes_data.reshape(-1, 1)
    labels = cluster.fit_predict(boxes_data)
    '''
    plt.scatter(boxes_data[:, 0], boxes_data[:, 1], s=1, c=labels)
    plt.show()
    '''
    for i in range(len(labels)):
        print(w_sorted[i], labels[i])
    classified_box_ids = collections.defaultdict(list)
    for idx, label in enumerate(labels):
        classified_box_ids[label].append(idx)
    classified_boxes = []
    avgs = []
    count = 0
    for k in classified_box_ids.keys():
        box_ids = classified_box_ids[k]
        classified_boxes.append([w_sorted[box_ids[0]], w_sorted[box_ids[-1]]])
        if adv:  # 主要解决层次聚类至少归两类的问题
            widths_list = []
            for box in box_ids:
                widths_list.append(w_sorted[box])
            avgs_mean = np.mean(widths_list)
            if count > 0:
                if abs(avgs_mean - avgs[-1]) < 5:
                    classified_boxes.pop(-1)
                    new_min = classified_boxes[-1][0]
                    # print(new_min)
                    classified_boxes.pop(-1)
                    new_max = w_sorted[box_ids[-1]]
                    classified_boxes.append([new_min, new_max])
                    avgs_mean = (avgs_mean + avgs[-1]) / 2
                    avgs.pop(-1)
            avgs.append(avgs_mean)
            count += 1
    print(avgs)
    print(classified_boxes)
    return classified_boxes

# data_raw = [43, 43, 44, 51, 52, 52, 52, 52, 53, 53, 53, 54, 55, 55, 57, 60, 69, 73, 74, 74, 76, 77, 77, 80, 80, 80, 80, 80, 81]
# data_raw = [51, 60, 74, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81]
# data_raw = [81, 80, 80, 53, 54, 57, 57, 80, 44, 66, 60, 80, 80, 54, 54, 55, 57, 80, 77, 55, 76, 80, 83]
# data_raw = [81, 80, 80, 53, 54, 57, 57, 80, 47, 69, 61, 80, 80, 54, 54, 55, 57, 80, 77, 55, 76, 80, 83]
# data_raw = [80, 80, 54, 54, 81, 80, 54, 56, 81, 77, 77, 48, 67, 65, 77, 82, 80, 81, 54, 53, 77, 80, 75]
# data_raw = [81, 80, 80, 77, 80, 80, 81, 81, 80, 81, 81] # 77
# data_raw = [81, 80, 81, 77, 81, 81, 81, 81, 82, 81, 81]  # 77
data_raw_list = [
    # [43, 43, 44, 51, 52, 52, 52, 52, 53, 53, 53, 54, 55, 55, 57, 60, 69, 73, 74, 74, 76, 77, 77, 80, 80, 80, 80, 80, 81],  # 60
    # [81, 80, 80, 77, 80, 80, 81, 81, 80, 81, 81],  # 77
    # [81, 77, 47, 73, 81, 81, 81, 47, 73, 82, 77, 74, 47, 65, 76, 81, 80, 80, 57, 53],  # 65
    [81],  # 65
]
# data = np.array(data_raw)
# data = data.reshape(-1, 1)
# print(data)
for data_raw in data_raw_list:
    cluster_boxes4ers(data_raw, 'AgglomerativeClustering')
    print('-' * 50)
    cluster_boxes4ers(data_raw, 'DBSCAN')
    print('*' * 80)
'''
DBSCAN
51 0
60 1
74 2

MEAN 3
51 3
60 2
74 1

OPTICS
51 0
60 0
74 0

51 0
60 1
74 2
80 3

AgglomerativeClustering
51 0
60 0
74 1
'''
