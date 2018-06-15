# -*- coding:utf-8 -*-

from lxml import html
import requests,pymysql
import json
import re

#正则表达式的元字符 . * ?
class Tool:
    #去除img标签
    removeImg = re.compile('<img.*>| {1,7}|&nbsp;')
    #去除超链接 a标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行换成\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')

    #去除所有标签
    removeTag = re.compile('<.*?>')

    @classmethod
    def replace(cls,x):
        x = re.sub(cls.removeImg,'',x)
        x = re.sub(cls.removeAddr,'',x)
        x = re.sub(cls.replaceLine,'',x)
        x = re.sub(cls.removeTag,'',x)

        return x.strip()#去掉多余的内容

url = 'https://m.weibo.cn/api/container/getIndex?uid=5488087569&type=uid&value=5488087569&containerid=1076035488087569&page=1'
reponse = requests.get(url)
ob_json = json.loads(reponse.text)
list_cards = ob_json.get('cards')
for card in list_cards:
    if card.get('card_type') == 9:
        text = card.get('mblog').get('text')
        text = Tool.replace(text)  # 微博的内容
        print text
        print '===================================='