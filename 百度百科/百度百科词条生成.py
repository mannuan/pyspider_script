# -*- coding:utf-8 -*-
import pymysql,json

with open('/home/mininet/河流名称列表.txt','r') as f:
    river_list = json.loads(f.read())
entry_list = []
for river in river_list:
    entry = [river.encode('utf-8'),'http://baike.baidu.com/item/{}'.format(river.encode('utf-8'))]
    entry_list.append(entry)
conn = pymysql.connect(host='10.1.17.25', port=3306, user='repository', passwd='repository', db='repository', charset='utf8')
cur = conn.cursor()
cur.executemany("insert into baidubaike_entry(name,url) values(%s,%s)",entry_list)
# rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()