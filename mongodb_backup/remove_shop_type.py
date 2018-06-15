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
shops.remove({'shop_type':'景点'})
