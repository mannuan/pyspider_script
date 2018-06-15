# -*- coding:utf-8 -*-

import requests

url = 'http://127.0.0.1:5000/run'
d = {'project':'test111'}
r = requests.post(url,data=d)
print r.text
