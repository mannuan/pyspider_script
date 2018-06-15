# -*- coding:utf-8 -*-

from pyspider.libs.base_handler import *
import json,pymysql,time


class Handler(BaseHandler):
    crawl_config = {
        'headers': {'Content-Type': 'application/json; charset=utf-8'}
    }

    @every(minutes=24 * 60)
    def on_start(self):
        for page in range(1,22):
            url = 'http://m.elong.com/hotel/api/list?city=1233&pageindex={}'.format(page)
            self.crawl(url, callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        ob_json = response.json
        list_shops = ob_json.get('hotelList')
        if list_shops is None:
            return None
        for shop in list_shops:  # 遍历
            businessAreaName = shop.get('businessAreaName')
            commentPoint = shop.get('commentPoint')
            commentScore = shop.get('commentScore')  # int
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            districtName = shop.get('districtName')
            hotelName = shop.get('hotelName')
            id = str(shop.get('detailPageUrl')).split('hotel/')[1].split('/#indate')[0]
            lmOriPrice = shop.get('lmOriPrice')  # int
            lowestPrice = shop.get('lowestPrice')  # int
            minPriceInventories = shop.get('minPriceInventories')
            minPriceSubCouponInventories = json.dumps(shop.get('minPriceSubCouponInventories'))
            picUrl = shop.get('picUrl')
            placeName = shop.get('placeName')
            starLevel = shop.get('starLevel')  # int
            totalCommentCount = shop.get('totalCommentCount')#int
            trafficInfo = shop.get('trafficInfo')
            result = [businessAreaName,commentPoint,commentScore,crawl_time,districtName,hotelName,id,lmOriPrice,lowestPrice,minPriceInventories,minPriceSubCouponInventories,picUrl,placeName,starLevel,totalCommentCount,trafficInfo]
            url = 'http://m.elong.com/hotel/{}/'.format(id)
            self.crawl(url, fetch_type = 'js', save={'result':result}, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        address = response.doc('div.addr').text()
        result = [address]
        result.extend(response.save['result'])
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO elong_shop values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
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