# -*- coding:utf-8 -*-

from lxml import html
import requests,pymysql
import json
import re

#加载微博参数 uid,containerid
#评论请求需要参数 id,page

# uid:5044281310
# containerid:107603 + uid

#实例方法和类方法 self 是实例方法　cls　是类方法

#正则表达式的元字符 . * ?
class Tool:
    #去除img标签
    removeImg = re.compile('<img.*>| {1,7}|&nbsp;')
    #去除超链接 a标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行换成\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')

    #去除所有标签
    removeTag = re.compile('<.*?>')

    @classmethod
    def replace(cls,x):
        x = re.sub(cls.removeImg,'',x)
        x = re.sub(cls.removeAddr,'',x)
        x = re.sub(cls.replaceLine,'',x)
        x = re.sub(cls.removeTag,'',x)

        return x.strip()#去掉多余的内容

class Weibo(object):

    @classmethod
    def get_weibo(cls,id,page): #个人id
        '''
        获取指定博主的所有微博
        :param id:表示博主的id
        :param page:表示博主的微博页数
        :return: list_cards
        '''
        url = "https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}&containerid=107603{}&page={}".format(id,id,id,page)
        reponse = requests.get(url)
        ob_json = json.loads(reponse.text)
        list_cards = ob_json.get('cards')
        return list_cards

    @classmethod
    def get_comment(cls,id,page):#微博id
        '''
        获取某条微博的所有评论
        :param id:表示微博的id
        :param page:表示微博评论的页数，热门的评论一定在第一页
        :return:
        '''
        url = "https://m.weibo.cn/api/comments/show?id={}&page={}".format(id,page)
        response = requests.get(url)
        ob_json = json.loads(response.text)
        list_comments = ob_json.get('hot_data')
        if list_comments is None:
            list_comments = ob_json.get('data')
            if list_comments is None:
                return list_comments
            elif len(list_comments) >=9:
                return list_comments[0:9]
        return list_comments

    @classmethod
    def main(cls,uid,page):
        '''
        爬取制定微博用户的指定页面的微博和评论
        :param uid:表示用户的id
        :param page:表示博主的微博页数
        :return:
        '''
        list_cards = Weibo.get_weibo(uid,page)
        for card in list_cards:#遍历
            if card.get('card_type') == 9:#等于9的微博才是正文,其他的都是推荐或者其他,`weibo_user`的唯一标识
                mblog_user_id = card.get('mblog').get('user').get('id')#微博用户的id
                mblog_user_name = card.get('mblog').get('user').get('screen_name')#微博用户的昵称
                mblog_id = card.get('mblog').get('id')#微博的id,`weibo_weibo`table的唯一标识
                mblog_created_at = card.get('mblog').get('created_at')#微博创建的时间
                mblog_source = card.get('mblog').get('source')#微博的来源
                if mblog_source == '':
                    mblog_source = u'未知'
                mblog_text = card.get('mblog').get('text')
                mblog_text = Tool.replace(mblog_text)#微博的内容
                mblog_reposts_count = card.get('mblog').get('reposts_count')#微博的转发数
                mblog_comments_count = card.get('mblog').get('comments_count')#微博的评论数
                mblog_attitudes_count = card.get('mblog').get('attitudes_count')#微博的点赞数

                if len(mblog_text) is 0:#如果发表的微博里面没有文字,继续
                    continue

                print u'***'+mblog_user_name
                print u'***'+mblog_created_at+u'***来自***'+mblog_source
                print u'@@@微博：'+mblog_text
                print '***转发数***：'+str(mblog_reposts_count)+'***评论数***：'+str(mblog_comments_count)+\
                    '***点赞数***：'+str(mblog_attitudes_count)+'\n'

                list_comments = Weibo.get_comment(mblog_id,1)#热门评论只选第一页
                if list_comments is None:#如果发表的微博里面没有评论,则继续
                    continue

                # count_hotcomments = 1
                for comment in list_comments:
                    comment_user_id = comment.get('user').get('id')#发表评论者的id
                    comment_user_name = comment.get('user').get('screen_name')#发表评论者的昵称
                    comment_created_at = comment.get('created_at')#创建的时间
                    comment_like_counts = comment.get('like_counts')#点赞数
                    comment_text = comment.get('text')
                    tree = html.fromstring(comment_text)
                    comment_text = tree.xpath('string(.)')#微博内容,用string函数过滤多余标签
                    comment_source = comment.get('source')#来自那个哪个设备
                    if comment_source == '':
                        comment_source = u'未知'

                    print u'***'+comment_user_name
                    print u'***'+comment_created_at+u'***点赞数***'+str(comment_like_counts)
                    print u'@@@评论：'+comment_text
                    print u'来自***'+comment_source+'\n'
                    # count_hotcomments += 1
                print '================'



if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository',db='repository',charset='utf8')
    cur = conn.cursor()
    # 先查找是否存在
    cur.execute("select user_id from weibo_user")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    for id in rows:
        Weibo.main(id[0], 1)
