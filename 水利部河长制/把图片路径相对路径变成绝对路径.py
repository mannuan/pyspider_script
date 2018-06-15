# -*- coding:utf-8 -*-

import time,pymysql,sys,random,re,os
reload(sys)
sys.setdefaultencoding('utf8')

def change_pic_path():
    conn = pymysql.connect(host='122.224.129.35', port=23306, user='repository', passwd='repository', db='repository',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT url,context FROM repository.website where context like '%picture_hzz%'")
    rows = cur.fetchall()
    for row in rows:
        if '122.224.129.35:28080' not in row[1]:
            context = row[1].replace('/picture_hzz/', 'http://122.224.129.35:28080/picture_hzz/')
            cur.execute("update website set context = %s where url = %s", (context, row[0]))
            print row[0]
            conn.commit()
    if cur:
        cur.close()
    if conn:
        conn.close()

def check_pic_path():#检查图片路径是否重复
    conn = pymysql.connect(host='122.224.129.35', port=23306, user='repository', passwd='repository', db='repository',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT url,context FROM repository.website where context like '%picture_hzz%'")
    rows = cur.fetchall()
    for row in rows:
        if '122.224.129.35:28080' in row[1]:
            if len(re.findall(r'24.129.35:28080http://122.224.129.35:28080', row[1])) >= 1:
                print row[1]
                break
    if cur:
        cur.close()
    if conn:
        conn.close()

def pic_path_repair():
    conn = pymysql.connect(host='122.224.129.35', port=23306, user='repository', passwd='repository', db='repository',
                           charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT url,context FROM repository.website where source = '百度百科' and context like '%<img%'")
    rows = cur.fetchall()
    for row in rows:
        if '122.224.129.35:28080' in row[1]:
            if len(re.findall(r'24.129.35:28080http://122.224.129.35:28080', row[1])) >= 1:
                # context = re.sub(r'^(.*<img src=\")(?!/picture_hzz/)[^_]*(/picture_hzz/.*)$',r'\1\2',row[1])
                # cur.execute("update website set context = %s where url = %s", (context, row[0]))
                print row[1]
                # conn.commit()
    if cur:
        cur.close()
    if conn:
        conn.close()

if __name__ == '__main__':
    # change_pic_path()
    # check_pic_path()
    pic_path_repair()
