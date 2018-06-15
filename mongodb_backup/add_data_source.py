# -*- coding:utf-8 -*-

from pymongo import MongoClient
import sys,os,json
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo.cursor import Cursor

conn = MongoClient('localhost', 27017)
db = conn.xiecheng_qiandaohu
shops = db.shops
comments = db.comments
item_count = 0
for i in shops.find({'data_source':'景点'}):
    for j in comments.find({'shop_id':i.get('shop_id')}):
        j.pop('_id')
        k = j.copy()
        j.setdefault('data_source','景点')
        comments.update(k, {"$set": j})