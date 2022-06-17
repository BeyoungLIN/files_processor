# -*- coding: utf-8 -*-
# @Time   : 2022/6/16 20:32
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : niuke_6.py

import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
	'''
	此函数用于获取网页的html文档
	'''
	try:
		#获取服务器的响应内容，并设置最大请求时间为6秒
		res = requests.get(url, timeout = 6)
		#判断返回状态码是否为200
		res.raise_for_status()
		#设置该html文档可能的编码
		res.encoding = res.apparent_encoding
		#返回网页HTML代码
		return res.text
	except:
		return '产生异常'

def main():
	'''
	主函数
	'''
	#目标网页，这个可以换成一个你喜欢的网站
	url = 'https://www.nowcoder.com/search?type=post&query=%E6%9C%9D%E5%A4%95%E5%85%89%E5%B9%B4'

	demo = getHTMLText(url)
	print(demo)
	#解析HTML代码
	soup = BeautifulSoup(demo, 'html.parser')
	# soup = BeautifulSoup(html, 'html.parser')

	#模糊搜索HTML代码的所有包含href属性的<a>标签
	a_labels = soup.find_all('a', attrs={'href': True})

	#获取所有<a>标签中的href对应的值，即超链接
	for a in a_labels:
		if a:
			if a.startswith('/discuss/') and ('tag' not in a):
				print(a.get('href'))

main()