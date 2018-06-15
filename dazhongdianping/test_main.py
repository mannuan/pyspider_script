# -*- coding:utf-8 -*-

from lxml import html
import requests,pymysql
import json
import re,time

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

class DaZhongDianPing(object):

    @classmethod
    def get_shop(cls,limit,start): #店铺
        '''
        获取店铺的id,一次访问返回最多50个数据
        :return:
        '''
        url = 'https://m.dianping.com/isoapi/module'
        headers = {'Content-Type': 'application/json'}
        data = {"moduleInfoList":[{"moduleName":"mapiSearch","query":{"search":{"start":start,"categoryid":"10","parentCategoryId":10,"locatecityid":3,"limit":limit,"sortid":"0","cityid":3,"range":"1","maptype":0},"loaders":["list","noResult"]}}],
                "pageEnName":"shopList"}
        response = requests.get(url,headers=headers,data=json.dumps(data))
        ob_json = json.loads(response.text)
        list_shops = ob_json.get('data').get('moduleInfoList')[0].get('moduleData').get('data').get('listData')
        if list_shops is None:
            return list_shops
        else:
            return list_shops.get('list')

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
        limit = 50
        count = 50
        while True:
            # time.sleep(0.5)
            print(count*limit)
            list_shops = DaZhongDianPing.get_shop(limit,count*limit)
            count+=1
            if list_shops is None:
                break
            for shop in list_shops:#遍历
                if(shop.get('adShop') is True):
                    adInfo = json.dumps(shop.get('adInfo'))#广告信息,一个json字符串
                else:
                    adInfo = None
                altName = shop.get('altName')
                authorityLabelType = shop.get('authorityLabelType')
                if(shop.get('bookable') is True):
                    bookType = shop.get('bookType')#str
                else:
                    bookType = None
                branchName = shop.get('branchName')#店铺所属分支
                categoryId = shop.get('categoryId')#菜系id,int
                categoryName = shop.get('categoryName')#菜系
                cityId = shop.get('cityId')#所在城市的id,int
                defaultPic = shop.get('defaultPic')#店铺的头像
                dishtags = shop.get('dishtags')#菜的种类
                extraJson = shop.get('extraJson')#str
                if(shop.get('hasDeals') is True):
                    shopDealInfos = shop.get('shopDealInfos')
                else:
                    shopDealInfos = None
                shop_id = shop.get('id')#店铺的id,int
                matchText = shop.get('matchText')#店铺的匹配字段
                memberCardId = shop.get('memberCardId')#int
                shop_name = shop.get('name')#店铺的名字
                newShop = str(shop.get('newShop'))#布尔类型
                orderDish = str(shop.get('orderDish'))#布尔类型
                originalUrlKey = shop.get('originalUrlKey')#店铺的头像(原本的大小)
                priceText = shop.get('priceText')#店铺的平均价格
                recommendReasonData = json.dumps(shop.get('recommendReasonData'))
                regionName = shop.get('regionName')#店铺所属的行政区
                reviewCount = shop.get('reviewCount')#店铺的评论数,int
                scoreText = shop.get('scoreText')
                shopPositionInfo = json.dumps(shop.get('shopPositionInfo'))
                shopPower = shop.get('shopPower')#店铺的评分(总分50),int
                shopStateInformation = json.dumps(shop.get('shopStateInformation'))
                shopType = shop.get('shopType')#店铺的类别,int
                status = shop.get('status')#店铺的状态,int
                tagList = shop.get('tagList')
                tag_list = list()
                for tag in tagList:
                    tag_list.append(tag.get('text'))
                tag = json.dumps(tag_list)

                list_comments = DaZhongDianPing.get_comment(shop_id,1)
                if len(list_comments) is 0:
                    continue
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

                    print('addTime : '+addTime)
                    print('avgPrice :'+str(avgPrice))
                    print('browseCount : '+str(browseCount))
                    print('flowerTotal : '+str(flowerTotal))
                    print('followNoteNo : '+str(followNoteNo))
                    print('honour : '+str(honour))
                    print('lastTime : '+lastTime)
                    print('lastTimeStr : '+lastTimeStr)
                    print('platform : '+str(platform))
                    print('reviewBody : '+reviewBody)
                    print('reviewId : '+str(reviewId))
                    print('reviewPicNum : '+str(reviewPicNum))
                    print('reviewPics : '+reviewPics)
                    print('reviewdetailUrl : '+reviewdetailUrl)
                    print('star : '+str(star))
                    print('userLevelImg : '+userLevelImg)
                    print('userNickName : '+userNickName)
                    print('userPhoto : '+userPhoto)
                    print('userPower : '+str(userPower))
                    print('vipLevel : '+str(vipLevel))


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
