#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-28 10:56:18
# Project: lvmama

from pyspider.libs.base_handler import *
from pyquery import PyQuery as pq
import re,time,json
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.lvmama_qiandaohu
shops = db.shops
comments = db.comments


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        url = 'http://s.lvmama.com/ticket/P{}?keyword=千岛湖&tabType=ticket'
        for i in range(3):
            self.crawl(url.format(i+1), callback=self.shop_page)

    @config(age=10 * 24 * 60 * 60)
    def shop_page(self, response):
        for each in response.doc('body > div.everything > div.main.clearfix > div.main-content.clearfix > div.product-list > div').items():
            shop_name = each('div.product-regular.clearfix > div.product-section > h3 > a').text()
            if '千岛湖' not in shop_name:
                continue
            shop_url = each('div.product-regular.clearfix > div.product-info > a').attr.href
            shop_img = each('div.product-regular.clearfix > div.product-left > a > img').attr.src
            shop_address = ''
            shop_time = ''
            shop_topic = ''
            shop_activity = ''
            shop_feature = ''
            for each1 in each('div.product-regular.clearfix > div.product-section > dl').items():
                if '景点地址' in each1.text():
                    shop_address = each1.text()
                elif '营业时间' in each1.text():
                    shop_time = each1.text()
                elif '精彩活动' in each1.text():
                    shop_activity = each1.text()
                elif '景点特色' in each1.text():
                    shop_feature = each1.text()
                else:
                    shop_topic = each1.text()
            shop_level = each('div.product-regular.clearfix > div.product-section > h3 > span.level').text()
            shop_price = float(each('div.product-regular.clearfix > div.product-info > div > em').text())
            shop_praise = each('div.product-regular.clearfix > div.product-info > ul > li:nth-child(1) > b').text()
            shop_comment = int(re.sub(r'[^\d]*',r'',each('div.product-regular.clearfix > div.product-info > ul > li:nth-child(2) > a').text()))
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
            print shop_name,shop_price,shop_url,shop_comment,shop_topic
            shop_data = {
                'shop_name':shop_name,
                'shop_url' :shop_url,
                'shop_img':shop_img,
                'shop_address':shop_address,
                'shop_time':shop_time,
                'shop_topic':shop_topic,
                'shop_activity':shop_activity,
                'shop_feature': shop_feature,
                'shop_level':shop_level,
                'shop_price':shop_price,
                'shop_praise':shop_praise,
                'shop_comment':shop_comment,
                'shop_type':'景点',
                'crawl_time':crawl_time
            }
            if len(list(shops.find({
                'shop_url': shop_url,
            }))) == 0:
                shops.insert(shop_data)
            else:
                shops.update({
                    'shop_url': shop_url,
                }, {'$set': shop_data
                })

            shop_id = shop_url.split('-')[-1]
            url = 'http://ticket.lvmama.com/vst_front/comment/newPaginationOfComments?page={}&id={}'

            for i in range(1,shop_comment/10+10):
                data = 'type=all&currentPage={}&totalCount={}&placeId={}'.format(i,shop_comment,shop_id)
                self.crawl(url.format(i,shop_id), method='POST', data=data, callback=self.comment_page, save = {'shop_url':shop_url})



    @config(priority=2)
    def comment_page(self, response):
        shop_url = response.save['shop_url']
        try:
            response.doc('div.comment-li')
        except Exception:
            return
        for each in response.doc('div.comment-li').items():
            comment_user_name = each('div.com-userinfo > p > a:nth-child(1)').text()
            if comment_user_name is None:
                break
            comment_time = each('div.com-userinfo > p > em').text()
            comment_content = each('div.ufeed-content').text()
            comment_reply = each('div.com-userinfo > a.JS_reply.fr.com-dcom > em').text()
            comment_useful = each('#userfulCount_all_65890 > em').text()
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
            print comment_user_name,comment_time,comment_content
            comment_data = {
                'shop_url' : shop_url,
                'comment_user_name':comment_user_name,
                'comment_time':comment_time,
                'comment_content':comment_content,
                'comment_reply':comment_reply,
                'comment_useful':comment_useful,
                'crawl_time':crawl_time,
            }
            if len(list(comments.find({
                'shop_url': shop_url,
                'comment_user_name':comment_user_name,
                'comment_time':comment_time,
            }))) == 0:
                comments.insert(comment_data)
            else:
                comments.update({
                    'shop_url': shop_url,
                    'comment_user_name': comment_user_name,
                    'comment_time': comment_time,
                }, {'$set': comment_data
                })

