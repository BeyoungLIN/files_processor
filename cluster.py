# -*- coding: utf-8 -*-
# @Time   : 2021/10/6 15:04
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : cluster.py

import collections
import itertools

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN, MeanShift, OPTICS, Birch


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


def cluster_boxes(boxes, type='DBSCAN'):
    switch = {
        'DBSCAN': DBSCAN(min_samples=1, eps=7),
        'MeanShift': MeanShift(bandwidth=0.3),
        'OPTICS': OPTICS(min_samples=1, eps=20),
        'Birch': Birch(n_clusters=None)
    }
    cluster = switch[type]
    boxes_data = [[b['l'], b['r']] for b in boxes]
    print(boxes_data)
    boxes_data = np.array(boxes_data)
    print(boxes_data)
    labels = cluster.fit_predict(boxes_data)
    # print(labels)
    print(boxes_data[:, 0], boxes_data[:, 1])
    # plt.scatter(boxes_data[:, 0], boxes_data[:, 1], s=1, c=labels)
    # plt.show()
    '''
    plt.scatter(boxes_data[:, 0], boxes_data[:, 1], s=1, c=labels)
    plt.show()
    '''
    classified_box_ids = collections.defaultdict(list)
    for idx, label in enumerate(labels):
        classified_box_ids[label].append(idx)
    return classified_box_ids


box_json = {0: [1100, 38, 1180, 38, 1180, 691, 1100, 691], 1: [1144, 714, 1196, 714, 1196, 941, 1144, 941],
            2: [1084, 714, 1137, 714, 1137, 852, 1084, 852], 3: [1105, 964, 1178, 964
        , 1178, 1447, 1105, 1447], 4: [1144, 1469, 1196, 1469, 1196, 1693, 1144, 1693],
            5: [1084, 1469, 1137, 1469, 1137, 1607, 1084, 1607], 6: [983, 37, 1057, 37, 1057, 357, 983
        , 357], 7: [1028, 380, 1074, 380, 1074, 431, 1028, 431], 8: [967, 380, 1013, 380, 1013, 433, 967, 433],
            9: [981, 453, 1058, 453, 1058, 523, 981, 523], 10: [1024, 545, 1076, 545, 1076, 682, 1024, 682],
            11: [962, 546, 1017, 546, 1017, 682, 962, 682], 12: [980, 708, 1060, 708, 1060, 1693, 980, 1693],
            13: [861, 37, 938, 37, 938, 520, 861, 520], 14: [904, 546, 956, 546, 956, 851, 904, 851],
            15: [845, 548, 896, 548, 896, 769, 845, 769], 16: [859, 877, 940, 877, 940, 1691, 859, 1691],
            17: [757, 34, 838, 34, 838, 1694, 757, 1694], 18: [676, 34, 753, 34, 753, 1698, 676, 1698],
            19: [590, 35, 670, 35, 670, 1698, 590, 1698], 20: [506, 34, 586, 34, 586, 1694, 506, 1694],
            21: [403, 40, 484, 40, 484, 775, 403, 775], 22: [447, 801, 501, 801, 501, 1693, 447, 1693],
            23: [387, 800, 440, 800, 440, 1690, 387, 1690], 24: [326, 45, 381, 45, 381, 765, 326, 765],
            25: [265, 46, 322, 46, 322, 764, 265, 764], 26: [166, 201, 242, 201, 242, 441, 166, 441],
            27: [212, 1221, 259, 1221, 259, 1273, 212, 1273], 28: [165, 1294, 237, 1294, 237, 1360, 165, 1360],
            29: [171, 1463, 234, 1463, 234, 1528, 171, 1528], 30: [63, 41, 140, 41, 140, 857, 63, 857],
            31: [61, 958, 141, 958, 141, 1696, 61, 1696]}
cords = [box for i, box in box_json.items()]
# print(cords)
cords_np = []
for cord in cords:
    cord = np.array(cord)
    cord = cord.reshape(-1, 2)
    # print(cord)
    cords_np.append(cord)
# cords = adjustColumeBoxes(cords)
# cords = adjustBoxesoutput(cords_np)
boxes = []
# print(cords_np)
boxes_np = cluster_sort(cords_np)
# boxes_np = cords_np
#
# for box in boxes_np:
#     box = box.reshape(-1, 8)
#     for box_ in box.tolist():
#         # print(box_)
#         # for box__ in box_:
#         boxes.append(box_)
# # print(boxes)
#
# data = np.array(
#     [43, 43, 44, 51, 52, 52, 52, 52, 53, 53, 53, 54, 55, 55, 57, 60, 69, 73, 74, 74, 76, 77, 77, 80, 80, 80, 80, 80, 81,
#      81, 81, 83])
# data = data.reshape(-1, 1)
# print(data)
# cluster_boxes(data)
