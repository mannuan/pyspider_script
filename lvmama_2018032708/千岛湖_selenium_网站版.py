# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time,random,re,sys,json
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo import MongoClient
from util import *

conn = MongoClient('localhost', 27017)
db = conn.lvmama_qiandaohu  # 连接lvmama_qiandaohu数据库，没有则自动创建
shops = db.shops  # 使用shops集合,没有则自动创建
comments = db.comments  # 使用comments集合,没有则自动创建

service_args=[]
service_args.append('--load-images=no')
service_args.append('--disk-cache=yes')
service_args.append('--ignore-ssl-errors=true')
driver = webdriver.Chrome(service_args=service_args)
driver.set_page_load_timeout(10)
driver.set_script_timeout(10)#这两种设置都进行才有效
driver.implicitly_wait(10)#隐性等待
try:
    driver.get("https://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(u"lvmama_2018032708")
    time.sleep(1)
    driver.find_element_by_id("su").click()
    time.sleep(1)
    driver.find_elements_by_partial_link_text(u"lvmama_2018032708")[0].click()
except TimeoutException:
    print '超时了'
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.find_elements_by_partial_link_text(u"景点门票").click()

# driver.find_element_by_id("nav_ticket").click()
# driver.find_element_by_id("mainInput").clear()
# driver.find_element_by_id("mainInput").send_keys(u"千岛湖")#搜索目的地
# driver.find_element_by_css_selector('#base_bd > div:nth-child(1) > div > div.main_right > div.search_wrap.basefix > a').click()#点击搜索
# try:
#     driver.find_element_by_css_selector('#chosenFilterContainer > ul:nth-child(3) > li > span.area_box > a:nth-child(1)').click()
# except Exception:
#     pass


# while(True):
#     getShopInfo(driver)
#     try:#检查有没有结束页的标志
#         driver.find_element_by_css_selector('#searchResultContainer > div.pkg_page.basefix > a.down.down_nocurrent')
#         break
#     except Exception:#没有下一页,继续点击
#         driver.find_element_by_css_selector('#searchResultContainer > div.pkg_page.basefix > a.down').click()
# driver.quit()