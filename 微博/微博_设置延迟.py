#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-20 13:26:05
# Project: weibo

from pyspider.libs.base_handler import *
import time,pymysql,re,random,os

class Tool:
    #去除img标签
    removeImg = re.compile('<img.*>| {1,7}|&nbsp;')
    #去除超链接 a标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行换成\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')

    #去除所有标签
    removeTag = re.compile('<.*?>')

    @classmethod
    def replace(cls,x):
        x = re.sub(cls.removeImg,'',x)
        x = re.sub(cls.removeAddr,'',x)
        x = re.sub(cls.replaceLine,'',x)
        x = re.sub(cls.removeTag,'',x)

        return x.strip()#去掉多余的内容

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

    key_words = ["河长制", "智慧治水", "水利厅", "污水治理", "一河一策", "水政执法", "水资源保护", "河湖水域岸线保护", "水污染防治", "水生态修复", "水利工程管理", "环境改善","水质监测", "涉河水利工程", "岸线规划", "污水治理", "水环境治理"]

    @every(minutes=24 * 60)
    def on_start(self):
        for kw in self.key_words:
            url = 'http://m.weibo.cn/api/container/getIndex?key={}'.format(kw)
            self.crawl(url, params={'containerid':"100103type=1&q={}".format(kw)}, callback=self.index_page,
                           exetime=time.time() + random.randint(60 * 60, 12 * 60 * 60))  # 1h~12h

    @config(age=24 * 60 * 60)
    def index_page(self, response):
        result = []
        ob_json = response.json
        for i in ob_json.get('data').get('cards'):
            if i.get('card_type') is 9:
                result.append(self.detail_page(i))
            else:
                card_group = i.get('card_group')
                if card_group is None:
                    continue
                for j in card_group:
                    if j.get('card_type') is 9:
                        result.append(self.detail_page(j))
        return result

    @config(priority=2)
    def detail_page(self, response):
        ob_json = response
        user_id = ob_json.get('mblog').get('user').get('id')
        user_name = ob_json.get('mblog').get('user').get('screen_name')
        weibo_id = ob_json.get('mblog').get('id')
        created_at = ob_json.get('mblog').get('created_at')
        source = ob_json.get('mblog').get('source')
        longTextContent = Tool.replace(ob_json.get('mblog').get('text'))
        title = longTextContent[:10]+'...'
        longTextContent = '<p>'+longTextContent+'</p>'
        pics = ob_json.get('mblog').get('pics')
        if pics is not None:
            for pic in ob_json.get('mblog').get('pics'):
                img_url = pic.get('large').get('url')
                img_name = img_url.replace('https://', '').replace('http://', '').replace('/', '_')
                img_tail = '.' + img_name.split('.')[-1]
                img_head = img_name.replace(img_tail, '').replace('.', '-')
                img_name = img_head + img_tail
                server_path = '/picture_hzz/' + img_name
                local_path = os.environ['HOME'] + '/.picture_hzz/' + img_name
                os.system('wget {} -t 3 -T 10 -O {}'.format(img_url, local_path))
                longTextContent += "<p><img src={}></p>".format(server_path)  # 为了显示图片更加清楚把img标签加入p标签里面
        reposts_count = ob_json.get('mblog').get('reposts_count')
        comments_count = ob_json.get('mblog').get('comments_count')
        attitudes_count = ob_json.get('mblog').get('attitudes_count')
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        type_id = 0
        return [[weibo_id,title, "https://m.weibo.cn/status/{}".format(weibo_id),longTextContent,u'微博',created_at,crawl_time,user_name,type_id],[crawl_time,reposts_count,comments_count,attitudes_count]]

    def on_result(self, result):
        if not result:
            return
        for r in result:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
            cur = conn.cursor()
            cur.execute("select * from invitation where note_id = %s" , r[0][0])
            rows = cur.fetchall()
            if len(rows) == 0:
                try:
                    cur.execute('select max(id) from invitation')
                    trend_id = (lambda x: 0 + 1 if x is None else x + 1)(cur.fetchone()[0])
                    sql = 'INSERT INTO invitation(note_id,note_title,note_url,note_context,source,push_time,crawl_time,push_name,type_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    # 批量插入
                    cur.execute(sql,r[0])
                    conn.commit()
                except Exception as e:
                    print e
                    conn.rollback()
            else:
                r[0] = r[0][::-1]
                try:
                    cur.execute('select id from invitation where note_id = %s', r[0][-1])
                    trend_id = cur.fetchone()[0]
                    sql = 'UPDATE invitation SET type_id=%s,push_name=%s,crawl_time=%s,push_time=%s,source=%s,note_context=%s,note_url=%s,note_title=%s WHERE note_id=%s'
                    # 批量更新
                    cur.execute(sql,r[0])
                    conn.commit()
                except Exception as e:
                    print e
                    conn.rollback()
            try:
                sql = 'INSERT INTO invitation_trend(crawl_time,reposts_count,comments_count,attitudes_count,id) values(%s,%s,%s,%s,%s)'
                r[1].append(trend_id)
                cur.execute(sql, r[1])
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
            # 释放数据连接
            if cur:
                cur.close()
            if conn:
                conn.close()