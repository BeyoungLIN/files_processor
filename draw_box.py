# -*- coding: utf-8 -*-
# @Time   : 2021/7/11 16:42
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : draw_box.py

from PIL import Image, ImageDraw

boxes = \
    [
        1397, 41, 1429, 42, 1400, 971, 1369, 970,
        1342, 39, 1373, 40, 1344, 970, 1312, 969,
        1285, 35, 1319, 36, 1291, 967, 1256, 966,
        1231, 36, 1262, 37, 1233, 966, 1201, 965,
        1174, 33, 1209, 34, 1178, 962, 1143, 961,
        1118, 28, 1154, 29, 1128, 961, 1093, 960,
        1059, 20, 1105, 22, 1097, 192, 1051, 189,
        1015, 25, 1047, 26, 1016, 954, 984, 953,
        958, 23, 989, 24, 960, 957, 930, 956,
        904, 23, 936, 24, 909, 864, 877, 863,
        851, 21, 883, 22, 852, 951, 820, 950,
        763, 945, 796, 18, 828, 20, 795, 946,
        724, 87, 780, 87, 780, 143, 724, 143,
        718, 256, 774, 256, 774, 401, 718, 40,
        704, 689, 761, 689, 761, 742, 704, 742,
        681, 13, 717, 14, 685, 941, 650, 939,
        627, 13, 657, 14, 627, 938, 597, 937,
        573, 10, 608, 12, 576, 933, 540, 931,
        517, 10, 549, 11, 519, 931, 487, 930,
        464, 9, 496, 10, 465, 931, 433, 930,
        410, 6, 442, 7, 412, 924, 380, 923,
        353, 5, 388, 6, 358, 924, 323, 923,
        298, 5, 332, 6, 302, 922, 268, 921,
        242, 4, 278, 5, 247, 919, 211, 918,
        189, 6, 221, 7, 190, 916, 158, 915,
        134, 6, 166, 7, 134, 916, 103, 915,
        76, 6, 111, 8, 82, 912, 46, 911,

    ]

pic_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/temp/WechatIMG618.png'
im = Image.open(pic_path)
draw = ImageDraw.Draw(im)
box_path = '/Users/Beyoung/Desktop/Projects/AC_OCR/temp/000008.txt'
# with open(box_path, 'r', encoding='UTF-8') as b:
#     boxes = b.readlines()
#     b.close()
# print(boxes)
# numbers = list(map(int, boxes))
# print(numbers)
n = 8
for box in [boxes[i:i + n] for i in range(0, len(boxes), n)]:
# for box in boxes:
    # box = box.replace('\n', '')
    box.append(box[0])
    box.append(box[1])
    print(box)
    draw.line(box, width=4, fill=255)
print('OK')
im.save(pic_path[:-4] + '_draw_box.png')
