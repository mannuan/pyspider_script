#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project:

from pyspider.libs.base_handler import *
import time,pymysql,sys,random

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
        forum = {'page':21,'name':u'水环境保护标准','type':u'标准'}
        url = 'http://kjs.mep.gov.cn/hjbhbz/bzwb/shjbh/index.shtml'
        self.crawl(url, fetch_type='js', callback=self.index_page,save={'name':forum.get('name'),'type':forum.get('type')},
                   exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h
        for p in range(1,forum.get('page')):
            url = 'http://kjs.mep.gov.cn/hjbhbz/bzwb/shjbh/index_{}.shtml'.format(p)
            self.crawl(url, fetch_type='js', callback=self.index_page,save={'name':forum.get('name'),'type':forum.get('type')},
                       exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div.main_rt_list>ul>li').items():
            url = each('a').attr.href
            title = each('a').attr.title
            created_at = each('span').text()
            name = response.save['name']
            type = response.save['type']
            # print url,title,created_at,name,type
            self.crawl(url, fetch_type='js', callback=self.detail_page, save={'title':title,'created_at':created_at,'name':name,'type':type},
                       exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        title = response.save['title']
        created_at = response.save['created_at']
        text = ''
        for cs in ['div.wzxq_neirong2>p','div.wzxq_neirong2']:
            for each in response.doc(cs).items():
                text += each.text()
                if text is not '':
                    break
        for cs in ['div.TRS_Editor>p>a','div.wzxq_neirong2>p>a','div.Custom_UnionStyle>p>a']:
            file_url = response.doc(cs).attr.href
            # print file_url
            if file_url is not None:
                break
        file_name = ''
        if file_url is not None:
            file_name = file_url.split('/')[-1]
        come_from = u"无"
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
        result = [url,title,created_at,text,file_url,file_name,come_from,forum_name,type_id,crawl_time,u'环保部']
        # print text
        # print file_url
        # print file_name
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
                sql = 'INSERT INTO website(url,title,push_time,context,file_url,file_name,come_from,page_type,type_id,spider_time,source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 批量插入
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
        else:
            result = result[::-1]
            try:
                sql = 'UPDATE website SET source=%s,spider_time=%s,type_id=%s,page_type=%s,come_from=%s,file_name=%s,file_url=%s,context=%s,push_time=%s,title=%s WHERE url=%s'
                # 批量更新
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()