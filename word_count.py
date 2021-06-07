# -*- coding: utf-8 -*-
# @Time   : 2021/5/14 01:51
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : word_count.py


from collections import Counter

input_path = 'multi_lines.txt'
with open(input_path, 'r') as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    line = line.replace('/disks/sdd/beyoung/Fakepages/chinese_fonts/', '').replace('\n', '').replace(' ', '')
    new_lines.append(line)

dict2 = Counter(new_lines)
sorted_x = sorted(dict2.items(), key=lambda x: x[1], reverse=True)
# print(sorted_x)

for i in sorted_x:
    print(i)
# for key, value in dict2.items():
#     print('{key}:{value}'.format(key=key, value=value))
'''

b=set(new_lines)
c=[]
for i in b:
    c.append([i,new_lines.count(i)])
c.sort(key = lambda x:(x[1], x[0]),reverse = True)
print(c)
'''

'''
#  字典统计
dict = {}
for key in new_lines:
    dict[key] = dict.get(key, 0) + 1
print(dict)
'''
