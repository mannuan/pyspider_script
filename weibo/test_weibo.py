# -*- coding:utf-8 -*-

# 微博热搜主页 ： https://m.weibo.cn/p/102803_ctg1_8999_-_ctg1_8999_home

# 微博热搜主页的数据 ： https://m.weibo.cn/api/container/getIndex?containerid=102803_ctg1_8999_-_ctg1_8999_home&page={}
# 微博热搜博主发表微博的数据 ： https://m.weibo.cn/api/container/getIndex?uid={}&luicode=10000011&lfid=102803_ctg1_8999_-_ctg1_8999_home%26page%3D1&featurecode=20000320&type=uid&value={}&containerid=107603{}
# 微博热搜博主发表的微博的评论的数据 ：　https://m.weibo.cn/api/comments/show?id={}&page=1


import requests,json,re
import sys,time,pymysql

class Handler(object):
    def on_start(self):
        '''
        获取微博热搜的用户的id
        :return:
        '''
        page=1
        while True:
            url = "https://m.weibo.cn/api/container/getIndex?containerid=102803_ctg1_8999_-_ctg1_8999_home&page={}".format(page)
            page+=1
            reponse = requests.get(url)
            ob_json = json.loads(reponse.text)
            list_cards = ob_json.get('cards')
            if list_cards is None:
                break
            for card in list_cards:
                if card.get('card_type') is 9:
                    mblog = card.get('mblog')
                    user = mblog.get('user')
                    user_id = user.get('id')
                    user_name = user.get('screen_name')
                    crawl_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                                           charset='utf8')
                    cur = conn.cursor()
                    # 先查找是否存在
                    cur.execute("select * from weibo_user where user_id = %s", user_id)
                    rows = cur.fetchall()
                    if len(rows) == 0:
                        cur.execute("insert into weibo_user(user_id,user_name,crawl_time) values(%s,%s,%s)",(user_id, user_name,crawl_time))
                    conn.commit()
                    cur.close()
                    conn.close()
                    self.get_weibo(user_id)

    def get_weibo(self,id):
        '''
        获取热搜博主的发表的微博id
        :param id:表示某位博主的id
        :return:
        '''
        for page in range(1,2):#选取某博主最近发表的10条微博
            url = "https://m.weibo.cn/api/container/getIndex?uid={}&luicode=10000011&lfid=102803_ctg1_8999_-_ctg1_8999_home&featurecode=20000320&type=uid&value={}&containerid=107603{}&page={}".format(id,id,id,page)
            reponse = requests.get(url)
            ob_json = json.loads(reponse.text)
            list_cards = ob_json.get('cards')
            if list_cards is None:
                return
            for card in list_cards:
                if card.get('card_type') is 9:
                    mblog = card.get('mblog')
                    user_id = mblog.get('user').get('id')
                    weibo_id = mblog.get('id')#某条微博的id
                    text = mblog.get('text')
                    reposts_count = mblog.get('reposts_count')#转发数
                    comments_count = mblog.get('comments_count')#评论数
                    attitudes_count = mblog.get('attitudes_count')#点赞数
                    created_at = mblog.get('created_at')
                    crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    print user_id,weibo_id,text,reposts_count,comments_count,attitudes_count,created_at,crawl_time
                    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                    #                        charset='utf8')
                    # cur = conn.cursor()
                    # # 先查找是否存在
                    # cur.execute("select * from weibo_weibo where weibo_id = %s", weibo_id)
                    # rows = cur.fetchall()
                    # if len(rows) == 0:
                    #     cur.execute("insert into weibo_weibo(user_id,weibo_id,text,reposts_count,comments_count,attitudes_count,created_at,crawl_time) values(%s,%s,%s)",(user_id,weibo_id,text,reposts_count,comments_count,attitudes_count,created_at,crawl_time))
                    # conn.commit()
                    # cur.close()
                    # conn.close()
                    # self.get_comment_userid(weibo_id)

    def get_comment_userid(self,id):
        '''
        获取评论微博用户的id
        :param id:表示某条微博的id
        :return:
        '''
        url = "https://m.weibo.cn/api/comments/show?id={}&page=1".format(id)
        reponse = requests.get(url)
        ob_json = json.loads(reponse.text)
        list_comments = ob_json.get('hot_data')
        if list_comments is None:
            return
        for comment in list_comments:
            user = comment.get('user')
            user_id = user.get('id')
            user_name = user.get('screen_name')
            crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print user_id,user_name

if __name__ == '__main__':
    handle = Handler()
    handle.on_start()

