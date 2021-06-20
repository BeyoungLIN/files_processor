# -*- coding: utf-8 -*-
# @Time   : 2021/6/20 23:11
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : combine_excels.py

import xlrd
from xlwt import *
import xlwt
from xlutils.copy import copy
import os.path

# dir = input("输入文件路径\n");
dir = '/Users/Beyoung/Library/Mobile Documents/com~apple~CloudDocs/20软微/党团公务/党课推优汇总'
# start_row = input("输入需要读取起始行号\n");
# start_row = int(start_row)
start_row = 1
# end_row = input("输入结束行,输入0表示有内容的最后一行\n")
# end_row = int(end_row)
end_row = 0
all_file = []


def min_s(a, b):
    if a == 0:
        return b
    if (a > b):
        return b
    else:
        return a


for parent, folder, filename in os.walk(dir):
    for file, x in zip(filename, range(len(filename))):
        file = os.path.join(parent, filename[x])
        print(filename[x])
        all_file.append(file)
print("\n文件总数：", len(all_file))
if os.path.exists("result.xlsx"):
    os.remove("result.xlsx")
w = xlwt.Workbook()
row = 0
ws = w.add_sheet('sheet1', cell_overwrite_ok=True)
style = XFStyle()
fnt = Font()
fnt.height = 240
fnt.name = u'宋体'
style.font = fnt
align = Alignment()
align.horz = 2
style.alignment = align
for single_file_path in all_file:
    data = xlrd.open_workbook(single_file_path)
    sheet = data.sheet_by_index(0)
    if sheet.nrows >= start_row:
        for i in range(start_row - 1, min_s(end_row, sheet.nrows)):
            list = sheet.row_values(i)
            for col in range(0, len(list)):
                ws.write(row, col, list[col], style)
            row = row + 1
    else:
        print("非法填写的表格名称:" + single_file_path)

print("运行结束，结果保存在result.xls文件里\n")
print("对于日期，可将对应单元格设置为为日期格式便可正确显示\n"
      "对于超长数字例如身份证号码，设置为文本格式即可\n")
w.save('result.xls')
os.system("pause")