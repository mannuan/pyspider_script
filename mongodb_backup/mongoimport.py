# -*- coding:utf-8 -*-
from pymongo import MongoClient
import sys,os,json
reload(sys)
sys.setdefaultencoding('utf8')

file_num = -1
os.chdir('{}/文档/'.format(os.environ['HOME']))
for i in os.listdir('.'):
    if 'mongodb_backup' in i:
        file_num += 1
if file_num >= 0:
    mongodb_folder = 'mongodb_backup_{}'.format(file_num).replace('mongodb_backup_0','mongodb_backup')
    print mongodb_folder
    conn = MongoClient('localhost', 27017)
    os.chdir('{}/文档/{}/'.format(os.environ['HOME'],mongodb_folder))
    db_list = os.listdir('.')
    for i in db_list:
        db_path = '{}/文档/{}/{}'.format(os.environ['HOME'],mongodb_folder,i)
        os.chdir(db_path)
        exec 'db = conn.{}'.format(i)
        collection_list_str = json.dumps(db.collection_names())
        for j in os.listdir('.'):
            import_collection = 'mongoimport --db {} --collection {} --file {}'.format(i,j.split('.')[0],db_path+'/'+j)
            if j.split('.')[0] not in collection_list_str:
                print import_collection
                os.system(import_collection)
            else:
                print '数据库{}-集合{}已经存在,无法导入!!!'.format(i,j.split('.')[0])
else:
    print '要导入的数据文件不存在'