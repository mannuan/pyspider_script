# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys,time,json,re
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq
from pymongo import MongoClient

dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1")
html_context = ''
obj = webdriver.PhantomJS(executable_path='phantomjs', desired_capabilities=dcap)  # 加载网址
obj.maximize_window()
obj.set_page_load_timeout(5)
scan_count = 1#表示浏览的序号
try:
    obj.get('http://h5.m.taobao.com/trip/hotel/searchlist/index.html?ttid=12bai0000004&e=kjRQGs7HnSlIGYWvs5y5E4AAksovHygfUR6Co5abHEPcEesopIDDZC_IAR7ok-np8sviUM61dt3AyMgUdz-fmZ4wgOgUxP9jBWqoyfzEffi-NCCc-lX3QU6j1QJSoFwkiiVicoq_k5dqE55nENphhtG5T7v9i6W7Wq_pVe8GRwxbWjXjFLUzDm3CCSTosozIBHHV38ohJK6uVjKj9BvATzhpiYA3a5n9&_preProjVer=1.0.11&_projVer=1.0.11&guid=1521010635587395982&cityName=%E5%8D%83%E5%B2%9B%E6%B9%96&cityCode=100017&adultNum=2&keyWords=%E5%8D%83%E5%B2%9B%E6%B9%96&recKeyword=undefined&checkIn=2018-03-14&checkOut=2018-03-15&isLBS=false&spm=181.7437877.1998398706.9')  # 打开网址
    before_page_source = obj.page_source
    after_page_source = obj.page_source
    print '正在浏览第{}页'.format(scan_count)
    while(True):
        before_page_source = after_page_source
        obj.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # scrollbar = obj.find_element_by_css_selector('#app > div > div > div.flex-remain-height > div.scroller-wrap > div')
        # scrollbar.send_keys(Keys.DOWN)
        scan_count += 1
        print '正在浏览第{}页'.format(scan_count)
        time.sleep(5)
        after_page_source = obj.page_source  # 获取网页文本
        if before_page_source == after_page_source:
            break
    html_context = obj.page_source
    obj.quit()
except Exception as e:
    print e
    obj.quit()  # 关闭浏览器。当出现异常时记得在任务浏览器中关闭PhantomJS，因为会有多个PhantomJS在运行状态，影响电脑性能
# print html_context
# with open('/home/mininet/桌面/飞猪_千岛湖.html','w+') as f:
#     f.write(html_context)

p = pq(html_context)
for each in p('#app > div > div > div.flex-remain-height > div.scroller-wrap > div > div > div > div').items():
    print each('div.text-box > div.card-title').text()

# conn=MongoClient('localhost',27017)
# db = conn.xiecheng#选择xiecheng数据库,没有自动创建
# shops = db.shops# 使用shops集合,没有自动创建
###########################
# with open('/home/mininet/桌面/携程酒店，酒店预订，酒店查询，宾馆住宿预订,网上订酒店-【携程旅行手机版】.html','r') as f:
#     html_context = f.read()
############################
# print html_context
# print '请稍等正在处理数据~'
# time.sleep(3)
# p = pq(html_context)
# for each in p('#content > div > div.lt-m.js_list_container > div.lt-items.js_hotellistinfo > a').items():
#     shop_id = each.attr.href.split('/')[-1].split('.')[0]
#     shop_pic = each('div > div.i-mod > img').attr.src
#     shop_name = each('div > div.c-mod > h3').text()
#     shop_score = each('div > div.c-mod > div:nth-child(2) > span.c-fn > b').text()
#     shop_comment_count = re.sub(r'[^\d]',r'',each('div > div.c-mod > div:nth-child(2) > span.c-be').text())
#     shop_evaluation = each('div > div.c-mod > div:nth-child(2) > span.c-fw').text() + ',' + each('div > div.c-mod > div:nth-child(2) > span.c-dp').text()
#     shop_distance = each('div > div.c-mod > div:nth-child(3) > div > div > span').text()
#     shop_lowest_price = '￥' + re.sub(r'[^\d]',r'',each('div > div.c-mod > div:nth-child(4) > div > span').text())
#     shop_type = each('div > div.c-mod > div:nth-child(4) > div > div > span').text()
#     shop_feature = each('div > div.c-mod > div.item.ellips > span:nth-child(2)').text()
#     crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
#     data = {
#         'shop_id' : shop_id,
#         'shop_pic' : shop_pic,
#         'shop_name': shop_name,
#         'shop_score': shop_score,
#         'shop_comment_count': shop_comment_count,
#         'shop_evaluation': shop_evaluation,
#         'shop_distance' : shop_distance,
#         'shop_lowest_price' : shop_lowest_price,
#         'shop_type' : shop_type,
#         'shop_feature' : shop_feature,
#         'crawl_time' : crawl_time
#     }
#     if len(list(shops.find({
#         'shop_id': shop_id,
#     }))) == 0:
#         shops.insert(data)
#     else:
#         shops.update({
#             'shop_id': shop_id
#         }, {'$set': {
#             'shop_pic': shop_pic,
#             'shop_name': shop_name,
#             'shop_score': shop_score,
#             'shop_comment_count': shop_comment_count,
#             'shop_evaluation': shop_evaluation,
#             'shop_distance': shop_distance,
#             'shop_lowest_price': shop_lowest_price,
#             'shop_type': shop_type,
#             'shop_feature': shop_feature,
#             'crawl_time': crawl_time
#             }
#         })
# print '处理数据完成!!!'