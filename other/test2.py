#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:27:29 2017

@author: mininet
"""

import urllib, random, sys, re, time

"""
此函数用于抓取返回403禁止访问的网页
"""
headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"]
random_header = random.choice(headers)
start_url = "https://mmbiz.qpic.cn/mmbiz_jpg/qJickicXOV5OGsAwcl6tOsHF0BdU4YWO7GDnlEbjKMy4o0ayfPI8WCRIej6yd19R2Nch1NUEhy9QUqRG02fgpDpA/640?wx_fmt=jpeg&tp=jpg&wxfrom=5&wx_lazy=1"

req = urllib.Request(start_url)
req.add_header("User-Agent", random_header)
req.add_header("GET", start_url)
content = urllib.urlopen(req).read()
f = open('temp.jpg', 'wb+')
f.write(content)
f.close()