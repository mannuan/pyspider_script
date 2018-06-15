# -*- coding:utf-8 -*-

from lxml import html
import requests,pymysql
import json
import re,time


class ELong(object):

    @classmethod
    def get_shop(cls,page): #店铺
        '''
        获取店铺的id,一次访问返回20个数据,共21页
        :return:
        '''
        url = 'http://m.elong.com/hotel/api/list?city=1233&pageindex={}'.format(page)
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.get(url,headers=headers)
        ob_json = json.loads(response.text)
        list_shops = ob_json.get('hotelList')
        if list_shops is None:
            return None
        else:
            return list_shops

    @classmethod
    def main(cls):
        for page in range(1,22):
            # time.sleep(0.5)
            # print count*limit
            list_shops = ELong.get_shop(page)
            if list_shops is None:
                break
            for shop in list_shops:#遍历
                activityTags = json.dumps(shop.get('activityTags'))
                baiduLatitude = shop.get('baiduLatitude')
                baiduLongitude = shop.get('baiduLongitude')
                businessAreaName = shop.get('businessAreaName')
                calDistanceType = shop.get('calDistanceType')#int
                commentPoint = shop.get('commentPoint')
                commentScore = shop.get('commentScore')#int
                detailPageUrl = shop.get('detailPageUrl')
                distance = shop.get('distance')
                distanceName = shop.get('distanceName')
                districtName = shop.get('districtName')
                facilityList = json.dumps(shop.get('facilityList'))
                hongbao = shop.get('hongbao')#int
                hotelBadge = shop.get('hotelBadge')#int
                hotelName = shop.get('hotelName')
                leftRoomCountShow = shop.get('leftRoomCountShow')
                lmOriPrice = shop.get('lmOriPrice')#int
                lowestPrice = shop.get('lowestPrice')#int
                minPriceInventories = shop.get('minPriceInventories')
                minPriceSubCouponInventories = shop.get('minPriceSubCouponInventories')
                newRecallReason = shop.get('newRecallReason')
                picUrl = shop.get('picUrl')
                placeName = shop.get('placeName')
                specialDay = shop.get('specialDay')
                starLevel = shop.get('starLevel')#int
                syncfacilityList = shop.get('syncfacilityList')
                tags = json.dumps(shop.get('tags'))
                totalCommentCount = shop.get('totalCommentCount')#int
                trafficInfo = shop.get('trafficInfo')

                #打印
                print 'activityTags : ',
                print activityTags
                print 'baiduLatitude : ',
                print baiduLatitude
                print 'baiduLongitude : ',
                print baiduLongitude
                print 'businessAreaName : ',
                print businessAreaName
                print 'calDistanceType',
                print calDistanceType
                print 'commentPoint : ',
                print commentPoint
                print 'commentScore : ',
                print commentScore
                print 'detailPageUrl : ',
                print detailPageUrl
                print 'distance : ',
                print distance
                print 'distanceName : ',
                print distanceName
                print 'districtName : ',
                print districtName
                print 'facilityList : ',
                print facilityList
                print 'hongbao : ',
                print hongbao
                print 'hotelBadge : ',
                print hotelBadge
                print 'hotelName : ',
                print hotelName
                print 'leftRoomCountShow : ',
                print leftRoomCountShow
                print 'lmOriPrice : ',
                print lmOriPrice
                print 'lowestPrice : ',
                print lowestPrice
                print 'minPriceInventories : ',
                print minPriceInventories
                print 'minPriceSubCouponInventories : ',
                print minPriceSubCouponInventories
                print 'newRecallReason : ',
                print newRecallReason
                print 'picUrl : ',
                print picUrl
                print 'placeName : ',
                print placeName
                print 'specialDay : ',
                print specialDay
                print 'starLevel : ',
                print starLevel
                print 'syncfacilityList : ',
                print syncfacilityList
                print 'tags : ',
                print tags
                print 'totalCommentCount : ',
                print totalCommentCount
                print 'trafficInfo : ',
                print trafficInfo


if __name__ == '__main__':
    ELong.main()