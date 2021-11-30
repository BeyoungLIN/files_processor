# 简介

本仓库主要包含了一些日常数据处理所需要的程序,可视为一个程序练习集,会在一定时间后对相关程序功能进行整理完善

## 一些程序的用途
* 检测纯黑图片.py
可以检测图片是否由纯正的黑色组成

* pic_format_convert.py
一些图片格式的相互转换

* text_diff_1.py
检测两个文件的文字是否存在差别, 结果以html格式返回

* open_urls.py
批量打开各种url

* progress_bar.py
实现进度条可视化效果

* cv_operation.py
一些使用open_cv的图片操作,如对比度之类的

## some errors records
1. 
```
type object 'RFPDupeFilter' has no attribute 'from_spider'
```

 scrapy-redis 版本的问题,之前安装的 0.7.1报错,`pip install scrapy-redis==0.6.8` 后解决