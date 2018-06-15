# -*- coding:utf-8 -*-
from pymongo import MongoClient
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

conn = MongoClient('localhost', 27017)
mongodb_folder = 'mongodb_backup'
file_num = 0
if os.path.exists('{}/文档/mongodb_backup/'.format(os.environ['HOME'])):
    os.chdir('{}/文档/'.format(os.environ['HOME']))
    for i in os.listdir('.'):
        if 'mongodb_backup' in i:
            file_num += 1
if file_num > 0:
    mongodb_folder = 'mongodb_backup_{}'.format(file_num)
qiandaohu_mongodb_list = conn.database_names()
for i in qiandaohu_mongodb_list:
    if 'local' not in i:
        exec 'db = conn.{}'.format(i)
        for j in db.collection_names():
            export_collection = 'mongoexport --db {} --collection {} --out /home/mininet/文档/{}/{}/{}.json'.format(i,j,mongodb_folder,i,j)
            print export_collection
            os.system(export_collection)
