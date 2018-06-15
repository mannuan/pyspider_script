#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-09-26 16:51:01
# Project: zhejiang_water

from pyspider.libs.base_handler import *
import datetime
import time,random,sys
import pymysql

class Handler(BaseHandler):
    crawl_config = {
        "headers": {
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

    @every(minutes=72 * 60)
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from web_list where web_name = %s", '浙江水利厅')
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for row in rows:
            url = row[2]
            page_type = row[3]
            page_num = row[4]
            for i in range(1, int(page_num) + 1):
                page_url = url + str(i) + ".htm"
                self.crawl(page_url, callback=self.new_list_page, save={"page_type": page_type})

    @config(age=10 * 24 * 60 * 60)
    def new_list_page(self, response):
        page_type = response.save["page_type"]
        # 获取每个新闻的title和time信息,url
        count = 0
        for each_line_tr in response.doc('table#ctl00_cphBody_ctl00_dt_itemlist>tr').items():
            count += 1
            if count == 1:
                continue
            for each_new_table in each_line_tr('table').items():
                title = each_new_table('div.SHORT_DIV1>a').text()
                href = each_new_table('div.SHORT_DIV1>a').attr.href
                created_at = each_new_table('tr>td:nth-child(2)').text()
                self.crawl(href, callback=self.detail_page, save={"title": title, "time": created_at, "page_type": page_type},exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h

    @config()
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        artical = ""
        for each_word in response.doc('td#NewsContent').items():
            for each_p in each_word('p').items():
                artical += each_p.text()

        come_from = response.doc('td#NewsContent>div').text()
        artical_set = set(artical)
        if len(artical_set) == 0:
            artical = ""
            for each_p in response.doc('p').items():
                artical += each_p.text()
            come_from = "本站"
            artical_set = set(artical)
        if len(artical_set) == 0:
            title = response.save["title"]
            push_time = response.save["time"]
            page_type = response.save["page_type"]
            url = "http://www.zjwater.com" + response.doc("HTML").text()[17:-2]
            self.crawl(url, callback=self.detail_page, save={"title": title, "time": push_time, "page_type": page_type},exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h
        else:
            for ab in artical_set:
                if ab in 'qwertyuiopasdfghjklzxcvbnm/= ':
                    artical = artical.replace(ab, '')
            result = {}
            result["url"] = response.url
            result["title"] = response.save["title"]
            result["push_time"] = response.save["time"]
            result["context"] = artical
            result["spider_time"] = datetime.datetime.now()
            result["come_from"] = come_from
            result["page_type"] = response.save["page_type"]
            type_id = None
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                                   charset='utf8')
            cur = conn.cursor()
            try:
                cur.execute("select id from type where name=%s", u"动态")
                row = cur.fetchone()
                type_id = row[0]
                conn.commit()
            except Exception as e:
                conn.rollback()
            if cur:
                cur.close()
            if conn:
                conn.close()
            result["type_id"] = type_id
            result["source"] = u'浙江水利厅'

            return result

    def on_result(self, result):
        if not result or not result['title']:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                               charset='utf8')
        cur = conn.cursor()

        # 先查找是否存在
        cur.execute("select * from website where url = %s and source = '浙江水利厅'", result["url"])
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute(
                "insert into website(title,url,push_time,spider_time,come_from,context,page_type,type_id,source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(result["title"], result["url"], result["push_time"], result["spider_time"], result["come_from"],result["context"], result["page_type"],result["type_id"],result["source"]))
        conn.commit()
        cur.close()
        conn.close()