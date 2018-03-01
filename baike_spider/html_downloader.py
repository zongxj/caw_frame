#!/usr/bin/env python
#encoding: utf-8
'''
#Created by PyCharm
#User: Zongxj
#Date: 2018/2/26 
#Time: 14:35
'''
import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read().decode("utf-8")