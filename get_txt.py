# -*- coding: utf-8 -*-
# @Time   : 2023/5/27 17:21
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : get_txt.py

import os, json
from tqdm import tqdm

def main():
    json_ls = []
    folder_pth = '/disks/sdc/beyoung/corpus/清人笔记_res'
    name_ls = os.listdir(folder_pth)
    for n in name_ls:
        if n.endswith('.json'):
            json_ls.append(os.path.join(folder_pth, n))
    for j in tqdm(json_ls):
        with open(j, 'r', encoding='utf-8') as f:
            js_content = json.loads(f.read())
        txt = '\n'.join(js_content['txt'])
        # print(txt)
        name = j.replace('.json', '.txt')
        with open(name, 'w') as f:
            f.write(txt)
    return


if __name__ == '__main__':
    main()
