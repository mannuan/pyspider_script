# -*- coding:utf-8 -*-

from pymongo import MongoClient
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

conn = MongoClient('localhost', 27017)
comment_sum = 0
for i in conn.database_names():
    exec 'db = conn.{}'.format(i)
    comment_sum += db.comments.count()
print comment_sum