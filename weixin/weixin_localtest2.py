# -*- coding:utf-8 -*-

import requests,json,re,random

with open('cookies.txt','r') as file:
    cookie = file.read()
cookies = json.loads(cookie)

url = 'https://mp.weixin.qq.com'

response = requests.get(url,cookies=cookies)
token = re.findall(r'token=(\d+)',str(response.url))[0]

print token
headers={}
query = 'python'
data = {'token':'350204239','lang':'zh_CN','f':'json','ajax':'1','random':random.random(),
        'url':query,'begin':'0','count':'3'}
search_url = ''
search_response = requests.post(search_url,cookies=cookies)

print search_response.text