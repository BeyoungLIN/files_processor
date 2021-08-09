# -*- coding: utf-8 -*-
# @Time   : 2021/8/9 14:08
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : acocr_postprocessor.py

import os

def tag_convert2xml(input_path, output_path = '', mod = 'normal'):
    flag = 1
    contents = ''
    with open (input_path, 'r', encoding='utf-8') as f:
        # a = f.read()
        # b = f.readline()
        lines = f.readlines()
    for line in lines:
        line = line.replace('\n', '')
        content, tag = line.split('\t')[0], line.split('\t')[1]
        # print(tag)
        tag_s = tag.replace('[', '').replace(']', '')
        content_new = '<' + tag_s + '>' + content + '</' + tag_s + '>'
        if flag < len(lines):
            flag += 1
            content_new = content_new + '\n'
        contents = contents + content_new
    print(contents)

    if output_path == '':
        output_path = input_path[:-4] + '_xml.txt'

    with open(output_path,'w', encoding='utf-8') as of:
        of.write(contents)

    return

def getfiles(root, mod = 'singel'):
    files_new = []
    dirs = os.listdir(root)
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        if os.path.isdir(dir_path):
            files = os.listdir(dir_path)
            for file in files:
                file_path = os.path.join(dir_path, file)
                if file.endswith('_recog_adv.txt'):
                    files_new.append(file_path)
    #
    # for curDir, dirs, files in os.walk(root):
    #     # print("====================")
    #     # print("现在的目录：" + curDir)
    #     # print("该目录下包含的子目录：" + str(dirs))
    #     # print("该目录下包含的文件：" + str(files))
    #     for file in files:
    #         if file.endswith('_recog_adv.txt'):
    #             files_new.append(os.path.join())
    return files_new




if __name__ == '__main__':
    txt_files = getfiles(r'/Users/Beyoung/Desktop/Projects/AC_OCR/ER007_jpg_res/')
    for txt_file in txt_files:
        dirname, filename = os.path.split(txt_file)
        tag_convert2xml(txt_file, )