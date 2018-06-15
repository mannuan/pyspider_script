# -*- coding:utf-8 -*-

from lxml import html
import requests,pymysql
import json
import re,time


class DaZhongDianPing(object):

    @classmethod
    def get_shop(cls,cityid,limit,start): #店铺
        '''
        获取店铺的id,一次访问返回最多50个数据
        :return:
        '''
        url = 'https://m.dianping.com/isoapi/module'
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {"moduleInfoList":[{"moduleName":"mapiSearch","query":{"search":{"start":start,"categoryid":"10","parentCategoryId":10,"locatecityid":3,"limit":limit,"sortid":"0","cityid":cityid,"range":"1","maptype":0},"loaders":["list","noResult"]}}],
                "pageEnName":"shopList"}
        response = requests.get(url,headers=headers,data=json.dumps(data))
        # print response.text
        ob_json = json.loads(response.text)
        list_shops = ob_json.get('data').get('moduleInfoList')[0].get('moduleData').get('data')
        if list_shops is None:
            return None
        else:
            if list_shops.get('listData') is None:
                return None
            else:
                return list_shops.get('listData').get('list')

    @classmethod
    def main(cls,cityid):
        limit = 50
        count = 0
        shop_num = 0
        while True:
            # time.sleep(0.5)
            # print count*limit
            list_shops = DaZhongDianPing.get_shop(cityid,limit,count*limit)
            count+=1
            if list_shops is None:
                break
            for shop in list_shops:#遍历
                if(shop.get('adShop') is True):
                    adInfo = json.dumps(shop.get('adInfo'))#广告信息,一个json字符串
                else:
                    adInfo = None
                altName = shop.get('altName')
                authorityLabelType = shop.get('authorityLabelType')#int
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

                #打印
                shop_num+=1
                print(adInfo)
                print('altname : '+altName)
                print('authorityLabelType : '+str(authorityLabelType))
                print('bookType : '+str(bookType))
                print(branchName)
                print('categoryId : '+str(categoryId))
                print('categoryName : '+categoryName)
                print('cityId : '+str(cityId))
                print(defaultPic)
                print(dishtags)
                print('extraJson : '+extraJson)
                print(shopDealInfos)
                print('shop_id : '+str(shop_id))
                print('matchText : '+matchText)
                print('memberCardId : '+str(memberCardId))
                print('shop_name : '+shop_name)
                print('newShop : '+newShop)
                print('orderDish : '+orderDish)
                print(originalUrlKey)
                print('priceText : '+priceText)
                print('recommendReasonData : '+recommendReasonData)
                print('regionName : '+regionName)
                print('reviewCount : '+str(reviewCount))
                print('scoreText : '+scoreText)
                print('shopPositionInfo : '+shopPositionInfo)
                print('shopPower : '+str(shopPower))
                print('shopStateInformation : '+shopStateInformation)
                print('shopType : '+str(shopType))
                print('status : '+str(status))
                print('tag : '+tag)
                print(shop_num)




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
    # citys = {'北京':2,"成都":8,"重庆":9,"广州":4,"杭州":3,"南京":5,"上海":1,"深圳":7,"苏州":6,"天津":10,"武汉":16,"西安":17}
    # for cityid in citys.values():
    #     print cityid
    DaZhongDianPing.main(3602)