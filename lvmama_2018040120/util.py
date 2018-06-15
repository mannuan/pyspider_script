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
db = conn.lvmama_qiandaohu
shops = db.shops
comments = db.comments

def DropDown(driver):
    driver.execute_script('window.scrollTo(0, 100000)')

def PageTimeout(exestr):
    try:
        exec(exestr)
    except Exception:
        print('页面超时')
def NewWindow(driver,url):
    newwindow = 'window.open("{}");'.format(url)
    driver.execute_script(newwindow)

def getCommentInfo2(driver,shop_id,shop_name,shop_url):
    print('commentinfo2')
    item_count = 0

    for each in driver.find_elements_by_css_selector('#view > div.comment > div.wrap2 > div'):
        item_count += 1
        try:
            comment_user_name = each.find_element_by_css_selector('div.top > div.tourist > div').text
        except Exception:
            continue
        print('comment_user_name:{}'.format(comment_user_name))
        try:
            comment_time = each.find_element_by_css_selector('div.comment-bottom > p').text
        except Exception:
            comment_time = ''
        print('comment_time:{}'.format(comment_time))
        comment_content = ''
        for each1 in each.find_elements_by_css_selector('div.comment-txt.line-clamp3 > div > p'):
            comment_content = each1.text
        print('comment_content:{}'.format(comment_content))
        comment_img = list()
        try:
            review_pics = each.find_element_by_css_selector('div.comment-pic')
            for each1 in review_pics.find_elements_by_css_selector('img'):
                comment_img.append(each1.get_attribute('src'))
        except Exception as e:
            print(e)
            pass
        print('comment_img:{}'.format(comment_img))
        try:
            comment_useful = driver.find_element_by_css_selector('div.comment-bottom > div.usefulCount.ticket').text
            comment_useful = re.sub(r'[^\d]*',r'',comment_useful)
        except Exception:
            comment_useful = 0
        print('comment_useful:{}'.format(comment_useful))
        try:
            comment_reply = driver.find_element_by_css_selector('div.comment-bottom > div.chatReply').text
            comment_reply = re.sub(r'[^\d]*',r'',comment_reply)
        except Exception:
            comment_reply = 0
        print('comment_reply:{}'.format(comment_reply))
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        comment_data = {
            'shop_id' : shop_id,
            'shop_name' : shop_name,
            'comment_url':shop_url,
            'comment_user_name': comment_user_name,
            'comment_time' : comment_time,
            'comment_content': comment_content,
            'comment_img':comment_img,
            'comment_reply':comment_reply,
            'comment_useful':comment_useful,
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
    print('commentinfo')
    page = 0
    while (True):
        page += 1
        print('正在点击查看{}的第{}页评论...'.format(shop_name, page))
        comment_list_len = len(
            driver.find_elements_by_css_selector('#view > div.comment > div.wrap2 > div'))
        DropDown(driver)
        pause_time = (lambda x:1 if x < 1 else x)(random.random()*random.randint(9999,99999)/3333)
        print('...随机暂停{}秒...'.format(pause_time))
        time.sleep(pause_time)
        if comment_list_len == len(
                driver.find_elements_by_css_selector('#view > div.comment > div.wrap2 > div')):
            for i in range(3):
                driver.refresh()
            for i in range(3):
                DropDown(driver)
            time.sleep(5)
            if comment_list_len == len(
                    driver.find_elements_by_css_selector(
                        '#view > div.comment > div.wrap2 > div')):
                print('结束查看{}的评论,共{}页评论...'.format(shop_name, page))
                break
    getCommentInfo2(driver,shop_id,shop_name,shop_url)

def getShopInfo2(driver,shop_id,shop_name,shop_url):
    print('shopinfo2')
    try:
        shop_address = driver.find_element_by_css_selector('#tpl > div.detail-page > div.viewspot-infos.borderRedius > div.addressWrap > p').text
    except Exception:
        shop_address = ''
    print('shop_address:{}'.format(shop_address))
    try:
        shop_comment = driver.find_element_by_css_selector('#tpl > div.detail-page > div.viewspot-infos.borderRedius > div.intro-main > div.right > span').text
        shop_comment = int(re.sub(r'[^\d]*',r'',shop_comment))
    except Exception:
        shop_comment = 0
    print('shop_comment:{}'.format(shop_comment))
    try:
        shop_satisfaction = driver.find_element_by_css_selector('#tpl > div.detail-page > div.viewspot-infos.borderRedius > div.intro-main > div.right > p').text
        shop_satisfaction = re.sub(r'[^\d.%]*', r'', shop_satisfaction)
    except Exception:
        shop_satisfaction = '0%'
    print('shop_satisfaction:{}'.format(shop_satisfaction))
    DropDown(driver)
    try:
        shop_time = driver.find_element_by_css_selector(
            '#tpl > div.detail-page > div.viewspot-details.hasFreeTour > div > section > article.tabChange.order-ticket.comment.pdb0.pdt66 > div.notice.detail-notice.JQXZ > div.detailSpots.detailShow > div:nth-child(1) > p').text.replace('\n','')
    except Exception as e:
        print(e)
        shop_time = ''
    print('shop_time:{}'.format(shop_time))
    try:
        shop_intro = driver.find_element_by_css_selector(
            '#tpl > div.detail-page > div.viewspot-details.hasFreeTour > div > section > article.tabChange.order-ticket.comment.pdb0.pdt66 > div.notice.detail-notice.JQXZ > div.detailSpots.detailShow').text.replace('\n','')
    except Exception as e:
        print(e)
        shop_intro = ''
    print('shop_intro:{}'.format(shop_intro))
    shop_data = {
        'shop_address':shop_address,
        'shop_comment':shop_comment,
        'shop_satisfaction':shop_satisfaction,
        'shop_time': shop_time,
        'shop_intro':shop_intro,
        'shop_statistics' :''
    }
    print('点击查看{}全部评论...'.format(shop_name))
    time.sleep(3)
    try:
        driver.find_element_by_css_selector('#tpl > div.detail-page > div.viewspot-details.hasFreeTour > div > section > article.tabChange.order-ticket.comment.pdb0.pdt66 > div.more-comment.all > span').click()
    except Exception as e:
        print(e)
        return shop_data
    for i in range(3):
        driver.refresh()
    time.sleep(3)
    try:
        shop_statistics = driver.find_element_by_css_selector().text
    except Exception:
        shop_statistics = ''
    print('shop_statistics:{}'.format(shop_statistics))
    shop_data = {
        'shop_address':shop_address,
        'shop_comment':shop_comment,
        'shop_satisfaction':shop_satisfaction,
        'shop_time': shop_time,
        'shop_intro':shop_intro,
        'shop_statistics' :shop_statistics
    }
    getCommentInfo(driver,shop_id,shop_name,shop_url)
    return shop_data

def getShopInfo(driver):
    print('shopinfo')
    item_count = 0
    for each in driver.find_elements_by_css_selector('article.masterplate-list > ul > li')[:18]:
        item_count += 1
        print('正在浏览第{}家店铺...'.format(item_count))
        item = each.find_element_by_css_selector('a')
        try:
            shop_url = item.get_attribute('href')
        except Exception:
            continue
        print('shop_url:{}'.format(shop_url))
        try:
            shop_id = shop_url.split('-')[-1]
        except Exception:
            continue
        print('shop_id:{}'.format(shop_id))
        try:
            shop_img = item.find_element_by_css_selector('div.ml-pro-img > img').get_attribute('src')
        except Exception:
            shop_img = ''
        print('shop_img:{}'.format(shop_img))
        shop_name = item.find_element_by_css_selector('div.ml-pro-info > p').text
        print('shop_name:{}'.format(shop_name))
        try:
            shop_price = float(re.sub(r'[^\d.]*',r'',item.find_element_by_css_selector('div.ml-pro-info > div.ml-pro-price > span.price').text))
        except Exception:
            shop_price = 0
        print('shop_price:{}'.format(shop_price))
        try:
            shop_active = item.find_element_by_css_selector('div.ml-pro-info > div.ml-pro-price').text
        except Exception:
            shop_active = ''
        print('shop_active:{}'.format(shop_active))
        try:
            shop_rate = driver.find_element_by_css_selector(
                'div.ml-pro-info > div.orderNum.adress').text
            shop_rate = re.sub(r'[^\dA]',r'',shop_rate)
        except Exception:
            shop_rate = ''
        print('shop_rate:{}'.format(shop_rate))
        # try:
        #     shop_distance = driver.find_element_by_css_selector(
        #         'div.ml-pro-info > div.orderNum.adress').text
        #     shop_distance = re.sub(r'[^\dkm]',r'',shop_distance)
        # except Exception:
        #     shop_distance = ''
        # print('shop_distance:{}'.format(shop_distance))
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
            'shop_rate':shop_rate,
            # 'shop_distance':shop_distance,
            'shop_price': shop_price,
            'shop_active':shop_active,
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