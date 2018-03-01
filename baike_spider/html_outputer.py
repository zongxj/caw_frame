#!/usr/bin/env python
#encoding: utf-8
'''
#Created by PyCharm
#User: Zongxj
#Date: 2018/2/26 
#Time: 14:36
'''
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding="utf-8")
        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta http-equiv="content-type" content="text/html;charset=utf-8">')
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<td>链接地址</td>")
        fout.write("<td>词条标题</td>")
        fout.write("<td>词条简介</td>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")