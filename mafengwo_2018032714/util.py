#-*- coding:utf-8 -*-
import time,random,re,sys,json
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
reload(sys)
sys.setdefaultencoding('utf8')
from driver import *

conn = MongoClient('localhost', 27017)
db = conn.mafengwo_qiandaohu
shops = db.shops
comments = db.comments

def DropDown(driver):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

def PageTimeout(exestr):
    try:
        exec exestr
    except Exception:
        print '页面超时'

def getCommentInfo(shop_url):
    driver = getPhantomJsMobileDriver()
    shop_url = 'https://m.mafengwo.cn/poi/comment_{}'.format(shop_url.split('/')[-1])
    driver.get(shop_url)
    time.sleep(1)
    shop_grade = float(driver.find_element_by_css_selector('body > div.comment > div.bd > div.score > p:nth-child(1) > strong').text)
    while(True):
        comment_len = len(driver.find_elements_by_css_selector('body > div.comment > div.list > ul > li'))
        DropDown(driver)
        time.sleep(0.5)
        if len(driver.find_elements_by_css_selector('body > div.comment > div.list > ul > li')) == comment_len:
            break
    for each in driver.find_elements_by_css_selector('body > div.comment > div.list > ul > li'):
        comment_user_url = each.find_element_by_css_selector('dl > dt > a').get_attribute('href')
        comment_user_img = each.find_element_by_css_selector('dl > dt > a > img').get_attribute('src')
        comment_user_name = each.find_element_by_css_selector('dl > dd > p').text.split('Lv')[0]
        comment_user_grade = each.find_element_by_css_selector('dl > dd > p > span').text
        comment_time = each.find_element_by_css_selector('dl > dd > div.time').text
        comment_content = each.find_element_by_css_selector('div.context').text
        content_img_url = list()
        for each1 in each.find_elements_by_css_selector('div.photos.clearfix > a'):
            content_img_url.append(each1.get_attribute('href'))
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        print comment_user_name,comment_time,comment_content
        comment_data = {
            'shop_url' : shop_url,
            'comment_user_url': comment_user_url,
            'comment_user_img': comment_user_img,
            'comment_user_name': comment_user_name,
            'comment_user_grade' : comment_user_grade,
            'comment_time' : comment_time,
            'comment_content': comment_content,
            'content_img_url' : content_img_url,
            'crawl_time' : crawl_time
        }

        if len(list(comments.find({
            'shop_url' : shop_url,
            'comment_user_url': comment_user_url,
            'comment_content': comment_content
        }))) == 0:
            comments.insert(comment_data)
        else:
            comments.update({
                'shop_url' : shop_url,
                'comment_user_url': comment_user_url,
                'comment_content': comment_content
            },{'$set': {
                'comment_user_img': comment_user_img,
                'comment_user_name': comment_user_name,
                'comment_user_grade': comment_user_grade,
                'comment_time': comment_time,
                'crawl_time': crawl_time
            }
        })
    driver.quit()
    return shop_grade

def getShopInfo2(driver,shop_url):
    for each in driver.find_elements_by_link_text(u'展开全部'):
        each.click()
    shop_time=''
    shop_price=''
    shop_traffic = ''
    for each in driver.find_elements_by_css_selector('body > div.container > div:nth-child(6) > div.mod.mod-detail > dl'):
        if '开放时间' in each.text:
            shop_time = each.text.replace('展开全部>','')
        elif '门票' in each.text:
            shop_price = each.text.replace('展开全部>','')
        elif '交通' in each.text:
            shop_traffic = each.text.replace('展开全部>','')
    try:
        shop_summary = driver.find_element_by_css_selector('body > div.container > div:nth-child(6) > div.mod.mod-detail > div').text.replace('展开全部>','')
    except Exception:
        shop_summary = ''
    try:
        shop_phone = driver.find_element_by_css_selector('body > div.container > div:nth-child(6) > div.mod.mod-detail > ul > li.tel > div.content').text.replace('展开全部>','')
    except Exception:
        shop_phone = ''
    try:
        shop_time_refer = driver.find_element_by_css_selector('body > div.container > div:nth-child(6) > div.mod.mod-detail > ul > li.item-time').text.replace('展开全部>','')
    except Exception:
        shop_time_refer = ''
    print shop_time_refer
    shop_address = driver.find_element_by_css_selector('body > div.container > div:nth-child(6) > div.mod.mod-location > div.mhd > p').text.replace('展开全部>','')
    shop_grade = getCommentInfo(shop_url)
    shop_data = {'shop_time':shop_time,
                 'shop_price':shop_price,
                 'shop_traffic':shop_traffic,
                 'shop_summary':shop_summary,
                 'shop_phone':shop_phone,
                 'shop_time_refer':shop_time_refer,
                 'shop_address':shop_address,
                 'shop_grade':shop_grade}
    return shop_data

def getShopInfo(driver):
    for each in driver.find_elements_by_css_selector('#_j_search_result_left > div > div > ul > li'):
        shop_url = each.find_element_by_css_selector('div > div.ct-text > h3 > a').get_attribute('href')
        shop_img = each.find_element_by_css_selector('div > div.flt1 > a > img').get_attribute('src')
        shop_name = each.find_element_by_css_selector('div > div.ct-text > h3 > a').text
        shop_comment = int(re.sub(r'[^\d]*',r'',each.find_element_by_css_selector('div > div.ct-text > ul > li:nth-child(2) > a').text))
        shop_diary = int(re.sub(r'[^\d]*',r'',driver.find_element_by_css_selector('div > div.ct-text > ul > li:nth-child(3) > a').text))
        if '景点' not in shop_name:
            continue
        shop_name = shop_name.split('-')[-1].strip()
        print shop_name
        each.find_element_by_css_selector('div > div.ct-text > h3 > a').click()
        driver.switch_to_window(driver.window_handles[1])#切换到评论窗口
        shop_data = getShopInfo2(driver,shop_url)#获取评论数据
        driver.close()#关闭评论窗口
        driver.switch_to_window(driver.window_handles[0])#切换为店铺列表页面
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        shop_data = dict(shop_data,**{
            'shop_url' : shop_url,
            'shop_img' : shop_img,
            'shop_name' : shop_name,
            'shop_comment' : shop_comment,
            'shop_diary' : shop_diary,
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