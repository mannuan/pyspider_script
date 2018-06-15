#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-16 20:55:58
# Project: 大众点评_店铺_未设置延迟

from pyspider.libs.base_handler import *
import json,re,sys,time
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo import MongoClient


class Handler(BaseHandler):
    crawl_config = {
        "headers" : {
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1',
        }
    }

    conn = MongoClient('localhost', 27017)
    db = conn.dazhongdianping #连接dazhongdianping数据库，没有则自动创建
    shops = db.shops #使用shops集合,没有则自动创建
    categorynavs = db.categorynavs

    @every(minutes=24 * 60)
    def on_start(self):
        for i in range(43):
            start = i*50+1
            limit = 50
            url = "http://mapi.dianping.com/searchshop.json?start={}&categoryid=0&parentCategoryId=0&locatecityid=3602&limit={}&pagemodule=msiteseoshoplist&sortid=0&cityid=3602&keyword=千岛湖&regionid=0&maptype=0".format(start,limit)
            self.crawl(url, callback=self.shop_page)
        url = "http://mapi.dianping.com/searchshop.json?start={}&categoryid=0&parentCategoryId=0&locatecityid=3602&limit={}&pagemodule=msiteseoshoplist&sortid=0&cityid=3602&keyword=千岛湖&regionid=0&maptype=0".format(0,1)
        self.crawl(url, callback=self.categorynav_page)

    @config(age=10 * 24 * 60 * 60)
    def shop_page(self, response):
        ob_json = response.json
        list_shop = ob_json.get('list')
        queryid = ob_json.get('queryId')
        for shop in list_shop:
            id = shop.get('id')
            self.crawl('http://m.dianping.com/shop/{}/map'.format(id), fetch_type='js', save={
                'shop': shop,
                'queryid': queryid
            },
                       callback=self.shop_address_page)

    @config(priority=2)
    def shop_address_page(self, response):
        shop = response.save['shop']
        obj = response.text.split('window.PAGE_INITIAL_STATE = ')[1].split(';\n    </script>')[0]
        address = json.loads(obj).get('_context').get('pageInitData').get('address')
        shop.setdefault('address',address)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        shop.setdefault('crawl_time', crawl_time)
        if len(list(self.shops.find({
            'id': shop.get('id')
        }))) == 0:
            self.shops.insert(shop)
        else:
            self.shops.update({
                'id': shop.get('id')
            }, {'$set': shop
            })

    @config(age=10 * 24 * 60 * 60)
    def categorynav_page(self, response):
        ob_json = response.json
        list_categorynav = ob_json.get('categoryNavs')
        for categorynav in list_categorynav:
            if len(list(self.categorynavs.find({
                'id': categorynav.get('id')
            }))) == 0:
                self.categorynavs.insert(categorynav)
            else:
                self.categorynavs.update({
                    'id': categorynav.get('id')
                }, {'$set': categorynav
                })
    #
    # @config(priority=2)
    # def detail_page(self, response):
    #     return {
    #         "url": response.url,
    #         "title": response.doc('title').text(),
    #     }