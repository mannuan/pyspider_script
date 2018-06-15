# -*- coding:utf-8 -*-

from lxml import html
import requests,pymysql
import json
import re,time


class DaZhongDianPing(object):

    @classmethod
    def get_comment(cls,shop_id,page):#店铺的评论
        '''
        获取店铺的评论
        :return:
        '''
        url = 'https://m.dianping.com/isoapi/module'
        headers = {'Content-Type': 'application/json'}
        data = {"moduleInfoList": [{"moduleName": "reviewlist", "query": {"shopId": str(shop_id), "page": page}}],
                "pageEnName": "shopreviewlist"}
        response = requests.get(url, headers=headers, data=json.dumps(data))
        ob_json = json.loads(response.text)
        list_comments = ob_json.get('data').get('moduleInfoList')[0].get('moduleData').get('data').get('reviewList')
        # print len(list_comments)
        return list_comments

    @classmethod
    def main(cls):

        list_comments = DaZhongDianPing.get_comment(shop_id,1)
        if len(list_comments) is 0:
            return
        for comment in list_comments:
            addTime = comment.get('addTime')#创建的时间
            avgPrice = comment.get('avgPrice')#平均价格,int
            browseCount = comment.get('browseCount')#浏览数,int
            flowerTotal = comment.get('flowerTotal')#点赞数,int
            followNoteNo = comment.get('followNoteNo')#评论数,int
            honour = comment.get('honour')#int
            lastTime = comment.get('lastTime')
            lastTimeStr = comment.get('lastTimeStr')
            platform = comment.get('platform')#int
            reviewBody = comment.get('reviewBody')#评论
            reviewId = comment.get('reviewId')#评论者的id,int
            reviewPicNum = comment.get('reviewPicNum')#评论照片的数量,int
            reviewPics = json.dumps(comment.get('reviewPics'))
            reviewdetailUrl = comment.get('reviewdetailUrl')
            star = comment.get('star')#评论的评分,最高50分,int
            userLevelImg = comment.get('userLevelImg')#评论者的账户等级图片
            userNickName = comment.get('userNickName')#评论者的昵称
            userPhoto = comment.get('userPhoto')#评论者的头像
            userPower = comment.get('userPower')#用户的评分,int
            vipLevel = comment.get('vipLevel')#评论者的vip等级

            # print u'addTime : '+addTime
            # print 'avgPrice :'+str(avgPrice)
            # print 'browseCount : '+str(browseCount)
            # print 'flowerTotal : '+str(flowerTotal)
            # print 'followNoteNo : '+str(followNoteNo)
            # print 'honour : '+str(honour)
            # print u'lastTime : '+lastTime
            # print u'lastTimeStr : '+lastTimeStr
            # print u'platform : '+str(platform)
            # print u'reviewBody : '+reviewBody
            # print u'reviewId : '+str(reviewId)
            # print u'reviewPicNum : '+str(reviewPicNum)
            # print 'reviewPics : '+reviewPics
            # print 'reviewdetailUrl : '+reviewdetailUrl
            # print 'star : '+str(star)
            # print 'userLevelImg : '+userLevelImg
            # print u'userNickName : '+userNickName
            # print 'userPhoto : '+userPhoto
            # print 'userPower : '+str(userPower)
            # print 'vipLevel : '+str(vipLevel)


if __name__ == '__main__':
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository',db='repository',charset='utf8')
    # cur = conn.cursor()
    # # 先查找是否存在
    # cur.execute("select user_id from weibo_user")
    # rows = cur.fetchall()
    # conn.commit()
    # cur.close()
    # conn.close()
    # for id in rows:
    #     Weibo.main(id[0], 1)
    DaZhongDianPing.main()
