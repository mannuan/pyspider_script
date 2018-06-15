#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project:

from pyspider.libs.base_handler import *
import time,pymysql,sys

conn = pymysql.connect(host='10.1.17.25', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
cur = conn.cursor()
try:
    sql = 'select note_id from invitation where source = \'微博\''
    cur.execute(sql)
    rows = cur.fetchall()
    # for row in rows:
    #     print row[0]
    # print len(rows)
    sql = 'UPDATE `invitation` SET `type_id`=\'0\' WHERE `note_id`=%s;'
    cur.executemany(sql,rows)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
# 释放数据连接
if cur:
    cur.close()
if conn:
    conn.close()