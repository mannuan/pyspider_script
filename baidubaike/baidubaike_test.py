# -*- coding:utf-8 -*-

import urllib2,random,sys,re,time,json,requests
reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://wapbaike.baidu.com/item/丁栅港'
response = requests.get(url)
print response.text