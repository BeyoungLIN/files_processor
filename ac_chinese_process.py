# -*- coding: utf-8 -*-
# @Time   : 2021/9/8 00:02
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : ac_chinese_process.py

import os
import re,string

sym = '[。（）「」：；！!？『』，、]〔〕1234567890-= 一<>》《{〈〉}·<>．'
# punc = '~`!#$%^&*()_+-=|;:.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}1234567890[。（）「」：；！？『』，、]〔〕-= <>'
punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}﹗【】 〔〕1234567890-=（）「」：；！!？『』，、<>》《{〈〉}·<>．﹑\t”‘ 　qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_\[\]'
# r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n。！，？：「」》]：+'

def remove_sym(txt_file):
    content = ''
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        # for s in sym:
        #     line = line.replace(s, '')
        # line = re.sub(r"[{}]+".format(punc), "", line)
        line_new = re.sub(r"[%s]+" %punc, "", line)
        # print(line_new)
        content += line_new
        # print(line_new)
    print(content)
    return content


# def find_chinese(file):
#     pattern = re.compile(r'[^\u4e00-\u9fd5]')
#     chinese = re.sub(pattern, '', file)
#     return chinese


def combine_all(dir_list, output_dir, output_name):
    all_content = ''
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    err = []
    book_list = []
    file_list =[]
    # 获取当前文件夹中的文件名称列表
    for dir in dir_list:
        filenames = os.listdir(dir)
        # print(filenames)
        for file in filenames:
            file_list.append(os.path.join(dir, file))


    # 打开当前目录下的result.txt文件，如果没有则创建
    # 先遍历文件名
    print(filenames)
    error = 0
    # for i in range(881):
    #     file = filedir + '/hanfei_plain_jt_para' + str(i) + '.txt'
    #     # 遍历单个文件，读取行数
    #     for line in open(file):
    #         print(line)
    #         f.writelines(line)
    for file in file_list:
        # if filename != '.DS_Store' or filename != '.idea':
        if file.endswith('.txt'):
            # if filename != '.DS_Store':
            try:
                # filepath = filedir + '/' + filename
                file_content = remove_sym(file)
                all_content += file_content
                # 遍历单个文件，读取行数
                # for line in open(filepath):
                #     print(line)
                #     f.writelines(line)
                #     book_list.append(filename)
            except:
                error += 1
                err.append(file)
    f = open(os.path.join(output_dir, output_name), 'w')
    f.write(all_content)
    # 关闭文件
    f.close()

    print('error:' + str(error))
    print(err)


def combine_all(dir_list, output_dir, output_name):
    all_content = ''
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    err = []
    book_list = []
    file_list =[]
    # 获取当前文件夹中的文件名称列表
    for dir in dir_list:
        filenames = os.listdir(dir)
        # print(filenames)
        for file in filenames:
            file_list.append(os.path.join(dir, file))


    # 打开当前目录下的result.txt文件，如果没有则创建
    # 先遍历文件名
    print(filenames)
    error = 0
    # for i in range(881):
    #     file = filedir + '/hanfei_plain_jt_para' + str(i) + '.txt'
    #     # 遍历单个文件，读取行数
    #     for line in open(file):
    #         print(line)
    #         f.writelines(line)
    for file in file_list:
        # if filename != '.DS_Store' or filename != '.idea':
        if file.endswith('.txt'):
            # if filename != '.DS_Store':
            try:
                # filepath = filedir + '/' + filename
                # file_content = remove_sym(file)
                content = ''
                with open(file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                for line in lines:
                    content += line
                    # print(line_new)
                # print(content)
                all_content += content
                # 遍历单个文件，读取行数
                # for line in open(filepath):
                #     print(line)
                #     f.writelines(line)
                #     book_list.append(filename)
            except:
                error += 1
                err.append(file)
    f = open(os.path.join(output_dir, output_name), 'w')
    f.write(all_content)
    # 关闭文件
    f.close()

    print('error:' + str(error))
    print(err)


if __name__ == '__main__':
    # 获取目标文件夹的路径
    # filedir = '/Users/Beyoung/Desktop/Projects/论文相关代码/BERT_for_SBD_CWS/output'
    # filedir = '/Users/Beyoung/Desktop/Projects/corpus/语料1'
    # filedir = '/Users/Beyoung/Desktop/Projects/corpus/corpus_2'
    dir_list = [
        # '/home/euphoria/deep-text-recognition-benchmark/dataset/DingXiu_train_output/gts/'
        '/Users/Beyoung/Desktop/Projects/corpus/corpus_2',
        '/Users/Beyoung/Desktop/Projects/corpus/语料1',
        # '/Users/Beyoung/Desktop/Projects/corpus/zh',
    ]
    # output_dir = '/home/euphoria/deep-text-recognition-benchmark/dataset/Dingxiu_clean/'
    output_dir = '/Users/Beyoung/Desktop/Projects/corpus/combine_0908'
    # output_name = 'train_combine.txt'
    output_name = 'train_cor1+2.txt'
    combine_all(dir_list, output_dir, output_name)
