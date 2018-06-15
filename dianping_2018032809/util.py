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
db = conn.dianping_qiandaohu
shops = db.shops
comments = db.comments

def DropDown(driver):
    driver.execute_script('window.scrollTo(0, 100000)')

def PageTimeout(exestr):
    try:
        exec exestr
    except Exception:
        print '页面超时'
def NewWindow(driver,url):
    newwindow = 'window.open("{}");'.format(url)
    driver.execute_script(newwindow)

def getCommentInfo2(driver,shop_id,shop_name,comment_list_url,page):
    print 'commentinfo2'
    item_count = 0
    #点击展开评论
    for each in driver.find_elements_by_css_selector('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li > div > div.review-truncated-words > div > a'):
        print '正在展开评论...'
        each.click()

    for each in driver.find_elements_by_css_selector('#review-list > div.review-list-container > div.review-list-main > div.reviews-wrapper > div.reviews-items > ul > li'):
        item_count += 1
        # ActionChains(driver).move_to_element(each).perform()
        comment_user_name = each.find_element_by_css_selector('div > div.dper-info > a').text
        print 'comment_user_name:{}'.format(comment_user_name)
        comment_user_url = each.find_element_by_css_selector('div > div.dper-info > a').get_attribute('href')
        print 'comment_user_url:{}'.format(comment_user_url)
        try:
            comment_user_pic = each.find_element_by_css_selector('a > img').get_attribute('src')
        except Exception:
            comment_user_pic = ''
        print 'comment_user_pic:{}'.format(comment_user_pic)
        try:
            comment_time = each.find_element_by_css_selector('div > div.misc-info.clearfix > span.time').text
        except NoSuchElementException:
            comment_time = ''
        print 'comment_time:{}'.format(comment_time)
        try:
            comment_star = each.find_element_by_css_selector('div > div.review-rank > span').get_attribute('class')
            comment_star = float(re.sub(r'[^\d]*',r'',comment_star))/10
        except Exception:
            comment_star = 0
        print 'comment_star:{}'.format(comment_star)
        comment_content = each.find_element_by_css_selector('div > div.review-words').text
        comment_content = re.sub(r'[\n]*',r'',comment_content).replace('收起评论','')
        print 'comment_content:{}'.format(comment_content)
        comment_img = list()
        try:
            review_pic = each.find_element_by_css_selector('div > div.review-pictures')
            for each1 in review_pic.find_elements_by_css_selector('ul > li'):
                comment_img.append(each1.find_element_by_css_selector('a > img').get_attribute('data-lazyload'))
        except Exception:
            pass
        print 'comment_img:{}'.format(comment_img)
        comment_like_replay = each.find_element_by_css_selector('div > div.misc-info.clearfix > span.actions').text
        try:
            comment_like = int(re.sub(r'[^\d]*',r'',comment_like_replay.split('回应')[0]))
        except Exception:
            comment_like = 0
        print 'comment_like:{}'.format(comment_like)
        try:
            comment_replay = int(re.sub(r'[^\d]*',r'',comment_like_replay.split('回应')[1]))
        except Exception:
            comment_replay = 0
        print 'comment_replay:{}'.format(comment_replay)
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        comment_data = {
            'shop_id' : shop_id,
            'shop_name' : shop_name,
            'comment_list_url':comment_list_url,
            'comment_user_name': comment_user_name,
            'comment_user_url': comment_user_url,
            'comment_user_pic': comment_user_pic,
            'comment_time' : comment_time,
            'comment_star':comment_star,
            'comment_content': comment_content,
            'comment_img':comment_img,
            'comment_like':comment_like,
            'comment_replay':comment_replay,
            'data_source':'景点',
            'page':page,
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

def getCommentInfo(driver,shop_id,shop_name,comment_url):
    print 'commentinfo'
    page = 1
    while(True):#加载全部评论
        print '*************************正在浏览 {} 评论页面的第 {} 页*************************'.format(shop_name, page)
        getCommentInfo2(driver, shop_id, shop_name,comment_url,page)
        try:
            driver.find_element_by_partial_link_text(u'下一页').click()
            print '*************************即将浏览 {} 评论页面的第 {} 页*************************'.format(shop_name, page + 1)
            # 产生随机暂停时间
            pause_time = (lambda x:10 if x < 10 else x)(random.random()*random.randint(9999,99999)/222)
            print '...随机暂停:{}s...'.format(pause_time)
            time.sleep(pause_time)
            page += 1
        except NoSuchElementException:
            pause_time = (lambda x:10 if x < 10 else x)(random.random()*random.randint(9999,99999)/222)
            print '...随机暂停:{}s...'.format(pause_time)
            time.sleep(pause_time)
            break
    try:
        shop_statistics = driver.find_element_by_css_selector('#summaryfilter-wrapper > div.comment-condition.J-comment-condition.Fix > div.content').text
    except NoSuchElementException:
        shop_statistics = ''
    print '################################结束浏览 {} 评论页面的共 {} 页############################'.format(shop_name,page)
    return shop_statistics

def getShopInfo2(driver,shop_id,shop_name):
    print 'shopinfo2'
    try:
        shop_address = driver.find_element_by_css_selector('body > div.J_address').text
    except Exception:
        shop_address = ''
    print 'shop_address:{}'.format(shop_address)
    try:
        shop_phone = driver.find_element_by_css_selector('body > div.J_phone').text
    except Exception:
        shop_phone = ''
    print 'shop_phone:{}'.format(shop_phone)
    try:
        shop_time = driver.find_element_by_css_selector('body > div.J_otherinfo > div > div > div.businessTime').text
    except Exception:
        shop_time = ''
    print 'shop_time:{}'.format(shop_time)
    shop_data = {
        'shop_address':shop_address,
        'shop_phone':shop_phone,
        'shop_time':shop_time,
        'shop_statistics':''
    }
    try:
        comment_url = driver.find_element_by_css_selector('body > div.J_review > div.modebox.shop-comment > a').get_attribute('href')
        comment_url = comment_url.replace('m.dianping.com','www.dianping.com')
    except Exception:
        return shop_data
    print 'comment_url:{}'.format(comment_url)
    NewWindow(driver,comment_url)
    driver.switch_to_window(driver.window_handles[2])
    time.sleep(1)
    shop_statistics = getCommentInfo(driver,shop_id,shop_name,comment_url)
    driver.close()
    driver.switch_to_window(driver.window_handles[1])
    shop_data = {
        'shop_address':shop_address,
        'shop_phone':shop_phone,
        'shop_time':shop_time,
        'shop_statistics':shop_statistics
    }
    return shop_data

def getShopInfo(driver):
    print 'shopinfo'
    item_count = 0
    for each in driver.find_elements_by_css_selector('#app > div > div.J_searchList > ul > li'):
        item_count += 1
        item = each.find_element_by_css_selector('a')
        try:
            shop_url = item.get_attribute('href').split('?')[0]
        except Exception:
            continue
        print 'shop_url:{}'.format(shop_url)
        try:
            shop_id = shop_url.split('/')[-1]
        except Exception:
            continue
        print 'shop_id:{}'.format(shop_id)
        try:
            shop_img = item.find_element_by_css_selector('div.item-pic').get_attribute('style').split('\"')[1]
        except Exception:
            shop_img = ''
        print 'shop_img:{}'.format(shop_img)
        shop_name = item.find_element_by_css_selector('div.item-content > div.item-title > h3').text
        print 'shop_name:{}'.format(shop_name)
        shop_price = 0
        shop_comment = 0
        try:
            div_item_count = each.find_element_by_css_selector('div.item-content > div.item-comment')
            for each1 in div_item_count.find_elements_by_css_selector(
                    'span.item-comment-price'):
                if '￥' in each1.text:
                    shop_price = float(re.sub(r'[^\d.]*', r'', item.find_element_by_css_selector(
                        'div.item-content > div.item-comment > span:nth-child(3)').text))
                elif '条' in each1.text:
                    shop_comment = int(re.sub(r'[^\d]*', r'', item.find_element_by_css_selector(
                        'div.item-content > div.item-comment > span:nth-child(2)').text))
        except Exception:
            pass
        print 'shop_price:{}'.format(shop_price)
        print 'shop_comment:{}'.format(shop_comment)
        shop_grade = float(item.find_element_by_css_selector('div.item-content > div.item-comment > span').get_attribute('class').split('-')[-1])/10
        print 'shop_grade:{}'.format(shop_grade)
        try:
            shop_feature = item.find_element_by_css_selector('div.item-content > div.item-info > div.item-info-left').text.replace('\n','')
        except Exception:
            shop_feature = ''
        print 'shop_feature:{}'.format(shop_feature)
        try:
            shop_distance = re.sub(r'[^\d.km]*',r'',item.find_element_by_css_selector('div.item-content > div.item-info > div.item-info-right > span > span').text)
        except Exception:
            shop_distance = ''
        print 'shop_distance:{}'.format(shop_distance)
        if '暂停营业' in item.text:
            print '暂停营业'
            return
        NewWindow(driver,shop_url)
        driver.switch_to_window(driver.window_handles[1])
        shop_data = getShopInfo2(driver,shop_id,shop_name)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        shop_data = dict(shop_data,**{
            'shop_url' : shop_url,
            'shop_id':shop_id,
            'shop_img' : shop_img,
            'shop_name' : shop_name,
            'shop_price': shop_price,
            'shop_grade' : shop_grade,
            'shop_comment' : shop_comment,
            'shop_feature': shop_feature,
            'shop_distance':shop_distance,
            'data_source' : '景点',
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