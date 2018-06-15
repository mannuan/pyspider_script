#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-21 14:28:38
# Project: baidubaike

from pyspider.libs.base_handler import *
import pymysql,time,sys,re,os,urlparse
reload(sys)
sys.setdefaultencoding('utf-8')
from pyquery import PyQuery

class Handler(BaseHandler):
    crawl_config = {
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

    def filter_page(self, response, *args):
        server_path = '/picture_hzz/'
        local_path = os.environ['HOME'] + '/.picture_hzz/'
        content = ''
        for cs in args:
            p = response.doc(cs)  # rd是一个PyQuery对象
            p('script').remove()  # 去除script标签
            p('style').remove()  # 去除style标签
            content += (
                lambda x: '' if x is None else re.sub(
                    r'[ ]+[^ \"</>=]+[ ]*=[ ]*?\"(?!https://|http://)[^\"<>]*?\"|[\f\n\r]+', '', x))(
                p.html())  # 先去除没有用的class和style属性
        original_url_list = []
        regex = re.compile(
            r'<(?!div|img)[^ </>\"]+([^<>]*)[ ]+(?!href)[^ </>\"]+[ ]*=[ ]*?\"((?=https://|http://)[^ \"<>]+)?\"([^<>]*)[/]{0,1}?>')  # 标签不是img
        content = regex.sub(r'<img\1 src="\2"\3>', content)  # 更改为img标签
        original_url_list.extend([url[1] for url in regex.findall(content)])  # 原始的img url
        regex = re.compile(
            r'<(?=img)[^ </>\"]+([^<>]*)[ ]+(?=src)[^ </>\"]+[ ]*=[ ]*?\"((?=https://|http://)[^ \"<>]+)?\"([^<>]*)[/]{0,1}?>')  # 标签是img
        content = regex.sub(r'<img\1 src="\2"\3>', content)  # 更改为img标签
        original_url_list.extend([url[1] for url in regex.findall(content)])  # 原始的img url
        url_list = []  # 可用于下载的img url
        for i in range(len(original_url_list)):  # 过滤img url
            params = dict(
                [(k, v[0]) for k, v in urlparse.parse_qs(urlparse.urlparse(original_url_list[i]).query).items()])
            if len(params) != 0:
                url = (lambda url, src: url.split('?')[0] if src is None else src)(original_url_list[i],
                                                                                   params.get('src'))  # 修改后的img url
                url_list.append(url)
                content = content.replace(original_url_list[i], url)
            else:
                url_list.append(original_url_list[i])
        time_list = []
        for i in range(len(original_url_list)):
            name = str(time.time()).replace('.', '')
            time_list.append(name)
            time.sleep(0.01)
        pic_list = []
        download_pic_list = []
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                               charset='utf8')
        cur = conn.cursor()
        for i in range(len(original_url_list)):
            cur.execute("select name,url from hzz_local_picture where url = %s", url_list[i])
            row = cur.fetchone()
            if row is None:
                cur.execute("insert into hzz_local_picture values(%s,%s)", [time_list[i], url_list[i]])
                pic_list.append((time_list[i], url_list[i]))
                download_pic_list.append((time_list[i], url_list[i]))
            else:
                pic_list.append((row[0].encode('utf-8'), row[1].encode('utf-8')))
            conn.commit()
        cur.close()
        conn.close()
        for pic in pic_list:
            content = content.replace(pic[1], server_path + pic[0])
        for pic in download_pic_list:
            os.system('wget {} -O {}'.format(pic[1], local_path + pic[0]))
        return content

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        river_name = response.save['river_name']
        url = response.url
        content = self.filter_page(response,
                         '#J-lemma > div.BK-body-wrapper > div.BK-before-content-wrapper',
                         '#J-lemma > div.BK-body-wrapper > div.BK-content-wrapper')
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        return [content,crawl_time,river_name,url.encode('utf-8')]

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO baidubaike values(%s,%s,%s,%s)'
            # 批量插入
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