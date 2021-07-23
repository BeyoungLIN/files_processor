# -*- coding: utf-8 -*-
# @Time   : 2021/6/22 00:35
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : extract_json.py

import os
import re
import time


def read_json_2txt(json, txt=None):
    with open(json, 'r') as json_file:
        content = json_file.read()

    pattern = re.compile(r'"text": "(.*)",\n')
    result = pattern.findall(content)

    if not txt:
        txt = json[:-9] + '.txt'
        # print(txt)
    content_txt = []

    for line in result:
        line_new = line + '\n'
        content_txt.append(line_new)

    with open(txt, 'w') as txt_file:
        txt_file.writelines(content_txt)


if __name__ == '__main__':
    # read_json_2txt('/disks/sde/beyoung/files_processor/6060.凤岗李氏宗谱[桐庐]_rectify_res/6060.凤岗李氏宗谱[桐庐]_2_rectify_resapi_mix.json.txt')
    root_list = [
        # '/disks/sdd/beyoung/data/國家圖書館藏敦煌遺書_001',
        # '/disks/sdd/beyoung/data/2563[函368]',
        # '/disks/sdd/beyoung/data/纂図互註荀子3',
        # '/disks/sdd/beyoung/data/测试7.5',
        # '/disks/sde/beyoung/files_processor/6059.桐南凤岗李氏宗谱：三十二卷：[桐庐]',
    ]

    for root in root_list:
        start_time = time.time()
        source_path = os.path.join(root, 'output')
        files = os.listdir(source_path)
        target_path = root + '_res'
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        for file in files:
            if file.endswith('_mix.json.txt'):
                read_json_2txt(os.path.join(source_path, file))
                os.system('cp ' + os.path.join(source_path, file[:-9] + '.txt') + ' ' + os.path.join(target_path, file[
                                                                                                                  :-9] + '.txt'))
                os.system('cp ' + os.path.join(source_path, file) + ' ' + os.path.join(target_path, file))
        end_time = time.time()
        used_time = end_time - start_time
        print(root + '\n处理时间', used_time)

read_json_2txt('/Users/Beyoung/Desktop/Projects/ER/dataset/ER007/20_19584_jpg/output/000010_resapi_mix.json.txt')
