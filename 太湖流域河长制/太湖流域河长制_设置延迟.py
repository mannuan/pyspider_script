#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project: taihuliuyuhezhangzhi

from pyspider.libs.base_handler import *
import time,pymysql,sys,random,os
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

    list_forums = [{'forum':'gzdt','page':1,'name':u'工作动态','type':u'动态'},
                   {'forum':'zcwj','page':1,'name':u'政策文件,中央/地方','type':u'政府发文'},
                   {'forum':'jyjl','page':1,'name':u'经验交流','type':u'动态'},
                   {'forum':'mtbg','page':1,'name':u'媒体报道','type':u'动态'}]

    @every(minutes=24 * 60)
    def on_start(self):
        for forum in self.list_forums:
            url = 'http://www.tba.gov.cn/tba/content/TBA/xwzx/jczt/hcz/{}/'.format(forum.get('forum'))
            self.crawl(url, fetch_type='js', callback=self.index_page,save={'name':forum.get('name'),'type':forum.get('type')},exetime=time.time()+random.randint(60*60, 12*60*60))#1h~12h

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('tbody#pageNumRows_1>tr>td>li').items():
            url = each('a').attr.href
            title = each('a').attr.title
            created_at = each('span').text().replace('&nbsp','')
            name = response.save['name']
            type = response.save['type']
            # print url,title,created_at,name,type
            self.crawl(url, fetch_type='js', callback=self.detail_page, save={'title':title,'created_at':created_at,'name':name,'type':type},exetime=time.time()+random.randint(60*60, 12*60*60))#1h~12h

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        title = response.save['title']
        created_at = response.save['created_at']
        text = ''
        for each in response.doc('#print > tbody > tr:nth-child(5) > td > table > tbody > tr > td').items('p'):
            img_url = each('img').attr.src
            if img_url is not None:
                img_name = img_url.replace('http://','').replace('https://','').replace('/','_')
                img_tail = '.'+img_name.split('.')[-1]
                img_head = img_name.replace(img_tail,'').replace('.','-')
                img_name = img_head+img_tail
                server_path = '/picture_hzz/'+img_name
                local_path = os.environ['HOME']+'/.picture_hzz/'+img_name
                os.system('wget {} -O {}'.format(img_url,local_path))
                part = "<p><img src={}></p>".format(server_path)  # 为了显示图片更加清楚把img标签加入p标签里面
            else:
                part = '<p>{}</p>'.format(each.text())
                part = part.replace('\'','\\\'').replace('\"','\\\"')
            text+=part
        come_from = u"水利部太湖流域管理局"
        forum_name = response.save['name']
        forum_type = response.save['type']
        type_id = (lambda x:1 if x == u'动态' else 0)(forum_type)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
        result = [url,title,created_at,text,come_from,forum_name,type_id,crawl_time,u'太湖流域河长制']
        # print text
        # print come_from
        # print type_id
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