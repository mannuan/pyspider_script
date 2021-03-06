#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project:

from pyspider.libs.base_handler import *
import time,pymysql,sys,random
reload(sys)
sys.setdefaultencoding('utf8')

class Handler(BaseHandler):
    crawl_config = {
        "headers":{
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1',
        "Accept": "*/*",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }
    }

    list_forums = [{'forum':'col43216','page':4,'name':u'时事要闻','type':u'动态'},
                   {'forum':'col42975','page':5,'name':u'各地动态','type':u'动态'},
                   {'forum':'col42896','page':2,'name':u'媒体聚焦','type':u'动态'}]

    list_text_css_selector = ['td.content>div.TRS_Editor>p','div.model#about_txt>div.mbd>div.cnt_bd>p','div.slnewscon.autoHeight','div.vintro>p','div.content1']

    @every(minutes=24 * 60)
    def on_start(self):
        for forum in self.list_forums:
            for p in range(1,forum.get('page')+1):
                url = 'http://jswater.jiangsu.gov.cn/col/{}/index.html?uid=191194&pageNum={}'.format(forum.get('forum'),p)
                self.crawl(url, fetch_type='js', callback=self.index_page,save={'name':forum.get('name'),'type':forum.get('type')},
                           exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div.default_pgContainer>table>tbody>tr').items():
            url = each('td:nth-child(1)>div>a').attr.href
            title = each('td:nth-child(1)>div>a').attr.title
            created_at = each('td:nth-child(2)').text()
            name = response.save['name']
            type = response.save['type']
            # print url
            # print title
            # print created_at
            self.crawl(url, fetch_type='js', callback=self.detail_page, save={'title':title,'created_at':created_at,'name':name,'type':type},
                       exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        title = response.save['title']
        created_at = response.save['created_at']
        text = ''
        for each in response.doc('div#zoom>p').items():
            text += each.text()
        come_from = ''
        forum_name = response.save['name']
        forum_type = response.save['type']
        type_id = None
        conn = pymysql.connect(host='localhost', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        try:
            cur.execute("select id from type where name=%s", forum_type)
            row = cur.fetchone()
            type_id = row[0]
            conn.commit()
        except Exception as e:
            conn.rollback()
        if cur:
            cur.close()
        if conn:
            conn.close()
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
        result = [url,title,created_at,text,come_from,forum_name,type_id,crawl_time,u'江苏省水利厅/河长制']
        # print text
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from website where url = %s" , result[0])
        rows = cur.fetchall()
        if len(rows) == 0:
            try:
                sql = 'INSERT INTO website(url,title,push_time,context,come_from,page_type,type_id,spider_time,source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 批量插入
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        else:
            result = result[::-1]
            try:
                sql = 'UPDATE website SET source=%s,spider_time=%s,type_id=%s,page_type=%s,come_from=%s,context=%s,push_time=%s,title=%s WHERE url=%s'
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