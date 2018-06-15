#-*- coding:utf-8 -*-
import time,random,re,sys,json
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
reload(sys)
sys.setdefaultencoding('utf8')
from driver import *

conn = MongoClient('localhost', 27017)
db = conn.fliggy_qiandaohu
shops = db.shops
comments = db.comments

def DropDown(driver):
    driver.execute_script('window.scrollTo(0, 20000)')

def PageTimeout(exestr):
    try:
        exec exestr
    except Exception:
        print '页面超时'
def NewWindow(driver,url):
    newwindow = 'window.open("{}");'.format(url)
    driver.execute_script(newwindow)

def getCommentInfo2(driver,shop_id,shop_name,shop_url):
    print 'commentinfo2'
    item_count = 0

    for each in driver.find_elements_by_css_selector('#J_detail > div > section.rate-detail.section-cell > ul > li'):
        item_count += 1
        try:
            comment_user_name = each.find_element_by_css_selector('div > div.side > div.user-name').text
        except Exception:
            continue
        print 'comment_user_name:{}'.format(comment_user_name)
        try:
            comment_user_pic = each.find_element_by_css_selector('div > img').get_attribute('src')
        except Exception:
            comment_user_pic = ''
        print 'comment_user_pic:{}'.format(comment_user_pic)
        try:
            comment_time = each.find_element_by_css_selector('div > div.time').text
        except Exception:
            comment_time = ''
        print 'comment_time:{}'.format(comment_time)
        comment_content = ''
        for each1 in each.find_elements_by_css_selector('p'):
            comment_content = each1.text
        print 'comment_content:{}'.format(comment_content)
        comment_img = list()
        try:
            review_pics = each.find_elements_by_css_selector('ul > li > div')
            for each1 in review_pics:
                comment_img.append(each1.get_attribute('style'))
        except Exception as e:
            print e
            pass
        print 'comment_img:{}'.format(comment_img)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        comment_data = {
            'shop_id' : shop_id,
            'shop_name' : shop_name,
            'comment_url':shop_url,
            'comment_user_name': comment_user_name,
            'comment_user_pic': comment_user_pic,
            'comment_time' : comment_time,
            'comment_content': comment_content,
            'comment_img':comment_img,
            'item_count':item_count,
            'crawl_time' : crawl_time
        }

        if len(list(comments.find({
            'shop_id' : shop_id,
            'comment_user_name':comment_user_name,
            'comment_time': comment_time,
        }))) == 0:
            comments.insert(comment_data)
        else:
            comments.update({
                'shop_id': shop_id,
                'comment_user_name': comment_user_name,
                'comment_time': comment_time,
            },{'$set': comment_data})

def getCommentInfo(driver,shop_id,shop_name,shop_url):
    print 'commentinfo'
    page = 0
    while (True):
        page += 1
        print '正在点击查看{}的第{}页评论...'.format(shop_name, page)
        try:
            item_more = driver.find_element_by_css_selector(
            '#J_detail > div > section.rate-detail.section-cell > div.item-more')
        except Exception:
            break
        comment_list_len = len(
            driver.find_elements_by_css_selector('#J_detail > div > section.rate-detail.section-cell > ul > li'))
        item_more.click()
        pause_time = (lambda x:1 if x < 1 else x)(random.random()*random.randint(9999,99999)/8888)
        print '...随机暂停{}秒...'.format(pause_time)
        time.sleep(pause_time)
        if comment_list_len == len(
                driver.find_elements_by_css_selector('#J_detail > div > section.rate-detail.section-cell > ul > li')):
            time.sleep(3)
            if comment_list_len == len(
                    driver.find_elements_by_css_selector(
                        '#J_detail > div > section.rate-detail.section-cell > ul > li')):
                print '结束查看{}的评论,共{}页评论...'.format(shop_name, page)
                break
    getCommentInfo2(driver,shop_id,shop_name,shop_url)

def getShopInfo2(driver,shop_id,shop_name,shop_url):
    print 'shopinfo2'
    try:
        shop_address = driver.find_element_by_css_selector('#J_detail > div > section.new-base-info.section-cell > div.scenic-address > p').text
    except Exception:
        shop_address = ''
    print 'shop_address:{}'.format(shop_address)
    try:
        shop_comment = driver.find_element_by_css_selector('#J_detail > div > section.rate-detail.section-cell > div.rate-title').text
        shop_comment = int(re.sub(r'[^\d]*',r'',shop_comment))
    except Exception:
        shop_comment = 0
    print 'shop_comment:{}'.format(shop_comment)
    #点击店铺详细信息
    try:
        driver.find_element_by_css_selector('#J_detail > div > section.new-base-info.section-cell > div.scenic-info').click()
    except Exception:
        pass
    try:
        shop_time = driver.find_element_by_css_selector('#page-scenic-intro > div > div:nth-child(1) > p:nth-child(2)').text
    except Exception:
        shop_time = ''
    print 'shop_time:{}'.format(shop_time)
    try:
        shop_intro = driver.find_element_by_css_selector('#page-scenic-intro > div > div:nth-child(2) > p').text
    except Exception:
        shop_intro = ''
    print 'shop_intro:{}'.format(shop_intro)
    driver.back()
    shop_data = {
        'shop_address':shop_address,
        'shop_comment':shop_comment,
        'shop_time': shop_time,
        'shop_intro':shop_intro,
    }
    getCommentInfo(driver,shop_id,shop_name,shop_url)
    return shop_data

def getShopInfo(driver):
    print 'shopinfo'
    item_count = 0
    for each in driver.find_elements_by_css_selector('#app > div > div.search-result-ctn > div > div > div > div:nth-child(7) > div:nth-child(1) > ul > div'):
        item_count += 1
        item = each.find_element_by_css_selector('a')
        try:
            shop_url = item.get_attribute('href')
        except Exception:
            continue
        print 'shop_url:{}'.format(shop_url)
        try:
            shop_id = shop_url.split('=')[-1]
        except Exception:
            continue
        print 'shop_id:{}'.format(shop_id)
        try:
            shop_img = item.find_element_by_css_selector('div.item-image-container > img').get_attribute('src')
        except Exception:
            shop_img = ''
        print 'shop_img:{}'.format(shop_img)
        shop_name = item.find_element_by_css_selector('div.item-info > div.item-text-container > div.item-text.item-title.line-count-1 > span').text
        print 'shop_name:{}'.format(shop_name)
        try:
            shop_price = float(re.sub(r'[^\d.]*',r'',item.find_element_by_css_selector('div.item-info > div.price-container > div.rpi-price.price > span:nth-child(2)').text))
        except Exception:
            shop_price = 0
        print 'shop_price:{}'.format(shop_price)
        try:
            shop_rate_active = item.find_element_by_css_selector('div.item-info > div.item-text-container > div.item-sub-text.item-desc3.line-count-1').text
            shop_rate = re.sub(r'[^A]*',r'',shop_rate_active)
            shop_active = re.sub(r'[(A)]*',r'',shop_rate_active)
        except Exception:
            shop_rate = ''
            shop_active = ''
        try:
            shop_feature = item.find_element_by_css_selector('div.item-info > div.item-text-container > div.item-sub-text.item-desc.line-count-1 > span').text.replace('\n','')
        except NoSuchElementException:
            shop_feature = ''
        print 'shop_feature:{}'.format(shop_feature)
        try:
            shop_volume = item.find_element_by_css_selector('div.item-info > div.price-container > div.price-desc').text
        except Exception:
            shop_volume = ''
        NewWindow(driver,shop_url)
        driver.switch_to_window(driver.window_handles[1])
        shop_data = getShopInfo2(driver,shop_id,shop_name,shop_url)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        shop_data = dict(shop_data,**{
            'shop_url' : shop_url,
            'shop_id':shop_id,
            'shop_img' : shop_img,
            'shop_name' : shop_name,
            'shop_price': shop_price,
            'shop_rate' : shop_rate,
            'shop_active':shop_active,
            'shop_feature': shop_feature,
            'shop_volume':shop_volume,
            'shop_type' : '景点',
            'crawl_time' : crawl_time,
            'item_count':item_count
        })

        if len(list(shops.find({
            'shop_id': shop_id,
        }))) == 0:
            shops.insert(shop_data)
        else:
            shops.update({
                'shop_id': shop_id,
            },{'$set': shop_data
        })