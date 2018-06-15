# -*- coding:utf-8 -*-

from pymongo import MongoClient
import sys,os,json
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo.cursor import Cursor

conn = MongoClient('localhost', 27017)
db = conn.xiecheng_dspider
shops = db.shops
comments = db.comments
item_count = 0
for i in comments.find():
    print i.get('crawl_time')
    i.pop('_id')
    k = i.copy()
    i.setdefault('data_region','千岛湖')
    i.setdefault('data_website', '携程')
    comments.update({'shop_url':k.get('shop_url')}, {"$set": i})