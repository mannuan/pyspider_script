#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-28 10:56:18
# Project: lvmama

from pyspider.libs.base_handler import *
from pyquery import PyQuery as pq
import re,time,json
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.tuniu_qiandaohu
shops = db.shops
comments = db.comments


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://s.tuniu.com/search_complex/ticket-hz-0-千岛湖', callback=self.shop_page)

    @config(age=10 * 24 * 60 * 60)
    def shop_page(self, response):
        for each in response.doc('#niuren_list > div.contentcontainer.clearfix > div.content_bottom > div.main.fl > div.thelist > ul > li').items():
            shop_name = each('div.theinfo.ticket.clearfix > a > dl > dt > p > span').text()
            shop_url = each('div.theinfo.ticket.clearfix > a').attr.href
            shop_img = each('div.theinfo.ticket.clearfix > a > div.imgbox > div > img').attr.src
            shop_address = each('div.theinfo.ticket.clearfix > a > dl > dd:nth-child(2)').text()
            shop_time = each('div.theinfo.ticket.clearfix > a > dl > dd.port').text()
            shop_price = float(each('div.theinfo.ticket.clearfix > a > div.priceinfo > span > em').text())
            shop_praise = each('div.theinfo.ticket.clearfix > a > div.priceinfo > div > p > i').text()
            shop_comment = int(re.sub(r'[^\d]*',r'',each('div.theinfo.ticket.clearfix > a > div.priceinfo > div > p > span').text()))
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
            print shop_name,shop_url,shop_comment
            print shop_price
            shop_data = {
                'shop_url':shop_url,
                'shop_name':shop_name,
                'shop_img':shop_img,
                'shop_address':shop_address,
                'shop_time':shop_time,
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

            shop_id = shop_url.split('=')[-1]

            url = 'http://menpiao.tuniu.com/tn?r=ticket/scenic/newRemarkList&currentPage={}&scenicId%5B%5D={}&pageLimit=10'

            for i in range(1,shop_comment/10+10):
                self.crawl(url.format(i,shop_id), callback=self.comment_page, save = {'shop_url':shop_url})



    @config(priority=2)
    def comment_page(self, response):
        comments_len = len(response.json.get('contents'))
        if comments_len == 0:
            return
        shop_url = response.save['shop_url']
        for each in response.json.get('contents'):
            comment_user_name = each.get('user').get('nickname')
            comment_user_level = each.get('user').get('level')
            comment_evaluation = each.get('subGradeContents')
            comment_time = each.get('compTextContent').get('updateTime')
            comment_content = each.get('compTextContent').get('dataSvalue')
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
            print comment_user_name,comment_time,comment_content
            comment_data = {
                'shop_url' : shop_url,
                'comment_user_name':comment_user_name,
                'comment_user_level':comment_user_level,
                'comment_evaluation':comment_evaluation,
                'comment_time':comment_time,
                'comment_content':comment_content,
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