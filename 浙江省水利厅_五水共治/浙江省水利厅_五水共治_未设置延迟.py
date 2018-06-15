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
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1',
        "Accept": "*/*",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }
    }

    list_forums = [{'forum':'0bj6','page':5,'name':u'综合动态','type':u'动态'},
                   {'forum':'0bj7','page':13,'name':u'地方动态','type':u'动态'},
                   {'forum':'0bj9','page':2,'name':u'经验交流','type':u'动态'}]

    @every(minutes=24 * 60)
    def on_start(self):
        url = "http://www.zjwater.com/pages/category/0bja/"
        self.crawl(url, fetch_type='js', callback=self.index_page1,
                   save={'name': u"政策文件,2015年11月10日起", 'type': u"政府发文"})
        for forum in self.list_forums:
            for p in range(1,forum.get('page')+1):
                url = 'http://www.zjwater.com/pages/category/{}/index_{}.htm'.format(forum.get('forum'),p)
                self.crawl(url, fetch_type='js', callback=self.index_page,save={'name':forum.get('name'),'type':forum.get('type')})

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('table#ctl00_cphBody_ctl00_dt_itemlist>tbody>tr>td>table>tbody>tr').items():
            url = each('td>div.SHORT_DIV1>a').attr.href
            title = each('td>div.SHORT_DIV1>a').attr.title
            created_at = each('td:nth-child(2)').text()
            name = response.save['name']
            type = response.save['type']
            # print url,title,created_at,name,type
            self.crawl(url, fetch_type='js', callback=self.detail_page, save={'title':title,'created_at':created_at,'name':name,'type':type})

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        title = response.save['title']
        created_at = response.save['created_at']
        selectors = [('#NewsContent', 'p', 'img'),('body > table:nth-child(5) > tbody > tr > td > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td','p','img')]
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
        come_from = response.doc('td#NewsContent>div').text().split(u'发布时间')[0].replace(u'来源：','')
        if come_from is None:
            come_from = text.split(u'来源：')[-1]
        forum_name = response.save['name']
        forum_type = response.save['type']
        type_id = (lambda x: 1 if x == u'动态' else 0)(forum_type)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
        result = [url,title,created_at,text,come_from,forum_name,type_id,crawl_time,u'浙江省水利厅/五水共治',None,None]
        # print text
        # print come_from
        # print type_id
        return result

    @config(age=24 * 60 * 60)
    def index_page1(self, response):
        for each in response.doc('table#ctl00_cphBody_ctl00_dt_itemlist>tbody>tr>td>table>tbody>tr').items():
            url = each('td>div.SHORT_DIV1>a').attr.href
            title = each('td>div.SHORT_DIV1>a').attr.title
            created_at = each('td:nth-child(2)').text()
            name = response.save['name']
            type = response.save['type']
            # print url,title,created_at,name,type
            if created_at >= '2015.11.10':
                self.crawl(url, fetch_type='js', callback=self.detail_page1,
                       save={'title': title, 'created_at': created_at, 'name': name, 'type': type})

    @config(priority=2)
    def detail_page1(self, response):
        url = response.url
        title = response.save['title']
        created_at = response.save['created_at']
        selectors = [('#NewsContent', 'p', 'img'),
                     ('#NewsContent > p:nth-child(2) > table > tbody > tr:nth-child(4) > td', 'p', 'img'),
                     ('#NewsContent > table > tbody > tr:nth-child(3) > td', 'p', 'img')]
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
        come_from = u"浙江省水利厅"
        forum_name = response.save['name']
        forum_type = response.save['type']
        type_id = (lambda x: 1 if x == u'动态' else 0)(forum_type)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
        file_url = None
        file_name = None
        for selector in selectors:
            for each in response.doc(selector[0]).items(selector[1]):
                file_url = each('a').attr.href
                if file_url is not None:
                    file_url_tmp = file_url.replace('?','#').replace('=','%')
                    file = file_url_tmp.replace('http://', '').replace('https://', '').replace('/', '_')
                    file_tail = '.' + file.split('.')[-1]
                    file_head = file.replace(file_tail, '').replace('.', '-')
                    file = file_head + file_tail
                    server_path = '/document_hzz/' + file
                    local_path = os.environ['HOME'] + '/.document_hzz/' + file
                    os.system('wget {} -O {}'.format(file_url, local_path))
                    file_name = server_path
                else:
                    file_name = ''
        result = [url,title,created_at,text,come_from,forum_name,type_id,crawl_time,u'浙江省水利厅/五水共治',file_url,file_name]
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
                sql = 'INSERT INTO website(url,title,push_time,context,come_from,page_type,type_id,spider_time,source,file_url,file_name) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 批量插入
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        else:
            result = result[::-1]
            try:
                sql = 'UPDATE website SET file_name=%s,file_url=%s,source=%s,spider_time=%s,type_id=%s,page_type=%s,come_from=%s,context=%s,push_time=%s,title=%s WHERE url=%s'
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