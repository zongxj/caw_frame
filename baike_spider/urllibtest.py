#!/usr/bin/env python
#encoding: utf-8
'''
#Created by PyCharm
#User: Zongxj
#Date: 2018/2/27 
#Time: 12:40
'''
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.getcode())
