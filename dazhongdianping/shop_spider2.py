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
        limit = 50
        cityid=3602
        for i in range(120):
            start = i*limit
            url = 'http://m.dianping.com/isoapi/module'
            url += "?start={}&cityid={}".format(start,cityid)
            data = {"moduleInfoList":[{"moduleName":"mapiSearch","query":{"search":{"start":start,"limit":limit,"cityid":cityid},"loaders":["list"]}}],"pageEnName":"shopList"}
            data = json.dumps(data)
            self.crawl(url, method='POST', data=data, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        ob_json = response.json
        list_shops = ob_json.get('data').get('moduleInfoList')[0].get('moduleData').get('data')
        if list_shops is None:
            return
        else:
            if list_shops.get('listData') is None:
                return
            else:
                list_shops = list_shops.get('listData').get('list')
        for shop in list_shops:  # 遍历
            authorityLabelType = shop.get('authorityLabelType')  # int
            branchName = shop.get('branchName')  # 店铺所属分支
            categoryId = shop.get('categoryId')  # 菜系id,int
            categoryName = shop.get('categoryName')  # 菜系
            cityId = shop.get('cityId')  # 所在城市的id,int
            defaultPic = shop.get('defaultPic')  # 店铺的头像
            dishtags = shop.get('dishtags')  # 菜的种类
            id = shop.get('id')  # 店铺的id,int
            matchText = shop.get('matchText')  # 店铺的匹配字段
            name = shop.get('name')  # 店铺的名字
            newShop = str(shop.get('newShop'))  # 布尔类型
            orderDish = str(shop.get('orderDish'))  # 布尔类型
            priceText = shop.get('priceText')  # 店铺的平均价格
            regionName = shop.get('regionName')  # 店铺所属的行政区
            reviewCount = shop.get('reviewCount')  # 店铺的评论数,int
            scoreText = shop.get('scoreText')
            shopPower = shop.get('shopPower')  # 店铺的评分(总分50),int
            shopType = shop.get('shopType')  # 店铺的类别,int
            status = shop.get('status')  # 店铺的状态,int
            tagList = shop.get('tagList')
            if tagList is None:
                tag = None
            else:
                tag_list = list()
                for tag in tagList:
                    tag_list.append(tag.get('text'))
                tag = ''
                for tl in tag_list:
                    tag += tl+','

            result = []
            result.extend([authorityLabelType,branchName,categoryId,categoryName,cityId,defaultPic,dishtags,id,matchText,name,newShop,orderDish,priceText,regionName,reviewCount,scoreText,shopPower,shopType,status,tag])
            # print id
            self.crawl('http://m.dianping.com/shop/{}/map'.format(id), fetch_type='js', save={'result':result}, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        obj = response.text.split('window.PAGE_INITIAL_STATE = ')[1].split(';\n    </script>')[0]
        address = json.loads(obj).get('_context').get('pageInitData').get('address')
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        result = [address,crawl_time]
        result.extend(response.save['result'])
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO dazhongdianping_shop values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # 批量插入
            cur.execute(sql,result)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()