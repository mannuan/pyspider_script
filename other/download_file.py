# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
cur = conn.cursor()
try:
    cur.execute("select file_name,file_url from website where file_url like '%.%'")
    rows = cur.fetchall()
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
if cur:
    cur.close()
if conn:
    conn.close()
import os,requests
for row in rows:
    file_name = os.getcwd()+'/website_document/'+row[0]
    file_url = row[1]
    r = requests.get(file_url, stream=True)
    f = open(file_name, "wb+")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
    f.close()
    if '/website_document/' not in file_name:
        try:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
            cur = conn.cursor()
            sql = "update website set file_name = %s where file_url = %s"
            cur.execute(sql,[file_name,file_url])
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        if cur:
            cur.close()
        if conn:
            conn.close()
        print(file_name)