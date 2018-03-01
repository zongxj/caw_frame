#!/usr/bin/env python
# encoding: utf-8
'''
#Created by PyCharm
#User: Zongxj
#Date: 2018/2/26 
#Time: 14:30
'''
# 从baike_spider包中，
# 导入模块
# url_manager（URL管理器）,
# html_downloader（HTML下载器）,
# html_parser（HTML解析器）,
# html_outputer（HTML输出器），
from baike_spider import url_manager, html_downloader, html_parser, html_outputer

# 创建SpierMain类
class SpiderMain(object):
    # 构造函数初始化
    def __init__(self):
        # urls(对象)作为url管理器
        self.urls =url_manager.UrlManager()
        # downloader(对象)作为html下载器
        self.downloader = html_downloader.HtmlDownloader()
        # parser(对象)作为html解析器
        self.parser = html_parser.HtmlParser()
        # outputer(对象)作为html输出器
        self.outputer = html_outputer.HtmlOutputer()

    # carw方法，爬虫的调度程序
    def craw(self, root_url):
        # 将初始url添加进url管理器
        self.urls.add_new_url(root_url)
        # 初始变量
        count = 1
        # 当url管理器中有待爬取的url时，
        while self.urls.has_new_url():
            # try判断循环
            try:
                # 从url管理器中，获取一个url
                new_url = self.urls.get_new_url()
                # 启动html下载器，下载html页面
                html_cont = self.downloader.download(new_url)
                # print(html_cont)
                # 调用html解析器，解析出url和data（new_urls,new_data），传入2个参数当前下载的url（new_url）,已下载的页面(html_cont)
                new_urls, new_data = self.parser.parser(new_url,html_cont)
                # 将解析出的url传入url管理器
                self.urls.add_new_urls(new_urls)
                # 将解析出的data传入html输出器
                print(new_data)
                self.outputer.collect_data(new_data)
                #循环1000次
                if count == 10:
                    break
                count = count + 1
            # 抛出异常
            except:
                print('craw failed')

        # 输出html页面
        self.outputer.output_html()

if __name__ == '__main__':
    # 爬取初始url
    root_url = "https://baike.baidu.com/item/PyCharm/8143824"
    # 调用SpiderMain类
    obj_spider = SpiderMain()
    # 使用SpiderMain类中的craw方法启动爬虫
    obj_spider.craw(root_url)
