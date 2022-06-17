import requests
from lxml import etree
from multiprocessing.dummy import Pool


def parse(dic):
    """请求并解析数据"""
    # 得到目标url
    url = dic.get('url')
    # UA伪装
    headers = dic.get('headers')
    # 得到文件句柄
    f = dic.get('f')

    # 获取页面的源码数据
    page_text = requests.get(url=url, headers=headers).text
    # 标签定位
    tree = etree.HTML(page_text)
    # 定位到所有的li标签
    li_list = tree.xpath('//div[@class="module-body"]/ul/li')

    # 获取模块的名称  有些模块名不在一个地方
    try:
        model_name = tree.xpath('//div[@class="discuss-tab-wrap"]/a[@class="discuss-tab selected"]/text() ')[0]
    except IndexError:
        model_name = tree.xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/ul/li[2]/a/text()')[0]

    # 遍历每一个帖子
    for li in li_list:
        try:
            title = li.xpath('./div/div[1]/a[1]/text() | ./div[2]/div[1]/a/text() ')[0]  # 标题
            num = li.xpath('./div/div[2]/div[2]/span[5]/span/text()')[0]  # 浏览量
            up = li.xpath('./div/div[2]/div[2]/span[3]/span/text()')[0]  # 点赞量
            content_num = li.xpath('./ div / div[2] / div[2] / span[1] / span/text()')[0]  # 回帖数
            # 以不同方式写入文件 看你想要什么
            f.write(title + '  浏览量' + str(num) + '  点赞量' + str(up) + '  评论数' + str(content_num))
            # f.write(title+model_name)
            # f.write(title)
        except IndexError:
            continue


if __name__ == '__main__':
    # 所要爬取的目标网址
    url = 'https://www.nowcoder.com/discuss?type=0&order=0'

    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    # 创建要写入的目标文件
    with open('../面试相关/朝夕观念_all.txt', 'w', encoding='utf-8') as f:
        pool = Pool(10)
        page_num = 1
        urls = []

        # 遍历所有的模块
        for i in range(13):
            # 每一次遍历新模块时，从第一页开始
            page_num = 1
            # 遍历所有的页面
            while page_num <= 100:
                # new_url = 'https://www.nowcoder.com/discuss?type=%s&order=4&pageSize=30&expTag=0&page=%s'
                new_url = 'https://www.nowcoder.com/search?type=post&order=recall&query=%E6%9C%9D%E5%A4%95%E5%85%89%E5%B9%B4&subType=0&tagId=&page=%s'
                url = format(new_url % (i, page_num))
                print(url)
                # 线程池就是这么玩的 传入字典 固定格式
                dic = {
                    'url': url,
                    'headers': headers,
                    'f': f  # 文件句柄
                }
                urls.append(dic)
                # 每一次循环页码+1
                page_num += 1

        # 将urls中的每个元素 传给parse函数执行
        pool.map(parse, urls)
        # 关闭线程池
        pool.close()
        # 等待主进程结束
        pool.join()