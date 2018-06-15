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
        sql = "select id,reviewCount from dazhongdianping_shop"
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        for row in rows:
            id = row[0]
            reviewCount = row[1]
            # print reviewCount
            # print int(reviewCount/20)+1
            # print '------------------------------------'
            for i in range(1,int(reviewCount/10)+2):
                url = 'http://m.dianping.com/isoapi/module'
                url += "?id={}&page={}".format(id,i)
                data = {"moduleInfoList": [{"moduleName": "reviewlist", "query": {"shopId": str(id), "page": i}}],
                        "pageEnName": "shopreviewlist"}
                data = json.dumps(data)
                self.crawl(url, method='POST', data=data, save={'id':id}, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        result = []
        ob_json = response.json
        list_comments = ob_json.get('data').get('moduleInfoList')[0].get('moduleData').get('data').get('reviewList')
        if len(list_comments) is 0:
            return
        for comment in list_comments:
            addTime = comment.get('addTime')#创建的时间
            avgPrice = comment.get('avgPrice')#平均价格,int
            browseCount = comment.get('browseCount')#浏览数,int
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
            flowerTotal = comment.get('flowerTotal')#点赞数,int
            followNoteNo = comment.get('followNoteNo')#评论数,int
            honour = comment.get('honour')#int
            id = response.save['id']
            lastTime = comment.get('lastTime')
            lastTimeStr = comment.get('lastTimeStr')
            platform = comment.get('platform')#int
            reviewBody = comment.get('reviewBody')#评论
            reviewId = comment.get('reviewId')#评论者的id,int
            reviewPicNum = comment.get('reviewPicNum')#评论照片的数量,int
            reviewPics = json.dumps(comment.get('reviewPics'))
            reviewdetailUrl = comment.get('reviewdetailUrl')
            star = comment.get('star')#评论的评分,最高50分,int
            userLevelImg = comment.get('userLevelImg')#评论者的账户等级图片
            userNickName = comment.get('userNickName')#评论者的昵称
            userPhoto = comment.get('userPhoto')#评论者的头像
            userPower = comment.get('userPower')#用户的评分,str
            if userPower is u'':
                userPower = 0
            vipLevel = comment.get('vipLevel')#评论者的vip等级
            result.append([addTime,avgPrice,browseCount,crawl_time,flowerTotal,followNoteNo,honour,id,lastTime,lastTimeStr,platform,reviewBody,reviewId,reviewPicNum,reviewPics,reviewdetailUrl,star,userLevelImg,userNickName,userPhoto,userPower,vipLevel])
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO dazhongdianping_comment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # 批量插入
            cur.executemany(sql,result)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()