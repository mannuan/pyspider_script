# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
cur = conn.cursor()
cur.execute('select id from invitation where note_id = %s','4186950363819968')
trend_id = cur.fetchone()[0]
print trend_id
# 释放数据连接
if cur:
    cur.close()
if conn:
    conn.close()