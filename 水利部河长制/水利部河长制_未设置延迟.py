#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project:

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
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Accept": "*/*",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }
    }

    list_forums = [{'forum':'zyjs','page':1,'name':u'中央精神','type':u'政府发文'},{'forum':'zydt','page':1,'name':u'重要动态','type':u'动态'},{'forum':'gzbs','page':1,'name':u'工作部署','type':u'动态'},{'forum':'dfldt','page':2,'name':u'地方领导谈','type':u'动态'},{'forum':'dfxd','page':18,'name':u'流域地方','type':u'动态'},{'forum':'gzfa','page':2,'name':u'工作方案','type':u'政府发文'},{'forum':'mtjj','page':10,'name':u'媒体聚焦','type':u'动态'},{'forum':'gzjb','page':5,'name':u'工作简报','type':u'动态'}]

    list_text_css_selector = ['td.content>div.TRS_Editor>p','div.model#about_txt>div.mbd>div.cnt_bd>p','div.slnewscon.autoHeight','div.vintro>p','div.content1']

    @every(minutes=24 * 60)
    def on_start(self):
        for forum in self.list_forums:
            url = 'http://www.mwr.gov.cn/ztpd/2016ztbd/qmtxhzzhhghkxj/{}/'.format(forum.get('forum'))
            self.crawl(url, fetch_type='js', callback=self.index_page,save={'name':forum.get('name'),'type':forum.get('type')},
                       exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h
            for p in range(1,forum.get('page')):
                url = 'http://www.mwr.gov.cn/ztpd/2016ztbd/qmtxhzzhhghkxj/{}/index_{}.html'.format(forum.get('forum'),p)
                self.crawl(url, fetch_type='js', save={'name':forum.get('name'),'type':forum.get('type')})

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('div.dbgxia>div.dbgshang>table.tbg>tbody>tr>td:nth-child(2)>table:nth-child(4)>tbody>tr>td>table:nth-child(2)>tbody>tr').items():
            url = each('td:nth-child(2)>a').attr.href
            title = each('td:nth-child(2)>a').text()
            created_at = each('td:nth-child(3)').text().replace('&nbsp;','')
            name = response.save['name']
            type = response.save['type']
            self.crawl(url, fetch_type='js', callback=self.detail_page, save={'title':title,'created_at':created_at,'name':name,'type':type})

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        title = response.save['title']
        created_at = response.save['created_at']
        selectors = [
            ('#about_txt > div.mbd > div', 'p', 'img'),('body > div.dbgxia > div > table.tbg > tbody > tr > td:nth-child(2) > table:nth-child(4) > tbody > tr > td > table:nth-child(2) > tbody > tr:nth-child(3) > td > div','p','img')]
        text = ''
        for (selector1, selector2, selector3) in selectors:
            for each in response.doc(selector1).items(selector2):
                img_url = each(selector3).attr.src
                if img_url is not None:
                    img_url_tmp = img_url.split('?')[0]  # 去除url后面的参数部分
                    img_name = img_url_tmp.replace('http://', '').replace('https://', '').replace('/', '_')
                    img_tail = '.' + img_name.split('.')[-1]
                    img_head = img_name.replace(img_tail, '').replace('.', '-')
                    img_name = img_head + img_tail
                    server_path = '/picture_hzz/' + img_name
                    local_path = os.environ['HOME'] + '/.picture_hzz/' + img_name
                    os.system('wget {} -O {}'.format(img_url, local_path))
                    part = "<p><img src={}></p>".format(server_path)  # 为了显示图片更加清楚把img标签加入p标签里面
                else:
                    part = '<p>{}</p>'.format(each.text())
                    part = part.replace('\'', '\\\'').replace('\"', '\\\"')
                text += part
            if text.replace(' ', '').replace('　', '').replace('\n', '').replace('\r', '') != '':
                break
        editor = response.doc('td.content>p').text().replace('责编：','')
        forum_name = response.save['name']
        forum_type = response.save['type']
        type_id = (lambda x: 1 if x == u'动态' else 0)(forum_type)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
        result = [url,title,created_at,text,editor,forum_name,type_id,crawl_time,u'水利部河长制']
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