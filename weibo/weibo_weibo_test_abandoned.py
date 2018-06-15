#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-18 09:06:44
# Project: weibo_weibo

from pyspider.libs.base_handler import *
import time, pymysql,re

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
    }

    key_words = ["河长制", "智慧治水", "水利厅", "污水治理", "一河一策", "水政执法", "水资源保护", "河湖水域岸线保护", "水污染防治", "水生态修复", "水利工程管理", "环境改善","水质监测", "涉河水利工程", "岸线规划", "污水治理", "水环境治理"]

    @every(minutes=24 * 60)#24个小时
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        # 先查找是否存在
        cur.execute("select user_id from weibo_user")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for id in rows:
            url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}&containerid=107603{}&page={}".format(id[0], id[0], id[0], 1)
            self.crawl(url, callback=self.index_page)

    @config(age=24 * 60 * 60)#24个小时
    def index_page(self, response):
        ob_json = response.json
        list_cards = ob_json.get('cards')
        if list_cards is None:
            return
        result = []
        for card in list_cards:  # 遍历
            if card.get('card_type') == 9:  # 等于9的微博才是正文,其他的都是推荐或者其他,`weibo_user`的唯一标识
                user_id = card.get('mblog').get('user').get('id')  # 微博用户的id
                user_name = card.get('mblog').get('user').get('screen_name')  # 微博用户的昵称
                weibo_id = card.get('mblog').get('id')  # 微博的id,`weibo_weibo`table的唯一标识
                created_at = card.get('mblog').get('created_at')  # 微博创建的时间
                source = card.get('mblog').get('source')  # 微博的来源
                if source == '':
                    source = u'未知'
                text = card.get('mblog').get('text')
                text = Tool.replace(text)  # 微博的内容

                reposts_count = card.get('mblog').get('reposts_count')  # 微博的转发数
                comments_count = card.get('mblog').get('comments_count')  # 微博的评论数
                attitudes_count = card.get('mblog').get('attitudes_count')  # 微博的点赞数
                crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
                result.append([user_id,user_name,weibo_id,created_at,source,text,reposts_count,comments_count,attitudes_count,crawl_time])
            if card.get('card_type') == 11:  # 等于9的微博才是正文,其他的都是推荐或者其他,`weibo_user`的唯一标识
                user_id = card.get('mblog').get('user').get('id')  # 微博用户的id
                user_name = card.get('mblog').get('user').get('screen_name')  # 微博用户的昵称
                weibo_id = card.get('mblog').get('id')  # 微博的id,`weibo_weibo`table的唯一标识
                created_at = card.get('mblog').get('created_at')  # 微博创建的时间
                source = card.get('mblog').get('source')  # 微博的来源
                if source == '':
                    source = u'未知'
                text = card.get('mblog').get('text')
                text = Tool.replace(text)  # 微博的内容

                reposts_count = card.get('mblog').get('reposts_count')  # 微博的转发数
                comments_count = card.get('mblog').get('comments_count')  # 微博的评论数
                attitudes_count = card.get('mblog').get('attitudes_count')  # 微博的点赞数
                crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
                result.append([user_id,user_name,weibo_id,created_at,source,text,reposts_count,comments_count,attitudes_count,crawl_time])
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO weibo_weibo(user_id,user_name,weibo_id,created_at,source,text,reposts_count,comments_count,attitudes_count,crawl_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # 批量插入
            cur.executemany(sql,result)
            conn.commit()
        except Exception as e:
            print e
            conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()