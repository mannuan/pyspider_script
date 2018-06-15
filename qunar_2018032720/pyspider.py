#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-28 10:56:18
# Project: lvmama

from pyspider.libs.base_handler import *
from pyquery import PyQuery as pq
import re,time,json
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.qunar_qiandaohu
shops = db.shops
comments = db.comments


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        url = 'http://piao.qunar.com/ticket/list.json?keyword=千岛湖&region=undefined&from=qunarindex&in_track=index_tab_search&page={}'
        for i in range(1,8):
            self.crawl(url.format(i), callback=self.shop_page)

    @config(age=10 * 24 * 60 * 60)
    def shop_page(self, response):
        shop_list = response.json.get('data').get('sightList')
        for each in shop_list:
            shop_name = each.get('sightName')
            shop_id = each.get('sightId')
            shop_img = each.get('sightImgURL')
            shop_address = each.get('address')
            # shop_grade = float(each.get('score'))
            shop_feature = each.get('intro')
            try:
                shop_price = float(each.get('qunarPrice'))
            except Exception:
                shop_price = 0
            shop_volume = int(each.get('saleCount'))
            shop_rate = each.get('star')
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
            print shop_name,shop_price,shop_id,shop_volume,shop_feature
            shop_data = {
                'shop_name':shop_name,
                'shop_id' :shop_id,
                'shop_img':shop_img,
                'shop_address':shop_address,
                'shop_feature': shop_feature,
                'shop_rate':shop_rate,
                'shop_price':shop_price,
                # 'shop_grade':shop_grade,
                'shop_volume':shop_volume,
                'shop_type':'景点',
                'crawl_time':crawl_time
            }
            url = 'http://piao.qunar.com/ticket/detail_{}.html'.format(shop_id)
            self.crawl(url, callback=self.shop_page2, save={'shop_data': shop_data})

    @config(priority=2)
    def shop_page2(self, response):
        try:
            shop_grade = float(response.doc('#mp-description-commentscore > span').text())
        except Exception:
            shop_grade = 0
        shop_weather = response.doc('#mp-description-weather > span.mp-description-val').text()
        shop_comment = response.doc('.mp-description-commentCount > a').text()
        print shop_comment
        try:
            shop_comment = int(re.sub(r'[^\d]*',r'',shop_comment))
        except Exception:
            shop_comment = 0
        shop_data = dict(response.save['shop_data'],**{
            'shop_grade':shop_grade,
            'shop_weather':shop_weather,
            'shop_comment':shop_comment,
        })
        shop_id = response.save['shop_data'].get('shop_id')
        if len(list(shops.find({
            'shop_id': shop_id,
        }))) == 0:
            shops.insert(shop_data)
        else:
            shops.update({
                'shop_id': shop_id,
            }, {'$set': shop_data
            })
        sight_id = response.doc('#mp-tickets').attr('data-sightid')
        url = 'http://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId={}&index={}&page={}&pageSize=10&tagType=0'
        for i in range(1,shop_comment/10+10):
            self.crawl(url.format(sight_id,i,i), callback=self.comment_page,save={'shop_id': shop_id})

    @config(priority=2)
    def comment_page(self, response):
        shop_id = response.save['shop_id']
        try:
            comment_list = response.json.get('data').get('commentList')
        except Exception:
            return
        if not comment_list:
            return
        for each in comment_list:
            shop_id = shop_id
            comment_user_name = each.get('author')
            comment_id = each.get('commentId')
            commnet_content = each.get('content')
            comment_time = each.get('date')
            comment_img = each.get('imgs')
            comment_grade = each.get('score')
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
            comment_data = {
                'shop_id':shop_id,
                'comment_user_name':comment_user_name,
                'comment_id':comment_id,
                'commnet_content':commnet_content,
                'comment_time':comment_time,
                'comment_img':comment_img,
                'comment_grade':comment_grade,
                'crawl_time':crawl_time,
            }
            print comment_id,comment_user_name,comment_time,commnet_content
            if len(list(comments.find({
                'shop_id': shop_id,
                'comment_id':comment_id,
            }))) == 0:
                comments.insert(comment_data)
            else:
                comments.update({
                    'shop_id': shop_id,
                    'comment_id': comment_id,
                }, {'$set': comment_data
                })

