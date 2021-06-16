# -*- coding: utf-8 -*-
# @Time   : 2021/6/2 15:41
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : craft_db_mix_test.py

# coding:utf-8


import math
import os
import random
import sys
import traceback

from detect.detector0.detector import crop_rect

from test_api_v0_test import *

import numpy as np
from PIL import Image
from skimage import io
import cv2
import six,base64

from detect.detector0.detector import Detector
from detect.detector2.detector2 import Detector2
from recog.recog0.recog1 import Recog1, empty_img

from detect.detector0.detector import crop_rect
from detect.postdetect import concat_boxes, get_w_rngs, get_line_size, re_mapping_lsize

# from postdetect import concat_boxes

IMG_EXT = {'.jpg', '.png', '.tif', '.tiff', '.bmp', '.gif'}

blank_img = empty_img

import time


def base64of_img(pth_img):
    image_base64 = ''
    with open(pth_img, 'rb') as f:
        image = f.read()
        image_base64 = str(base64.b64encode(image), encoding='utf-8')
    return image_base64


def base64_to_PIL(string):
    """
    base64 string to PIL
    """
    try:
        base64_data = base64.b64decode(string)
        buf = six.BytesIO()
        buf.write(base64_data)
        buf.seek(0)
        img = Image.open(buf).convert('RGB')
        return img
    except Exception as e:
        print(e)
        return None


def readPILImg(pth_img):
    img_base64 = base64of_img(pth_img)
    img = base64_to_PIL(img_base64)
    return img


def crop_rect(img, rect, alph=0.15):
    img = np.asarray(img)
    # get the parameter of the small rectangle
    # # print("rect!")
    # # print(rect)
    center, size, angle = rect[0], rect[1], rect[2]
    min_size = min(size)

    if (angle > -45):
        center, size = tuple(map(int, center)), tuple(map(int, size))
        # angle-=270
        size = (int(size[0] + min_size * alph), int(size[1] + min_size * alph))
        height, width = img.shape[0], img.shape[1]
        M = cv2.getRotationMatrix2D(center, angle, 1)
        # size = tuple([int(rect[1][1]), int(rect[1][0])])
        img_rot = cv2.warpAffine(img, M, (width, height))
        # cv2.imwrite("debug_im/img_rot.jpg", img_rot)
        img_crop = cv2.getRectSubPix(img_rot, size, center)
    else:
        center = tuple(map(int, center))
        size = tuple([int(rect[1][1]), int(rect[1][0])])
        size = (int(size[0] + min_size * alph), int(size[1] + min_size * alph))
        angle -= 270
        height, width = img.shape[0], img.shape[1]
        M = cv2.getRotationMatrix2D(center, angle, 1)
        img_rot = cv2.warpAffine(img, M, (width, height))
        # cv2.imwrite("debug_im/img_rot.jpg", img_rot)
        img_crop = cv2.getRectSubPix(img_rot, size, center)
    img_crop = Image.fromarray(img_crop)
    return img_crop


def crop_img(img, cord):
    image_np = np.array(img)
    # 获取坐标
    _cord = cord[0], cord[1], cord[4], cord[5]
    xmin, ymin, xmax, ymax = _cord
    # 坐标到中心点、高宽转换
    center, size = ((xmin + xmax) / 2, (ymin + ymax) / 2), (xmax - xmin, ymax - ymin)
    rect = center, size, 0
    partImg = crop_rect(image_np, rect)

    return partImg


def cv_imread(file_path=""):
    img_mat = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    return img_mat


def cv_imwrite(file_path, frame):
    cv2.imencode('.jpg', frame)[1].tofile(file_path)


def draw_box(cords, pth_img, pth_img_rect, color=(0, 0, 255), resize_x=1.0, thickness=1, text='', seqnum=False):
    try:
        # img = cv2.imread(pth_img)
        img = cv_imread(pth_img)  # 解决中文路径文件的读
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        boxes = []

        for cord in cords:
            _cord = int(cord[0]), int(cord[1]), int(cord[4]), int(cord[5])
            xmin, ymin, xmax, ymax = _cord
            if resize_x < 1.0:
                _cord = scale_x(_cord, resize_x)
            boxes.append(_cord)

        font = cv2.FONT_HERSHEY_SIMPLEX
        for ibox, box in enumerate(boxes):
            x, y, x_, y_ = box
            # draw_1 = cv2.rectangle(img, (x,y), (x_,y_), (0,0,255), 2 )
            draw_1 = cv2.rectangle(img, (x, y), (x_, y_), color, thickness)
            if seqnum:
                draw_1 = cv2.putText(img, str(ibox), (int((x + x_) / 2 - 10), y + 20), font, 0.6, color=color)
            if not '' == text:
                font = cv2.FONT_HERSHEY_SIMPLEX
                draw_1 = cv2.putText(img, text, (int((x + x_) / 2 - 10), y + 16), font, 0.4, color=color)

        # print('Writing to image with rectangle {}\n'.format(pth_img_rect))

        cv_imwrite(pth_img_rect, draw_1)  # 解决中文路径文件的写
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, e.__str__(), ',File', fname, ',line ', exc_tb.tb_lineno)
        traceback.print_exc()  # debug.error(e)


def draw_line(cords, pth_img, pth_img_rect, color=(0, 0, 255), thickness=2):
    try:
        # img = cv2.imread(pth_img)
        img = cv_imread(pth_img)  # 解决中文路径文件的读
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        lines = []

        for cord in cords:
            _cord = int(cord[0]), int(cord[1]), int(cord[2]), int(cord[3])
            xmin, ymin, xmax, ymax = _cord
            lines.append(_cord)

        for line in lines:
            x, y, x_, y_ = line

            draw_1 = cv2.line(img, (x, y), (x_, y_), color, thickness)

        # print('Writing to image with rectangle {}\n'.format(pth_img_rect))

        cv_imwrite(pth_img_rect, draw_1)  # 解决中文路径文件的写
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, e.__str__(), ',File', fname, ',line ', exc_tb.tb_lineno)
        traceback.print_exc()  # debug.error(e)


'''
post detecting functions begin here
'''


def scale_x(_cords, resize_x):
    xmin, ymin, xmax, ymax = _cords
    xmid = (xmin + xmax) / 2
    xmin_ = math.ceil(xmid - resize_x * (xmid - xmin))
    xmax_ = math.floor(xmid + resize_x * (xmax - xmid))

    return xmin_, ymin, xmax_, ymax


def scale_y(_cords, resize_y):
    xmin, ymin, xmax, ymax = _cords
    ymid = (ymin + ymax) / 2
    ymin_ = math.ceil(ymid - resize_y * (ymid - ymin))
    ymax_ = math.floor(ymid + resize_y * (ymax - ymid))

    return xmin, ymin_, xmax, ymax_


from colors import COLORS


def randcolors(n=10):
    _colors = []
    for color_series, color_dct in COLORS.items():
        for k, v_rgb in color_dct.items():
            _colors.append(tuple([int(num) for num in v_rgb.split(',')]))
    # return [ random.choice(_colors) for i in range(n)]
    return random.sample(_colors, n)


def conv_cords(cord):
    # 将[ 左上，右上，右下，左下 ] 的坐标 转换为 [左上，右下，宽，长，宽长比] 格式
    _cord = xmin, ymin, xmax, ymax = int(cord[0]), int(cord[1]), int(cord[4]), int(cord[5])
    w = xmax - xmin
    h = ymax - ymin
    w_h = w / h
    return list(_cord) + [w, h, w_h]


def line_interact(line1, line2, minDot, axis='x'):
    Xmin, Ymin = minDot
    # 判断两线段是否相叠
    interacted, interacted_x, interacted_y = False, False, False
    line_u = []
    xmin1, xmax1, ymin1, ymax1 = line1[0], line1[2], line1[1], line1[3]
    xmin2, xmax2, ymin2, ymax2 = line2[0], line2[2], line2[1], line2[3]
    _xmin = min(xmin1, xmin2)
    # 相叠判断逻辑
    if xmin1 <= xmax2 and xmin2 <= xmax1: interacted_x = True
    if ymin1 <= ymax2 and ymin2 <= ymax1: interacted_y = True
    # 线段并
    line_u_x = [min(xmin1, xmin2), Ymin - 2, max(xmax1, xmax2), Ymin - 2]
    line_u_y = [_xmin - 2, min(ymin1, ymin2), _xmin - 2, max(ymax1, ymax2)]
    # 线段交
    line_inter_x = [max(xmin1, xmin2), Ymin - 2, min(xmax1, xmax2), Ymin - 2]
    line_inter_y = [Xmin - 2, max(ymin1, ymin2), Xmin - 2, min(ymax1, ymax2)]

    interacted, line_u, line_inter = interacted_x, line_u_x, line_inter_x
    if 'y' == axis:
        interacted, line_u, line_inter = interacted_y, line_u_y, line_inter_y
    return interacted, line_u, line_inter


def rec_interact(box1, box2, minDot):
    xmin1, ymin1, xmax1, ymax1 = box1[0], box1[1], box1[2], box1[3]
    xmin2, ymin2, xmax2, ymax2 = box2[0], box2[1], box2[2], box2[3]
    line1x = [xmin1, ymin1, xmax1, ymin1]
    line2x = [xmin2, ymin2, xmax2, ymin2]
    line1y = [xmin1, ymin1, xmin1, ymax1]
    line2y = [xmin2, ymin2, xmin2, ymax2]
    interacted_x, interacted_y = False, False
    interacted_x, linex_u, linex_inter = line_interact(line1x, line2x, minDot)
    interacted_y, liney_u, liney_inter = line_interact(line1y, line2y, minDot, axis='y')
    return (interacted_x and interacted_y), linex_inter, liney_inter


def filter_subbox(cords, bigbox, minDot):
    cord_ = [bigbox[0], bigbox[1], bigbox[4], bigbox[5]]
    subboxes = [
        cord for cord in cords \
        if rec_interact(cord, cord_, minDot)[0]
    ]
    return subboxes


def union_2box(box1, box2, cords_db):
    # 合并两个相交的box
    xmin1, ymin1, xmax1, ymax1 = box1[0], box1[1], box1[2], box1[3]
    xmin2, ymin2, xmax2, ymax2 = box2[0], box2[1], box2[2], box2[3]
    xmin, ymin = min(xmin1, xmin2), min(ymin1, ymin2)
    xmax, ymax = max(xmax1, xmax2), max(ymax1, ymax2)

    '''  
    # 判断是否只有cord_craft成员
    if box1 in cords_db and not box2 in cords_db:
        _xmin,_ymin, _xmax,_ymax = xmin1, ymin1, xmax1, ymax1
        # if ymax-ymin > _ymax-_ymin: _ymax, _ymin = ymax, ymin
        # if _xmin > xmin and _xmax < xmax: _xmin, _xman = xmin, xmax
        return _xmin,_ymin, _xmax,_ymax
    if not box1 in cords_db and box2 in cords_db:
        _xmin,_ymin, _xmax,_ymax = xmin2, ymin2, xmax2, ymax2
        # if ymax-ymin > _ymax-_ymin: _ymax, _ymin = ymax, ymin
        # if _xmin > xmin and _xmax < xmax: _xmin, _xman = xmin, xmax
        return _xmin,_ymin, _xmax,_ymax
'''
    if box2 in cords_db:
        ymin, ymax = ymin2, ymax2
        if ymin1 < ymin and ymax1 > ymax:
            ymin, ymax = ymin1, ymax1
    if not (box2 in cords_db) and not (ymin2 < ymin1 and ymax2 > ymax1):
        ymin, ymax = ymin1, ymax1
    return [xmin, ymin, xmax, ymax]


def union_subboxes(sub_boxes, cords_db, minDot, URatio=0.6):
    sub_boxes.sort(key=lambda pt: pt[1])
    boxes_union = []
    while len(sub_boxes) > 0:
        # box_u = sub_boxes[0]
        # sub_boxes.remove(box_u)
        box_u = sub_boxes.pop(0)
        inter_u = []
        for i, sub_box in enumerate(sub_boxes):
            interacted, linex_inter, liney_inter = rec_interact(box_u, sub_box, minDot)
            # 相交， x和y方向相交率 > 0.6  (0.6这个值需要测)
            lx_boxu, ly_boxu = abs(box_u[2] - box_u[0]), abs(box_u[3] - box_u[1])
            lx_subbox, ly_subbox = abs(sub_box[2] - sub_box[0]), abs(sub_box[3] - sub_box[1])
            lx_inter, ly_inter = abs(linex_inter[2] - linex_inter[0]), abs(liney_inter[3] - liney_inter[1])

            if interacted:
                # print('ly_inter/ly_boxu:\t{}'.format(ly_inter/ly_boxu))
                # if not sub_box in cords_db:
                inter_u.append(sub_box)
                if (ly_inter / ly_boxu) < 0.08:
                    continue
                if ly_subbox < lx_subbox and \
                        ((lx_inter / lx_subbox) < URatio or (lx_inter / lx_boxu) < URatio):
                    continue
                box_u = union_2box(box_u, sub_box, cords_db)
                # 相交， x和y方向有一个方向 < 0.6
                # < 0.6的那个方向，不参与合并，但参与remove
        for box_ in inter_u: sub_boxes.remove(box_)
        boxes_union.append(box_u)
    return boxes_union


# y轴方向线段归并
def liney_union(lines, minDot):
    if len(lines) <= 1: return lines
    lines_union, line_u = [], lines[0]

    for i in range(1, len(lines)):
        _line = lines[i]
        interacted, _line_u, _ = line_interact(line_u, _line, minDot, axis='y')
        if interacted:
            line_u = _line_u
        else:
            lines_union.append(line_u)
            line_u = _line
    lines_union.append(line_u)
    return lines_union


def line_inter_box(line, box, minDot, axis='x'):
    _xmin, _ymin, _xmax, _ymax = line[0], line[1], line[2], line[3]
    xmin, ymin, xmax, ymax = box[0], box[1], box[2], box[3]
    liney_box = [xmin, ymin, xmin, ymax]
    linex_box = [xmin, ymin, xmax, ymin]

    interacted = False
    interacted_x, line_u_x, _ix = line_interact(line, liney_box, minDot)
    interacted_y, line_u_y, _iy = line_interact(line, liney_box, minDot, axis='y')
    if 'y' == axis: interacted = interacted_y
    return interacted


def ygroup_uboxes(_uboxes, minDot):
    ygrp_uboxes, ulines_y = {}, []
    _cords = _uboxes
    # 7.0 竖向坐标缩放0.9
    # 高度缩放比例， RESIZE_Y 参数配置
    # RESIZE_Y = 0.9
    # _cords = [ list(scale_y(_cord, RESIZE_Y)) for _cord in _cords ]

    # 7.1 竖向分组
    # liney [xmin-2, ymin, xmin-2, ymax]
    lines_y = [[c_d[0] + 1, c_d[1], c_d[0] + 1, c_d[3]] for c_d in _cords]
    lines_y.sort(key=lambda pt: pt[1])

    ulines_y = liney_union(lines_y, minDot)
    for i, uline_y in enumerate(ulines_y):
        # y方向与uline_y相交的ubox归为一组
        ygrp_uboxes[i] = [_ubox for _ubox in _uboxes if line_inter_box(uline_y, _ubox, minDot, axis='y')]
        # 竖向组内，横向排序 （x轴方向从大到小）
        ygrp_uboxes[i].sort(key=lambda pt: pt[2], reverse=True)

    return ygrp_uboxes, ulines_y


def isinter2plus(cord, cords_db_orig_, minDot):
    intercount = 0
    cord1 = xmin, ymin, xmax, ymax = cord[0], cord[1], cord[2], cord[3]
    for cord_ in cords_db_orig_:
        cord2 = xmin_, ymin_, xmax_, ymax_ = cord_[0], cord_[1], cord_[2], cord_[3]
        if rec_interact(cord1, cord2, minDot)[0]:
            intercount += 1
    return intercount >= 2


# class RecogHandler():
#     def __init__(self):
#         print('Initializing detector and recoginer models')
#         self.detector = Detector()
#         self.detector2 = Detector2()
#         self.recog = Recog1()
#
#     def detect_char(self, img, image_path=''):
#         '''
#         @param img PIL Image
#         '''
#         res_box_chars = {}
#         res4api = []
#         if img is not None:
#             img = np.array(img)
#             res_box_chars = self.detector.detect(img, ocr_type='single_char', image_path=image_path)
#         res4api = [
#             {
#                 'box': [str(pt) for pt in box],
#                 'name': i,
#                 'text': ''
#             } for i, box in res_box_chars.items()
#         ]
#         return res_box_chars, res4api
#
#     def detect_line(self, img, image_path=''):
#         '''
#         @param img PIL Image
#         '''
#         res_box_lines = {}
#         res4api = {}
#         if img is not None:
#             img = np.array(img)
#             res_box_lines = self.detector.detect(img, ocr_type='force_colume', image_path=image_path)
#         res4api = [
#             {
#                 'box': [str(pt) for pt in box],
#                 'name': str(i),
#                 'text': ''
#             } for i, box in res_box_lines.items()
#         ]
#         return res_box_lines, res4api
#
#     def detect_line_1(self, img):
#         '''
#         @param img PIL Image
#         '''
#         if img is not None:
#             img_np = np.array(img).astype('float32')
#             res_box_lines = self.detector2.detect(img_np)
#         res4api = [
#             {
#                 'box': [str(pt) for pt in box],
#                 'name': str(i),
#                 'text': ''
#             } for i, box in res_box_lines.items()
#         ]
#         return res_box_lines, res4api
#
#     def detect_ocr_line(self, img):
#         '''
#         @deprecated
#         '''
#         # dectect line
#         res_box_lines, _ = self.detect_line(img)
#
#         # crop line
#         PIL_imgs = []
#         image_np = np.array(img)
#         for i, cord in res_box_lines.items():
#             # 获取坐标
#             _cord = cord[0], cord[1], cord[4], cord[5]
#             xmin, ymin, xmax, ymax = _cord
#             # 坐标到中心点、高宽转换
#             center, size = ((xmin + xmax) / 2, (ymin + ymax) / 2), (xmax - xmin, ymax - ymin)
#             rect = center, size, 0
#             partImg = crop_rect(image_np, rect)  # 截取部分
#             PIL_imgs.append(partImg)
#         res_lines_ocr = []
#         for img_line in PIL_imgs:
#             res_line_ocr = self.ocr_line(img_line)
#             print(res_line_ocr['best'])
#             res_lines_ocr.append(res_line_ocr['best'])
#         # ocr each line
#         res4api = [
#             {
#                 'box': [str(pt) for pt in cord],
#                 'name': str(i),
#                 'text': res_lines_ocr[i]['text']
#             } for i, cord in res_box_lines.items()
#         ]
#
#         return res_box_lines, res_lines_ocr, res4api
#
#     def ocr_line(self, img):
#         '''
#         @param img PIL Image
#         '''
#         cands = res_line = self.recog.predict_one(img)
#         if len(cands) == 0:
#             cands = [{
#                 'confidence': 0.0,
#                 'char': ''
#             }]
#         res = {
#             'best': {
#                 'confidence': cands[0]['confidence'],
#                 'text': cands[0]['char']
#             },
#             'cands': [
#                 {
#                     'confidence': cand['confidence'],
#                     'text': cand['char']
#                 } for cand in cands
#             ]
#         }
#         return res
#
#     def recog_line(self, img):
#         '''
#         @ recog_line升级为recog_page现在功能,
#         @ recog_page升级为检测识别列/检测识别列中的字
#         @param img PIL Image
#         '''
#
#         cands = res_line = self.recog.predict_one(img)
#         if len(cands) == 0:
#             cands = [{
#                 'confidence': 0.0,
#                 'char': ''
#             }]
#         res = {
#             'best': {
#                 'confidence': cands[0]['confidence'],
#                 'text': cands[0]['char']
#             },
#             'cands': [
#                 {
#                     'confidence': cand['confidence'],
#                     'text': cand['char']
#                 } for cand in cands
#             ]
#         }
#         return res
#
#     def ocr_many(self, imgList):
#         res = self.recog.predict(imgList)
#         return res
#
#     def rng_interact(self, rng1, rng2):
#         interacted = False
#         xmin1, xmax1 = rng1[0], rng1[1]  # 最小x差值的放缩
#         xmin2, xmax2 = rng2[0], rng2[1]
#         # print(xmin1, xmax1, xmin2, xmax2)
#         if xmin1 <= xmax2 and xmin2 <= xmax1: interacted = True  # 此处不确定,缩小后的都要比另一个放大后的小
#         rng_u = [min(xmin1, xmin2), max(xmax1, xmax2)]  # rng_u理论上是 x min 1和 x max 2
#         return interacted, rng_u
#
#     def get_w_rngs(self, widths, R=0.1):
#         w_sorted = sorted(widths)  # 把所有x的差值排序
#         w_rngs_tmp = [[w * (1 - R), w * (1 + R)] for w in w_sorted]  # w_rngs_tmp为w放大缩小0.1
#         # print(w_rngs_tmp)
#         w_rngs, w_rng = [], w_rngs_tmp.pop(0)  # w_rng把最小的取出来
#         for _rng in w_rngs_tmp:
#             interacted, rng_u = self.rng_interact(w_rng, _rng)  # _rng每个放缩后的坐标
#             # print(interacted, _rng)
#         if interacted:
#             w_rng = rng_u  # rng_u理论上是 x min 1和 x max 2
#         else:
#             w_rngs.append(w_rng)
#             w_rng = _rng
#         # print(w_rngs)
#         return w_rngs
#
#     def get_line_size(self, w_rngs, w):
#         sizes = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL']
#         # print(w_rngs)
#         for i, rng in enumerate(w_rngs):
#             rngl, rngr = rng[0], rng[1]  # (0,x min1 缩; 1, x min1 放)
#             if rngl <= w <= rngr: return sizes[i]  # 18.9 <= w <= 23.1, return S
#         return sizes[-1]
#
#     def ocr_page(self, img, detector='craft'):
#         adv_res, concat_res = {}, {}
#         # 默认是craft行检测
#         res_detect_line, res4api_detect_line = self.detect_line(img)
#         if 'craft_char' == detector:
#             res_detect_line, res4api_detect_line = self.detect_char(img)
#         if 'db' == detector:
#             # 替换成db的行检测
#             res_detect_line, res4api_detect_line = self.detect_line_1(img)
#         if 'mix' == detector:
#             # 同时求db的行检测，并进行融合, 返回简单结果格式
#             res_detect_line, res4api_detect_line = self.detect_line(img)
#             res_detect_line_db, res4api_detect_line_db = self.detect_line_1(img)
#             concat_res = concat_boxes(res4api_detect_line, res4api_detect_line_db)
#         if 'adv' == detector:
#             # 同时求db的行检测，并进行融合, 返回复杂结果格式
#             res_detect_line, res4api_detect_line = self.detect_line(img)
#             res_detect_line_db, res4api_detect_line_db = self.detect_line_1(img)
#             concat_res = concat_boxes(res4api_detect_line, res4api_detect_line_db)
#         img_lst = []
#
#         if 'mix' == detector or 'adv' == detector:
#             uboxes_g = concat_res['uboxes_g']
#             # print(uboxes_g)
#             # print()
#             res_detect_line = {i: [ub[0], ub[1], ub[2], ub[1], ub[2], ub[3], ub[0], ub[3]] \
#                                for i, ub in enumerate(uboxes_g)}
#             # print(ub)
#             # print(res_detect_line)
#             res4api_detect_line = [
#                 {
#                     'box': [str(pt) for pt in box],
#                     'name': str(i),
#                     'text': ''
#                 } for i, box in res_detect_line.items()
#             ]
#
#         widths_line = []
#         for index, cord in res_detect_line.items():
#             try:
#                 img_line = crop_img(img, cord)
#                 img_lst.append(img_line)
#                 # print(img_line)
#                 x1, y1, x2, y2, x3, y3, x4, y4 = cord
#                 min_x, max_x = round((x1 + x4) / 2), round((x2 + x3) / 2)  # 为什么不直接 min_x, max_x = x1, x2 ?
#                 widths_line.append(abs(max_x - min_x))
#             except Exception as e:
#                 print(e)
#                 continue
#
#         width_rngs = self.get_w_rngs(widths_line)  # 得到的还是最小框的放缩?w_rngs
#         res_ocr_many = self.ocr_many(img_lst)  # 此处已经做好排序
#
#         # print()
#         # print(res4api_detect_line)
#
#         for i, r_line in enumerate(res4api_detect_line):
#             res_ocr_line = res_ocr_many[i]
#             # print(res_ocr_line)
#             cands = res_ocr_line['cands']
#             # print(cands)
#
#             cand = cands[0]['char']
#             r_line['text'] = cand
#             # 字检测结果
#             len_chars = len(cand)  # 字数
#             box_line = r_line['box']
#             x1, y1, x2, y2, x3, y3, x4, y4 = box_line = [int(cord) for cord in box_line]
#             min_x, max_x = round((x1 + x4) / 2), round((x2 + x3) / 2)
#             min_y, max_y = round((y1 + y2) / 2), round((y3 + y4) / 2)
#             width_line = abs(max_x - min_x)  # 框宽度
#
#             boxes_char = []
#             if len_chars > 0:
#                 h_char = (max_y - min_y) / len_chars  # 框高度/字数 ≈ 字高度
#                 for j in range(len_chars):
#                     box = [
#                         min_x, min_y + j * h_char, max_x, min_y + j * h_char,
#                         max_x, min_y + (j + 1) * h_char, min_x, min_y + (j + 1) * h_char
#                     ]
#                     box_char = {
#                         'box': [str(round(pt)) for pt in box],
#                         'name': j,
#                         'text': cand[j]
#                     }
#                     boxes_char.append(box_char)
#             r_line['boxes_char'] = boxes_char
#             # print(width_rngs, width_line)
#             line_size = self.get_line_size(width_rngs, width_line)  # 最小框的缩, 放, 框宽度
#             # r_line['size'] = 'M'
#             r_line['size'] = line_size
#             # print(line_size)
#
#         res = res4api_detect_line
#         if 'adv' == detector:
#             res = adv_res = {
#                 'res_basic': res4api_detect_line,
#                 'big_sub_boxes': concat_res['bigboxes_uboxes']
#             }
#         return res

class RecogHandler():
    def __init__(self):
        print('Initializing detector and recoginer models')
        self.detector = Detector()
        self.detector2 = Detector2()
        self.recog = Recog1()

    def detect_char(self, img, image_path=''):
        '''
        @param img PIL Image
        '''
        res_box_chars = {}
        res4api = []
        if img is not None:
            img = np.array(img)
            res_box_chars = self.detector.detect(img, ocr_type='single_char', image_path=image_path)
        res4api = [
            {
                'box': [str(pt) for pt in box],
                'name': i,
                'text': ''
            } for i, box in res_box_chars.items()
        ]
        return res_box_chars, res4api

    def detect_line(self, img, image_path=''):
        '''
        @param img PIL Image
        '''
        res_box_lines = {}
        res4api = {}
        if img is not None:
            img = np.array(img)
            res_box_lines = self.detector.detect(img, ocr_type='force_colume', image_path=image_path)
        res4api = [
            {
                'box': [str(pt) for pt in box],
                'name': str(i),
                'text': ''
            } for i, box in res_box_lines.items()
        ]
        return res_box_lines, res4api

    def detect_line_1(self, img):
        '''
        @param img PIL Image
        '''
        if img is not None:
            img_np = np.array(img).astype('float32')
            res_box_lines = self.detector2.detect(img_np)
        res4api = [
            {
                'box': [str(pt) for pt in box],
                'name': str(i),
                'text': ''
            } for i, box in res_box_lines.items()
        ]
        return res_box_lines, res4api

    def detect_ocr_line(self, img):
        '''
        @deprecated
        '''
        # dectect line
        res_box_lines, _ = self.detect_line(img)

        # crop line
        PIL_imgs = []
        image_np = np.array(img)
        for i, cord in res_box_lines.items():
            # 获取坐标
            _cord = cord[0], cord[1], cord[4], cord[5]
            xmin, ymin, xmax, ymax = _cord
            # 坐标到中心点、高宽转换
            center, size = ((xmin + xmax) / 2, (ymin + ymax) / 2), (xmax - xmin, ymax - ymin)
            rect = center, size, 0
            partImg = crop_rect(image_np, rect)  # 截取部分
            PIL_imgs.append(partImg)
        res_lines_ocr = []
        for img_line in PIL_imgs:
            res_line_ocr = self.ocr_line(img_line)
            print(res_line_ocr['best'])
            res_lines_ocr.append(res_line_ocr['best'])
        # ocr each line
        res4api = [
            {
                'box': [str(pt) for pt in cord],
                'name': str(i),
                'text': res_lines_ocr[i]['text']
            } for i, cord in res_box_lines.items()
        ]

        return res_box_lines, res_lines_ocr, res4api

    def ocr_line(self, img):
        '''
        @param img PIL Image
        '''
        cands = res_line = self.recog.predict_one(img)
        if len(cands) == 0:
            cands = [{
                'confidence': 0.0,
                'char': ''
            }]
        res = {
            'best': {
                'confidence': cands[0]['confidence'],
                'text': cands[0]['char']
            },
            'cands': [
                {
                    'confidence': cand['confidence'],
                    'text': cand['char']
                } for cand in cands
            ]
        }
        return res

    def recog_line(self, img):
        '''
        @ recog_line升级为recog_page现在功能,
        @ recog_page升级为检测识别列/检测识别列中的字
        @param img PIL Image
        '''

        cands = res_line = self.recog.predict_one(img)
        if len(cands) == 0:
            cands = [{
                'confidence': 0.0,
                'char': ''
            }]
        res = {
            'best': {
                'confidence': cands[0]['confidence'],
                'text': cands[0]['char']
            },
            'cands': [
                {
                    'confidence': cand['confidence'],
                    'text': cand['char']
                } for cand in cands
            ]
        }
        return res

    def ocr_many(self, imgList):
        res = self.recog.predict(imgList)
        return res

    def ocr_page(self, img, detector='craft'):
        adv_res, concat_res = {}, {}
        # 默认是craft行检测
        res_detect_line, res4api_detect_line = self.detect_line(img)
        if 'craft_char' == detector:
            res_detect_line, res4api_detect_line = self.detect_char(img)
        if 'db' == detector:
            # 替换成db的行检测
            res_detect_line, res4api_detect_line = self.detect_line_1(img)
        if 'mix' == detector:
            # 同时求db的行检测，并进行融合, 返回简单结果格式
            res_detect_line, res4api_detect_line = self.detect_line(img)
            res_detect_line_db, res4api_detect_line_db = self.detect_line_1(img)
            concat_res = concat_boxes(res4api_detect_line, res4api_detect_line_db)
        if 'adv' == detector:
            # 同时求db的行检测，并进行融合, 返回复杂结果格式
            res_detect_line, res4api_detect_line = self.detect_line(img)
            res_detect_line_db, res4api_detect_line_db = self.detect_line_1(img)
            concat_res = concat_boxes(res4api_detect_line, res4api_detect_line_db)
        img_lst = []

        if 'mix' == detector or 'adv' == detector:
            uboxes_g = concat_res['uboxes_g']
            res_detect_line = {i: [ub[0], ub[1], ub[2], ub[1], ub[2], ub[3], ub[0], ub[3]] \
                               for i, ub in enumerate(uboxes_g)}
            res4api_detect_line = [
                {
                    'box': [str(pt) for pt in box],
                    'name': str(i),
                    'text': ''
                } for i, box in res_detect_line.items()
            ]

        widths_line = []
        for index, cord in res_detect_line.items():
            try:
                img_line = crop_img(img, cord)
                img_lst.append(img_line)

                x1, y1, x2, y2, x3, y3, x4, y4 = cord
                min_x, max_x = round((x1 + x4) / 2), round((x2 + x3) / 2)
                widths_line.append(abs(max_x - min_x))
                print(abs(max_x - min_x))
            except Exception as e:
                print(e)
                continue

        width_rngs = get_w_rngs(widths_line)
        res_ocr_many = self.ocr_many(img_lst)
        M_size = []
        L_size = []
        XL_size = []
        XXL_size = []
        XXXL_size = []
        S_size = []


        for i, r_line in enumerate(res4api_detect_line):
            res_ocr_line = res_ocr_many[i]
            cands = res_ocr_line['cands']
            cand = cands[0]['char']
            r_line['text'] = cand
            # print(cand, end= ' ')
            # 字检测结果
            len_chars = len(cand)  # 字数
            box_line = r_line['box']
            x1, y1, x2, y2, x3, y3, x4, y4 = box_line = [int(cord) for cord in box_line]
            min_x, max_x = round((x1 + x4) / 2), round((x2 + x3) / 2)
            min_y, max_y = round((y1 + y2) / 2), round((y3 + y4) / 2)
            width_line = abs(max_x - min_x)

            boxes_char = []
            if len_chars > 0:
                h_char = (max_y - min_y) / len_chars
                for j in range(len_chars):
                    box = [
                        min_x, min_y + j * h_char, max_x, min_y + j * h_char,
                        max_x, min_y + (j + 1) * h_char, min_x, min_y + (j + 1) * h_char
                    ]
                    box_char = {
                        'box': [str(round(pt)) for pt in box],
                        'name': j,
                        'text': cand[j]
                    }
                    boxes_char.append(box_char)
                    # print(cand[j], end='')
            r_line['boxes_char'] = boxes_char
            line_size = get_line_size(width_rngs, width_line)
            # r_line['size'] = 'M'
            r_line['size'] = line_size
            # print(line_size)
        #     if line_size == 'M':
        #         M_size.append(cand)
        #     if line_size == 'S':
        #         S_size.append(cand)
        #     if line_size == 'L':
        #         L_size.append(cand)
        #     if line_size == 'XL':
        #         XL_size.append(cand)
        #     if line_size == 'XXL':
        #         XXL_size.append(cand)
        #     if line_size == 'XXXL':
        #         XXXL_size.append(cand)
        # print('XXXL: amount:',len(XXXL_size), XXXL_size)
        # print('XXL: amount:',len(XXL_size), XXL_size)
        # print('XL: amount:',len(XL_size), XL_size)
        # print('L: amount:',len(L_size), L_size)
        # print('M: amount:',len(M_size), M_size)
        # print('S: amount:',len(S_size), S_size)


        re_mapping_lsize(res4api_detect_line)  # line size remapping
        res = res4api_detect_line
        if 'adv' == detector:
            big_subs = concat_res['bigboxes_uboxes']
            # 遍历 big_subs，合并big下面的框 ，并标上大小字标签

            res = adv_res = {
                'res_basic': res4api_detect_line,
                'big_sub_boxes': concat_res['bigboxes_uboxes']
            }
        return res


def recog_jinling(draw=False):
    craft_db = RecogHandler()  # 实例化类
    # print(my_computer.screen)#打印类中的属性值
    dir_path = '/disks/sde/beyoung/files_processor/金陵诗徵44巻_gray_pure'
    # dir_path = '/disks/sde/beyoung/files_processor/OCR测试图像2'
    # test_one = '/disks/sde/beyoung/files_processor/金陵诗徵44巻_gray_pure/金陵诗徵44巻_2624.jpg'
    files = os.listdir(dir_path)
    AttributeError_pics = []
    otherError_pics = []
    num = 0
    strart_time = time.time()
    for file in files:
        if file.endswith('.jpg'):
            num += 1
            if not os.path.exists(os.path.join(dir_path, 'output', file[:-4] + '.txt')):
                try:
                    img_test = readPILImg(os.path.join(dir_path, file))
                    craft_db.ocr_page(img_test, 'adv')  # 启动类中的方法
                except:
                    AttributeError_pics.append(file)
                    print(file)
        if draw:
            ajust_boxes(img_test, dbg=False)
            end_time = time.time()
            used_time = end_time - strart_time
            rest_time = used_time / num * (len(files) - num)
            print(str(round(num / len(files) * 100, 2)) + '% rest_time: ', rest_time)

    print('AttributeError_pics:\n', AttributeError_pics)


# img_test = readPILImg(test_one)
# craft_db.ocr_page(img_test,'adv')#启动类中的方法

def recog_more_class():
    craft_db = RecogHandler()  # 实例化类
    dir_path = '/disks/sde/beyoung/files_processor/OCR测试图像2'
    # test_one = '/disks/sde/beyoung/files_processor/金陵诗徵44巻_gray_pure/金陵诗徵44巻_2624.jpg'
    dirs = os.listdir(dir_path)
    # print(dirs)
    AttributeError_pics = []
    otherError_pics = []
    num = 0
    strart_time = time.time()
    for dir in dirs:
        # print(dir)
        if os.path.isdir(os.path.join(dir_path, dir)):
            if not dir == 'output':
                files = os.listdir(os.path.join(dir_path, dir))
                # print(files)
                for file in files:
                    if os.path.splitext(file)[1].lower() in IMG_EXT:
                        num += 1
                        # if not os.path.exists(os.path.join(dir_path, dir, 'output', file[:-4] + '.txt')):
                        try:
                            img_test = readPILImg(os.path.join(dir_path, dir, file))
                            craft_db.ocr_page(img_test, 'adv')  # 启动类中的方法
                        except:
                            AttributeError_pics.append(file)
                            print(file)
                        end_time = time.time()
                        used_time = end_time - strart_time
                        rest_time = used_time / num * (len(files) - num)
                        print(str(round(num / len(files) * 100, 2)) + '% rest_time: ', rest_time)

    print('AttributeError_pics:\n', AttributeError_pics)

if __name__ == '__main__':

    # test_one_pic()
    #
    craft_db = RecogHandler()
    # file = '/disks/sde/beyoung/files_processor/OCR测试图像2/论语注疏（常见经典，大小字夹杂）/ZHSY003345-000020.tif'
    # file = '/disks/sde/beyoung/files_processor/OCR测试图像2/吕氏家塾（常见经典，大小字）/ZHSY003347-000008.tif'
    file = '/disks/sde/beyoung/files_processor/OCR测试图像2/春秋经传集解(页面有些杂质干扰，有大小字）/ZHSY003341-000011.tif'
    # file = '/disks/sde/beyoung/files_processor/OCR测试图像2/史记（经典中的经典）/史记1.jpg'
    img_test = readPILImg(file)
    res = craft_db.ocr_page(img_test, 'adv')  # 启动类中的方法
    y = list(res.values())
    # print(y[0])
    for i in y[0]:
        yy = list(i.values())
        # for yy in i.key
        # print(yy[2])
        # output_path = dir_path + '/output'
        # if not os.path.exists(output_path):
        #     os.mkdir(output_path)
        # with open(os.path.join(output_path, file[:-4] + '.txt'), 'a') as output_file:
        #     output_file.write(yy[2] + '\n')

    # # def recog_jinling():
    # craft_db = RecogHandler()  # 实例化类
    # # print(my_computer.screen)#打印类中的属性值
    # dir_path = '/disks/sde/beyoung/files_processor/宝庆'
    # # dir_path = '/disks/sde/beyoung/files_processor/OCR测试图像2'
    # # test_one = '/disks/sde/beyoung/files_processor/金陵诗徵44巻_gray_pure/金陵诗徵44巻_2624.jpg'
    # files = os.listdir(dir_path)
    # AttributeError_pics = []
    # otherError_pics = []
    # num = 0
    # strart_time = time.time()
    # for file in files:
    #     if file.endswith('.jpg'):
    #         num += 1
    #         if not os.path.exists(os.path.join(dir_path, 'output', file[:-4] + '.txt')):
    #             # try:
    #             img_test = readPILImg(os.path.join(dir_path, file))
    #             craft_db.ocr_page(img_test, 'adv')  # 启动类中的方法
    #             # except:
    #             #     AttributeError_pics.append(file)
    #             #     print(file)
    #         end_time = time.time()
    #         used_time = end_time - strart_time
    #         rest_time = used_time / num * (len(files) - num)
    #         print(str(round(num / len(files) * 100, 2)) + '% rest_time: ', rest_time)
    #
    # print('AttributeError_pics:\n', AttributeError_pics)

