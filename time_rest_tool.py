# -*- coding: utf-8 -*-
# @Time   : 2021/11/11 09:34
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : time_rest_tool.py

import time


def time_change(time_init):  # 定义将秒转换为时分秒格式的函数
    time_list = []
    if time_init / 3600 > 1:
        time_h = int(time_init / 3600)
        time_m = int((time_init - time_h * 3600) / 60)
        time_s = int(time_init - time_h * 3600 - time_m * 60)
        time_list.append(str(time_h))
        time_list.append('h ')
        time_list.append(str(time_m))
        time_list.append('m ')

    elif time_init / 60 > 1:
        time_m = int(time_init / 60)
        time_s = int(time_init - time_m * 60)
        time_list.append(str(time_m))
        time_list.append('m ')
    else:
        time_s = int(time_init)

    time_list.append(str(time_s))
    time_list.append('s')
    time_str = ''.join(time_list)
    return time_str


if __name__ == "__main__":
    process = .0
    start = time.time()
    total_num = 5  # edit needed
    for i in range(total_num):

        '''
        code here
        
        '''

        if process < (i * 1.0 / total_num):
            if process != 0:
                end = time.time()
                use_time = end - start
                all_time = use_time / process
                res_time = all_time - use_time
                str_ues_time = time_change(use_time)
                str_res_time = time_change(res_time)

                print("Percentage of progress:%.0f%%   Used time:%s   Rest time:%s " % (process * 100, str_ues_time, str_res_time))
            process = process + 0.01
