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

conn=MongoClient('localhost',27017)
db = conn.xiecheng#选择xiecheng数据库,没有自动创建
shops = db.shops# 使用shops集合,没有自动创建
comments = db.comments
for shop in shops.find():
    shop_id = shop.get('shop_id')
    print '正在处理店铺{}~'.format(shop_id)
    dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置userAgent
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1")
    html_context = ''
    obj = webdriver.PhantomJS(executable_path='phantomjs', desired_capabilities=dcap)  # 加载网址
    obj.maximize_window()
    obj.set_page_load_timeout(5)
    # scan_count = 1#表示浏览的序号
    try:
        obj.get('http://m.ctrip.com/webapp/hotel/hoteldetail/dianping/{}.html'.format(shop_id))  # 打开网址
        html_context = obj.page_source
        obj.quit()
    except Exception as e:
        print e
        obj.quit()  # 关闭浏览器。当出现异常时记得在任务浏览器中关闭PhantomJS，因为会有多个PhantomJS在运行状态，影响电脑性能
    # with open('/home/mininet/桌面/1615588.html','w+') as f:
    #     f.write(html_context)

    ###########################
    # with open('/home/mininet/桌面/1615588.html','r') as f:
    #     html_context = f.read()
    ############################
    print '请稍等正在处理数据~'
    time.sleep(3)
    p = pq(html_context)
    for each in p('#content > article > div.js_comment_wrap > div.myhotel-w.js_commentlist > div').items():
        comment_name = each('div > div.hotel-cell.dn-other > div.hotel-cell-num > p:nth-child(1) > span:nth-child(2)').text()
        comment_score = each('div > div.hotel-cell.dn-other > div.g-ve > strong').text()
        comment_count = re.sub(r'[\n ]+',r'',each('div > div.cm > ul > li > div > div > span').text())
        comment_evaluation = each('div > div.cbd.drop--tree.js_arr_rel_content').text()
        comment_grade = each('div > div.hotel-cell.dn-other > div.hotel-cell-num > p:nth-child(2) > span.user-level-base').text()
        comment_room = each('div > div.hotel-cell.dn-other > div.hotel-cell-num > p:nth-child(1) > span.fr.hotel-arr.js_room_layer_trigger').text()
        comment_feature = each('div > div.hotel-cell.dn-other > div.hotel-cell-num > p:nth-child(2) > span.hotel-dp-line.fr > em').text()
        comment_check_in = re.sub(r'[\n ]+',r'',each('div > p.dn-checkin').text())
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        data = {
            'comment_name' : comment_name,
            'comment_score' : comment_score,
            'comment_count': comment_count,
            'comment_evaluation': comment_evaluation,
            'comment_grade': comment_grade,
            'comment_room': comment_room,
            'comment_feature' : comment_feature,
            'comment_check_in' : comment_check_in,
            'crawl_time' : crawl_time
        }
        if len(list(comments.find({
            'comment_name' : comment_name,
            'comment_room': comment_room,
            'comment_check_in': comment_check_in
        }))) == 0:
            comments.insert(data)
        else:
            comments.update({
                'comment_name' : comment_name,
                'comment_room': comment_room,
                'comment_check_in': comment_check_in,
            }, {'$set': {
                'comment_score': comment_score,
                'comment_count': comment_count,
                'comment_evaluation': comment_evaluation,
                'comment_grade': comment_grade,
                'comment_feature': comment_feature,
                'crawl_time': crawl_time
                }
            })
    print '处理数据完成!!!'