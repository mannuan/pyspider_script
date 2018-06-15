# -*- coding:utf-8 -*-

from lxml import html
import requests,pymysql
import json
import re

#正则表达式的元字符 . * ?
# class Tool:
#     #去除img标签
#     removeImg = re.compile('<img.*>| {1,7}|&nbsp;')
#     #去除超链接 a标签
#     removeAddr = re.compile('<a.*?>|</a>')
#     #把换行换成\n
#     replaceLine = re.compile('<tr>|<div>|</div>|</p>')
#
#     #去除所有标签
#     removeTag = re.compile('<.*?>')
#
#     @classmethod
#     def replace(cls,x):
#         x = re.sub(cls.removeImg,'',x)
#         x = re.sub(cls.removeAddr,'',x)
#         x = re.sub(cls.replaceLine,'',x)
#         x = re.sub(cls.removeTag,'',x)
#
#         return x.strip()#去掉多余的内容

url = 'https://m.dianping.com/isoapi/module'
headers = {
# 'Host':'m.dianping.com',
# 'Connection': 'keep-alive',
# 'Content-Length': '164',
# 'Origin': 'https://m.dianping.com',
# 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53',
'Content-Type': 'application/json; charset=utf-8',
# 'Accept': '*/*',
# 'Referer': 'https://m.dianping.com/shop/19595161/review_all',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Cookie': '_lxsdk_cuid=15fe3fc3ed0c8-026fd89dad80db-1f2a1709-1aeaa0-15fe3fc3ed0c8; _lxsdk=15fe3fc3ed0c8-026fd89dad80db-1f2a1709-1aeaa0-15fe3fc3ed0c8; _hc.v=5e7e0724-a23e-9959-4d71-7e62c30bcd1f.1511358480; __mta=55958036.1512546479523.1512546479523.1512546479523.1; switchcityflashtoast=1; _dp.ac.v=e0096bdb-f7b6-495b-8c97-3c7e48a732cb; dper=0c98df72d34b20bdc9d46a1872710ee5cdf90328c62ae1dd54bda9ede4f17ea5; ua=dpuser_0198477750; ctu=6f5c321e57fb5447cae079cc45db42fe86be844db21774a18318126fc97a76d3; s_ViewType=10; aburl=1; cye=tonglu; _tr.u=RT0Br2n4dszzVm6n; _tr.s=JlE31vWZGsvCjCKU; appname=dp_m; __mta=55958036.1512546479523.1512546479523.1512614513790.2; cy=3; default_ab=citylist%3AA%3A1%7Cshop%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cshopreviewlist%3AA%3A1; m_flash2=1; cityid=3; chwlsource=baidusearch; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic%26utm_term%3D%25E5%25A4%25A7%25E4%25BC%2597%25E7%2582%25B9%25E8%25AF%2584; _lxsdk_s=1602f92c457-bde-cd9-2fc%7C%7C33; msource=baidusearch; baidusearch_ab=shop.sql%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cshopreviewlist%3AA%3A1',
}
data = {"moduleInfoList":[{"moduleName":"pageInitData","query":{"shopId":"63263234"}}],"pageEnName":"pageInitData"}
reponse = requests.post(url,headers=headers,data=json.dumps(data))
print(reponse.text)
# ob_json = json.loads(reponse.text)
# list_cards = ob_json.get('cards')
# for card in list_cards:
#     if card.get('card_type') == 9:
#         text = card.get('mblog').get('text')
#         text = Tool.replace(text)  # 微博的内容
#         print text
#         print '===================================='