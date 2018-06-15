#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-07 22:55:40
# Project: sdad

from pyspider.libs.base_handler import *
import json,pymysql,time


class Handler(BaseHandler):
    crawl_config = {
        "headers" : {
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1',
        }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                               charset='utf8mb4')
        cur = conn.cursor()
        sql = "select id,totalCommentCount from elong_shop"
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        for row in rows:
            id = row[0]
            totalCommentCount = row[1]
            # print reviewCount
            # print int(reviewCount/20)+1
            # print '------------------------------------'
            for i in range(1,int(totalCommentCount/20)+2):
                url = 'http://m.elong.com/hotel/api/morereviewnew?hotelid={}&pagesize=20&pageindex={}'.format(id,i)
                self.crawl(url, save={'id':id}, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        result = []
        ob_json = response.json
        list_comments = ob_json.get('comments')
        if len(list_comments) is 0:
            return
        for comment in list_comments:
            commentDateTime = comment.get('commentDateTime')#创建的时间
            commentFrom = comment.get('commentFrom')#评论来源
            commentScoreTotal = comment.get('commentScoreTotal')#int
            content = comment.get('content')#评论内容
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
            id = response.save['id']
            isMarrow = comment.get('isMarrow')#int
            largeImagePath = json.dumps(comment.get('largeImagePath'))
            replys = json.dumps(comment.get('replys'))#
            roomTypeName = comment.get('roomTypeName')#
            travelType = comment.get('travelType')#int
            userName = comment.get('userName')#
            userRank = comment.get('userRank')#int
            result.append([commentDateTime,commentFrom,commentScoreTotal,content,crawl_time,id,isMarrow,largeImagePath,replys,roomTypeName,travelType,userName,userRank])
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO elong_comment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
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