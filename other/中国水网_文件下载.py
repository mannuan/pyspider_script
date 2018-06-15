#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project:

from pyspider.libs.base_handler import *
import time,pymysql,sys

class Handler(BaseHandler):
    crawl_config = {
        "headers":{
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Accept": "*/*",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        # 先查找是否存在
        cur.execute("select file_name from zhongguoshuiwang")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for url in rows:
            print(url[0])
            # self.crawl(url, callback=self.index_page)

    # @config(age=10 * 24 * 60 * 60)
    # def index_page(self, response):
    #     for each in response.doc('div.lists.txtList>ul>li').items():
    #         url = each('em.title>a.ellip.w540').attr.href
    #         forum = response.save['forum']
    #         name = response.save['name']
    #         type = response.save['type']
    #         self.crawl(url, fetch_type='js', callback=self.detail_page, save={'forum':forum,'name':name,'type':type})
    #
    # def on_result(self, result):
    #     if not result:
    #         return
    #     conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
    #     cur = conn.cursor()
    #     try:
    #         sql = 'REPLACE INTO zhongguoshuiwang values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #         # 批量插入
    #         cur.executemany(sql,result)
    #         conn.commit()
    #     except Exception as e:
    #         print(e)
    #         conn.rollback()
    #     # 释放数据连接
    #     if cur:
    #         cur.close()
    #     if conn:
    #         conn.close()