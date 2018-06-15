#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project: weixin

from pyspider.libs.base_handler import *
import time,json,pymysql,os
from lxml import etree
from pyquery import PyQuery as py
import lxml,random

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60 * 10)
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository', charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from weixin_public")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for row in rows:
            url = "http://weixin.sogou.com/weixin?type=1&s_from=input&query=" + row[1] + "&ie=utf8&_sug_=n&_sug_type_="
            self.crawl(url, callback=self.index_page,exetime=time.time()+random.randint(60*60, 12*60*60))#1h~12h

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('UL.news-list2>LI:nth-child(1)>DIV.gzh-box2>DIV.txt-box>P.tit>a').items():
            self.crawl(each.attr.href, callback=self.list_page,exetime=time.time()+random.randint(60*60, 12*60*60))#1h~12h

    @config(priority=3)
    def list_page(self, response):
        time.sleep(10)
        scriptStr = response.doc('body').text()
        if scriptStr.find("msgList", 1) != -1:
            start = scriptStr.find("msgList", 1) + 10
            end = len(scriptStr) - 42
            msg = json.loads(scriptStr[start:end])
            for each in msg["list"]:
                url = each["app_msg_ext_info"]["content_url"]
                url = url.replace("amp;", "")
                self.crawl("http://mp.weixin.qq.com" + url, callback=self.detail_page,exetime=time.time()+random.randint(60*60, 12*60*60))#1h~12h

    @config(priority=2)
    def detail_page(self, response):
        content = response.doc('#js_content').html().strip()

        p = py(content)

        def Download_Pic(url, img_name):
            # os.system('wget {} -T 10 -t 6 -O {}/.picture_hzz/{}'.format(url, os.environ['HOME'], img_name))
            img_url = url
            server_path = 'http://122.224.129.35:28080/picture_hzz/{}'.format(img_name)
            local_path = '{}/.picture_hzz/{}'.format(os.environ['HOME'],img_name)

            result = [img_url,server_path,local_path,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())]
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
            cur = conn.cursor()
            try:
                sql = 'REPLACE INTO weixin_pic values(%s,%s,%s,%s)'
                cur.execute(sql, result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
            # 释放数据连接
            if cur:
                cur.close()
            if conn:
                conn.close()


        def GetPicname(url):
            return url.replace('https://', '').replace('http://', '').replace('/', '_').replace('.', '-').split('?')[0]

        def CreateEtree(next, root):
            if len(next.getchildren()) is not 0:
                for child in next.getchildren():
                    p = etree.SubElement(root, 'p')
                    CreateEtree(child, p)
            else:
                if next.tag == 'img':
                    if next.attrib.get('data-src') is None:
                        p = etree.SubElement(root, 'p')
                        p.text = ' '
                    elif next.attrib.get('data-src').find('http') == 0:  # http在字符串的最前面
                        img = etree.SubElement(root, 'img')
                        img_url = next.attrib.get('data-src')
                        img_name = GetPicname(img_url)
                        img.attrib['src'] = '/picture_hzz/{}'.format(img_name)
                        Download_Pic(img_url, img_name)
                else:
                    p = etree.SubElement(root, 'p')
                    p.text = (lambda x: ' ' if x is None else x)(next.text)

        text = ''
        for each in p.contents():
            if not isinstance(each,lxml.etree._ElementStringResult):
                root = etree.Element('p')
                for child in each.getchildren():
                    p = etree.Element('p')
                    CreateEtree(child, p)
                    root.append(p)
                text += etree.tostring(root, encoding='utf-8')
        text = text.replace('\"',' ')
        # print text

        result = [
            response.doc('#activity-name').text(),
            response.doc('#post-date').text(),
            response.doc('#meta_content > span').text(),
            text,
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            response.url
        ]
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from weixin_info where url = %s" , result[0])
        rows = cur.fetchall()
        if len(rows) == 0:
            try:
                sql = 'INSERT INTO weixin_info(title,time,public_name,main_body,spider_time,url) values(%s,%s,%s,%s,%s,%s)'
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        else:
            try:
                sql = 'UPDATE website SET title=%s,time=%s,public_name=%s,main_body=%s,spider_time=%s WHERE url=%s'
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