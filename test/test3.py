# -*- coding:utf-8 -*-


from pymongo import MongoClient
import time

MONGODB_PORT = 27017
MONGODB_IP = 'localhost'
CONN = MongoClient(MONGODB_IP, MONGODB_PORT)
MONGODB = CONN.dianping_qiandaohu
shops = MONGODB.shops
shops_data_list = list(shops.find({
    # 'data_website': '大众点评',
    # 'data_region': '千岛湖',
    # 'data_source': '景点',
}))
shops_data_list = list(shops_data_list)
for shop_data in shops_data_list:
    shop_data.pop('_id')
    shop_data.pop('item_count')
    if shop_data.has_key('shop_comment'):
        shop_comment_num = shop_data.get('shop_comment')
        shop_data.pop('shop_comment')
        shop_data.setdefault('shop_comment_num',shop_comment_num)
    if shop_data.has_key('shop_feature'):
        shop_title = shop_data.get('shop_feature')
        shop_data.pop('shop_feature')
        shop_data.setdefault('shop_title',shop_title)
    shop_data['data_website']= '大众点评'
    shop_data['data_region']='千岛湖'
    shop_data['data_source']= '景点'
    shop_data['crawl_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
    # key = {
    # 'data_website': '大众点评',
    # 'data_region': '千岛湖',
    # 'data_source': '景点',
    #     'shop_id':comment_data.get('shop_id'),
    # }
    CONN.dspider2.shops.insert(shop_data)
    print shop_data
# print comments_data_list