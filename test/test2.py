# -*- coding:utf-8 -*-


from pymongo import MongoClient
import time

MONGODB_PORT = 27017
MONGODB_IP = 'localhost'
CONN = MongoClient(MONGODB_IP, MONGODB_PORT)
MONGODB = CONN.dianping_qiandaohu
comments = MONGODB.comments
comments_data_list = list(comments.find({
    # 'data_website': '大众点评',
    # 'data_region': '千岛湖',
    # 'data_source': '景点',
}))
comments_data_list = list(comments_data_list)
for comment_data in comments_data_list:
    comment_data.pop('_id')
    if comment_data.has_key('comment_star'):
        comment_grade = comment_data.get('comment_star')
        comment_data.pop('comment_star')
        comment_data.setdefault('comment_grade',comment_grade)
    if comment_data.has_key('comment_img'):
        comment_pic_list = comment_data.get('comment_img')
        comment_data.setdefault('comment_pic_list',comment_pic_list)
        comment_data.pop('comment_img')
    comment_like_num = comment_data.get('comment_like')
    comment_data.setdefault('comment_like', comment_like_num)
    comment_data.pop('comment_like')
    comment_replay_num = comment_data.get('comment_replay')
    comment_data.setdefault('comment_replay', comment_replay_num)
    comment_data.pop('comment_replay')
    if comment_data.has_key('comment_user_pic'):
        comment_user_img = comment_data.get('comment_user_pic')
        comment_data.setdefault('comment_user_img', comment_user_img)
        comment_data.pop('comment_user_pic')
    if comment_data.has_key('comment_list_url'):
        comment_url = comment_data.get('comment_list_url')
        comment_data.setdefault('comment_url', comment_url)
        comment_data.pop('comment_list_url')
    comment_data['crawl_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
    if comment_data.has_key('page'):
        comment_data.pop('page')
    if comment_data.has_key('item_count'):
        comment_data.pop('item_count')
    comment_data['data_website']= '大众点评'
    comment_data['data_region']='千岛湖'
    comment_data['data_source']= '景点'
    # key = {
    # 'data_website': '大众点评',
    # 'data_region': '千岛湖',
    # 'data_source': '景点',
    #     'shop_id':comment_data.get('shop_id'),
    # }
    CONN.dspider2.comments.insert(comment_data)
# print comments_data_list