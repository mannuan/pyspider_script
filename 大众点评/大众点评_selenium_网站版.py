# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,random,re,sys,json
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo import MongoClient
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/47.0.2526.107 Mobile/13C75 Safari/601.1.46")

conn = MongoClient('localhost', 27017)
db = conn.xiecheng_qiandaohu  # 连接xiecheng_qiandaohu数据库，没有则自动创建
shops = db.shops  # 使用shops集合,没有则自动创建
comments = db.comments  # 使用comments集合,没有则自动创建
driver = webdriver.Chrome(desired_capabilities=dcap)
driver.set_page_load_timeout(10)
driver.implicitly_wait(10)#隐性等待
driver.set_script_timeout(10)
driver.get("https://m.baidu.com")

driver.find_element_by_id("index-kw").clear()
driver.find_element_by_id("index-kw").send_keys(u"大众点评")
driver.find_element_by_id("index-bn").click()
driver.find_elements_by_partial_link_text(u'大众点评')[0].click()
driver.find_element_by_css_selector("div.search.J_search_trigger").click()
driver.find_element_by_name("keyword").clear()
driver.find_element_by_name("keyword").send_keys(u"千岛湖")
driver.find_element_by_name("keyword").send_keys(Keys.ENTER)
driver.find_element_by_link_text(u'全部分类').click()

# driver.find_element_by_css_selector('#app > div > div.J_searchList > nav > section:nth-child(3) > div.menu.main > div:nth-child(1) > div:nth-child(8)').click()
# driver.find_element_by_link_text(u'景点').click()
# driver.find_element_by_css_selector()
# driver.find_elements_by_partial_link_text(u"大众点评")[0].click()
# driver.close()
# driver.switch_to_window(driver.window_handles[0])
# driver.find_element_by_id("J-search-input").clear()
# driver.find_element_by_id("J-search-input").send_keys(u"千岛湖")
# time.sleep(10)
# driver.find_element_by_css_selector('#J-all-btn').click()
# driver.close()
# driver.switch_to_window(driver.window_handles[0])
# time.sleep(10)
# driver.refresh()
# driver.find_element_by_link_text(u'周边游').click()
# driver.find_element_by_link_text(u'景点').click()
# try:
#     driver.find_element_by_css_selector('#chosenFilterContainer > ul:nth-child(3) > li > span.area_box > a:nth-child(1)').click()
# except Exception:
#     pass

def getCommentInfo(driver,shop_url):
    for each in driver.find_elements_by_css_selector('#J-comments > ul > li'):
        comment_grade = each.find_element_by_css_selector('h4 > span').text.strip()
        comment_user = re.sub(r'[\d]{4}-[\d]{2}-[\d]{2}[ ]+[\d]{2}:[\d]{2}',r'',each.find_element_by_css_selector('div').text).strip()
        comment_time = re.sub(r'.+([\d]{4}-[\d]{2}-[\d]{2}[ ]+[\d]{2}:[\d]{2})',r'\1',each.find_element_by_css_selector('div').text).strip().strip()
        print comment_user,comment_time
        comment_content = ''
        for p in each.find_elements_by_css_selector('p'):
            comment_content += p.text
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        comment_data = {
            'shop_url' : shop_url,
            'comment_user': comment_user,
            'comment_content': comment_content,
            'comment_grade' : comment_grade,
            'comment_time' : comment_time,
            'crawl_time' : crawl_time
        }

        if len(list(comments.find({
            'shop_url' : shop_url,
            'comment_user': comment_user,
            'comment_content': comment_content
        }))) == 0:
            comments.insert(comment_data)
        else:
            comments.update({
                'shop_url' : shop_url,
                'comment_user': comment_user,
                'comment_content': comment_content
            },{'$set': {
                'comment_grade' : comment_grade,
                'comment_time' : comment_time,
                'crawl_time' : crawl_time
            }
        })

def getShopInfo2(driver,shop_url):
    shop_time = driver.find_element_by_css_selector('#media-wrapper > div.media-right > ul > li.time > span').text
    shop_price = float(driver.find_element_by_css_selector('#media-wrapper > div.media-price > div > span').text)
    shop_active = driver.find_element_by_css_selector('#media-wrapper > div.media-price').text.split('起')[-1]
    shop_data = {'shop_time':shop_time,'shop_price':shop_price,'shop_active':shop_active}
    try:
        driver.find_element_by_link_text(u"用户点评").click()
    except Exception:
        return shop_data
    while(True):
        getCommentInfo(driver,shop_url)
        try:
            driver.find_element_by_css_selector('#J-Pages > a.c_down').click()
            time.sleep(1)
        except Exception:
            break
    return shop_data

def getShopInfo(driver):
    for each in driver.find_elements_by_css_selector('#searchResultContainer > div > div'):
        shop_url = each.find_element_by_css_selector('a').get_attribute('href')
        shop_img = each.find_element_by_css_selector('a > img').get_attribute('src')
        shop_name = each.find_element_by_css_selector('div.search_ticket_title > h2 > a').text
        shop_rate = each.find_element_by_css_selector('div.search_ticket_title > h2 > span > span.rate').text
        shop_address = each.find_element_by_css_selector('div.search_ticket_title > div.adress').text
        shop_feature = each.find_element_by_css_selector('div.search_ticket_title > div.exercise').text
        try:#判断该景区是否处于开放状态
            each.find_element_by_css_selector('div.search_ticket_assess > span.grades')
        except:
            continue
        print shop_name
        shop_grade = float(each.find_element_by_css_selector('div.search_ticket_assess > span.grades > em').text)
        shop_comment = int(each.find_element_by_css_selector('div.search_ticket_assess > span.grades').text.split('分(')[-1].replace('人点评)',''))
        each.find_element_by_css_selector('div.search_ticket_assess > span.comment > a').click()
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
            'shop_address' : shop_address,
            'shop_feature' : shop_feature,
            'shop_grade' : shop_grade,
            'shop_comment' : shop_comment,
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

# while(True):
#     getShopInfo(driver)
#     try:#检查有没有结束页的标志
#         driver.find_element_by_css_selector('#searchResultContainer > div.pkg_page.basefix > a.down.down_nocurrent')
#         break
#     except Exception:#没有下一页,继续点击
#         driver.find_element_by_css_selector('#searchResultContainer > div.pkg_page.basefix > a.down').click()
# driver.quit()