# -*- coding:utf-8 -*-

import requests
from pyquery import PyQuery as pq

p = pq('http://f.wanfangdata.com.cn/download/Periodical_zhonggsl201702007.aspx')
fileurl = 'http://f.wanfangdata.com.cn/'+p('#doDownload').attr.href
filename = "/home/mininet/zhonggsl201702007.pdf"
res = requests.get(fileurl)
with open(filename, 'wb+') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)
    f.close()