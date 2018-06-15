#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-21 14:28:38
# Project: baidubaike

from pyspider.libs.base_handler import *
import pymysql,time,urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Handler(BaseHandler):
    crawl_config = {
        "headers":{
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Upgrade-Insecure-Requests':'1',
            'Content-Encoding': 'gzip',
            'Content-Type': 'text/html',
        }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository', charset='utf8mb4')
        cur = conn.cursor()
        cur.execute("select name from river")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for row in rows:
            url = u'http://wapbaike.baidu.com/item/{}'.format(row[0])
            self.crawl(url, save={'river_name':row[0]}, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        river_name = response.save['river_name']
        url = response.url
        pic_url = response.doc('img.J-imgPlaceholder').attr.src
        title = response.doc('span.lemma-title').text()
        summary = ''
        for each in response.doc('div.summary-content>p').items():
            summary+=each.text()
        basic_info = ''
        for each in response.doc('div.basicInfo#J-basicInfo>ul>li>div').items():
            basic_info+=each.text()+' '
        content = response.doc('div.BK-main-content').text()
        reference = response.doc('div.reference#J-reference').text()
        quick_pic = "/home/quick_picture/{}_baidubaike.html".format(river_name)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        html = u"<html><head><meta http-equiv='Content-Type' content='text/html;charset=utf-8'><base href='" + response.url + u"'></head><body><div style='position:relative'>"
        html += response.doc("HEAD").html()
        html += response.doc("BODY").html()
        html += u"</div></body></html>"
        return [html,basic_info,content,crawl_time,pic_url,quick_pic,reference,river_name,summary,title,url]

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO baidubaike values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # 批量插入
            cur.execute(sql,result[1:])
            conn.commit()
        except Exception as e:
            print e
            conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()
        url = 'http://wapbaike.baidu.com/item/{}'.format(result[7])
        local = "/home/quick_picture/{}_baidubaike.html".format(result[7])
        urllib.urlretrieve(url, local)