#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from function import getData, getURLPaint

url = 'https://sonnha.dep.asia/son-mykolor/'
tagName = 'table'
className = ''
result = getData(url, tagName, className)
# print(result)

url_paint_list = getURLPaint(result)[:1]
list_url = ""
start_point = 'https://sonnha.dep.asia'

for url in url_paint_list:
    urlPaint = start_point + url["href"]
    print(urlPaint)
    tagName = 'div'
    className = 'post-content box mark-links entry-content'
    rs = getData(urlPaint, tagName, className)
    print('----------\n', rs, '\n----------\n')

    a_list = getURLPaint(rs)[:10]

    for paint in a_list:
        print('ABC----------\n', paint, '\n----------\n')

``