# -*- coding: utf-8 -*-
# @Time   : 2021/5/21 17:27
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : rm_blank.py

txt = '2015年《中国制造2025》发布以来,我国人工 智 能 产业进入快速发展阶段。2016年5月,《“互联网+”人工智能三年行动实施方案》提出我国人工智能产业在2018年要达到千亿元规模。2017年7月,国务院进一 步印发《新一代人工智能发展规划》,对我国人工智能发展作出“三步走”战略部署,让我国人工智能理论、技 术 和 应 用 在 2030 年 总 体 达 到 世 界 领 先 水 平 。2018 年 1 月 ,《人 工 智 能 标 准 化 白 皮 书 (2018 版 )》正 式 发 布 ,宣 布 成立国家人工智能标准化总体组,推行我国人工智能 标准化工作。这一系列相关政策的发布与实施不仅将 我国人工智能发展上升为国家战略,而且进一步推动 了我国人工智能产业健康快速发展。'
txt = txt.replace(' ', '')
print(txt)