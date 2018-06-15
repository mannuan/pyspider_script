#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-02-04 10:34:58
# Project: 百度百科网站版

from pyspider.libs.base_handler import *
import pymysql,time,re

class Handler(BaseHandler):
    crawl_config = {
    }

    context_css = "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/style.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/bootstrap.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/font-awesome.min.css\">"
    context_html_tmp = "<article class=\"entry\">{}</article>"

    @every(minutes=24 * 60)
    def on_start(self):
        # conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository', charset='utf8')
        # cur = conn.cursor()
        # cur.execute("select name from river")
        # rows = cur.fetchall()
        # conn.commit()
        # cur.close()
        # conn.close()
        # for row in rows:
        url = 'https://baike.baidu.com/item/东阳江'
        self.crawl(url, fetch_type='js', save={'river_name':'东阳江'}, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        title = response.save['river_name']
        url = response.url
        spider_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        type_id = 0
        source = '百度百科'
        if url.find('https://baike.baidu.com/error.html') == 0:
            result = None
        else:
            context = '<div class=\"entry__article\">'
            ##############
            content_html = response.doc('body > div.body-wrapper > div.content-wrapper > div > div.main-content').html()
            for i in re.findall('<[^ \"</>]+([ ]+[^<>]*)?>',content_html):
                content_html = content_html.replace(i,'')
            content_html = re.sub('[\f\n\r]+','',content_html)
            context += content_html
            ##############
            context += '</div>'
            context = self.context_css+self.context_html_tmp.format(context)
            with open('/home/mininet/test.txt','w+') as f:
                f.write(context)
            print context
            result = [title,url, '', context, '', '', type_id, spider_time, source]
        # return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from website where url = %s" , result[0])
        rows = cur.fetchall()
        if len(rows) == 0:
            try:
                sql = 'INSERT INTO website(title,url,push_time,context,come_from,page_type,type_id,spider_time,source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 批量插入
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        else:
            result = result[::-1]
            try:
                sql = 'UPDATE website SET source=%s,spider_time=%s,type_id=%s,page_type=%s,come_from=%s,context=%s,push_time=%s,url=%s WHERE title=%s'
                # 批量更新
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()