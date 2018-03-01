#!/usr/bin/env python
#encoding: utf-8
'''
#Created by PyCharm
#User: Zongxj
#Date: 2018/2/26 
#Time: 14:35
'''
import re

import urllib.parse
from bs4 import BeautifulSoup

class HtmlParser(object):

    def get_new_urls(self, page_url, soup):
        new_urls = set ()
        # https://baike.baidu.com/item/PyCharm/8143824
        links = soup.find_all('a',href=re.compile(r"/item/(.*?)") )
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls

    def get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>TextMate</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, "html.parser")
        #print(soup)
        new_urls = self.get_new_urls(page_url,soup)
        #print(new_urls)
        new_data = self.get_new_data(page_url,soup)
        #print(new_data)
        return new_urls,new_data
