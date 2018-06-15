# -*- coding:utf-8 -*-

from selenium import webdriver
import time,random,re,sys,json
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn.feizhu_qiandaohu  # 连接feizhu_qiandaohu数据库，没有则自动创建
shops = db.shops  # 使用shops集合,没有则自动创建
comments = db.comments  # 使用comments集合,没有则自动创建

service_args=[]
service_args.append('--load-images=no')
service_args.append('--disk-cache=yes')
service_args.append('--ignore-ssl-errors=true')
driver = webdriver.Chrome(service_args=service_args)
driver.get("https://www.baidu.com")
driver.set_page_load_timeout(15)
driver.implicitly_wait(15)#隐性等待

driver.find_element_by_id("kw").send_keys(u"飞猪")
time.sleep(1)
driver.find_element_by_id("su").click()
time.sleep(1)
driver.find_elements_by_partial_link_text(u"飞猪：国内外机票、酒店、火车票、旅游度假预订！")[0].click()
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_css_selector("input").click()
driver.find_element_by_css_selector("input").clear()
driver.find_element_by_css_selector("input").send_keys(u"千岛湖")
driver.find_element_by_css_selector("div.ts-search-btn > button").click()
driver.find_element_by_xpath("//div[@id='content']/div[3]/table/tbody/tr/td[4]/div/span").click()

def getShopInfo2(driver,shop_url):
    shop_time = driver.find_element_by_css_selector('#ticket-page > div > div:nth-child(2) > div.col-main > div > div > div:nth-child(2) > div.scenic-sell-info-wrap > div > dl:nth-child(3) > dd').text
    shop_volume = int(driver.find_element_by_css_selector('#ticket-page > div > div:nth-child(2) > div.col-main > div > div > div:nth-child(2) > div.scenic-sell-info-wrap > div > dl.sell-count > dd > em').text)
    shop_address = driver.find_element_by_css_selector('#ticket-page > div > div:nth-child(2) > div.col-main > div > div > div:nth-child(2) > div.scenic-sell-info-wrap > div > dl:nth-child(5) > dd:nth-child(2)').text
    shop_phone = driver.find_element_by_css_selector('#ticket-page > div > div:nth-child(2) > div.col-main > div > div > div:nth-child(2) > div.scenic-sell-info-wrap > div > dl:nth-child(2) > dd').text
    shop_data = {'shop_time':shop_time,'shop_volume':shop_volume,'shop_address':shop_address,'shop_phone':shop_phone}
    return shop_data

def getShopInfo(driver):
    for each in driver.find_elements_by_css_selector('#content > div.page-products-block.clear-fix > div.page-products-block-left.clear-fix > div.product-list-wrap > div > div'):
        try:
            shop_url = each.find_element_by_css_selector('div.product-right > div > a').get_attribute('href')
        except Exception:
            break
        shop_img = each.find_element_by_css_selector('div.product-left > a > div > img').get_attribute('data-src')
        shop_name = each.find_element_by_css_selector('div.product-middle > div.title-wrap > a > h3').text
        print shop_name
        try:
            shop_rate_available = each.find_element_by_css_selector('div.product-middle > div.tag-list-wrap > ul').text
            shop_rate = shop_rate_available.replace('可订今日票','').strip()
            shop_available = (lambda s:'可订今日票' if '可订今日票' in s else '')('可订今日票').strip()
        except Exception:
            shop_rate = ''
            shop_available = ''
        shop_feature = each.find_element_by_css_selector('div.product-middle > p.other-msg > span').text
        shop_price = each.find_element_by_css_selector('div.product-right > div > div').text
        each.find_element_by_css_selector('div.product-right > div > a').click()
        driver.switch_to_window(driver.window_handles[1])#切换到评论窗口
        shop_data = getShopInfo2(driver,shop_url)#获取评论数据
        driver.close()#关闭评论窗口
        driver.switch_to_window(driver.window_handles[0])#切换为店铺列表页面
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        shop_data = dict(shop_data,**{
            'shop_url' : shop_url,
            'shop_img' : shop_img,
            'shop_name' : shop_name,
            'shop_rate' : shop_rate,
            'shop_available': shop_available,
            'shop_feature' : shop_feature,
            'shop_price' : shop_price,
            'shop_type' : '景点',
            'crawl_time' : crawl_time
        })

        if len(list(shops.find({
            'shop_url': shop_url,
        }))) == 0:
            shops.insert(shop_data)
        else:
            shops.update({
                'shop_url': shop_url,
            },{'$set': shop_data
        })

getShopInfo(driver)
# driver.quit()