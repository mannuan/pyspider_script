# -*- coding:utf-8 -*-

import re,sys,time
# from pymongo import MongoClient
#
# MONGODB_PORT = 27017
# MONGODB_IP = 'localhost'
# CONN = MongoClient(MONGODB_IP, MONGODB_PORT)
# MONGODB = CONN.dspider2
# shops = MONGODB.shops
# comments = MONGODB.comments
#
# key = {'data_website':"飞猪",'data_source':"景点",'data_region':"千岛湖",'shop_name':"千岛湖中心湖区"}
#
# print comments.find(key).count()

b = dict({'a':1}, **{})
print b.has_key('b')
print b