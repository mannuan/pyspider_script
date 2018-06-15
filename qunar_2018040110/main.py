# -*- coding:utf-8 -*-

import time,random,re,sys,json
from util import *
from driver import *
import requests,json,sys
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.command import Command

driver = getChromeMobileDriver()
print '进入去哪儿移动版主页...'
driver.get('https://www.baidu.com/')
time.sleep(1)
driver.find_element_by_css_selector('#index-kw').send_keys(u'去哪儿')
driver.find_element_by_css_selector('#index-kw').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_elements_by_partial_link_text(u'去哪儿网')[0].click()
# time.sleep(5)
# driver.find_element_by_css_selector('#js_nva_cgy > li.c_piao.js-searchnav > a').click()
# time.sleep(1)
# driver.find_element_by_css_selector('body > div.J_search_container.search_container > form > div.head_cnt > div > input.J_search_input').send_keys(u'千岛湖')
# print '输入千岛湖...'
# driver.find_element_by_css_selector('body > div.J_search_container.search_container > form > div.head_cnt > div > input.J_search_input').send_keys(Keys.ENTER)
# print '搜索千岛湖...'
# driver.find_element_by_css_selector('#app > div > div.J_searchList > nav > div > a:nth-child(2)').click()
# scrollbar = driver.find_element_by_css_selector('#app > div > div.J_searchList > nav > section:nth-child(3) > div.menu.main > div.iScrollVerticalScrollbar.iScrollLoneScrollbar > div')
# around = driver.find_element_by_css_selector('#app > div > div.J_searchList > nav > section:nth-child(3) > div.menu.main > div:nth-child(1) > div:nth-child(9)')
# ActionChains(driver).click_and_hold(scrollbar).move_by_offset(0,-100).click(scrollbar).perform()
# driver.find_element_by_css_selector('#app > div > div.J_searchList > nav > section:nth-child(3) > div.menu.main > div:nth-child(1) > div:nth-child(9)').click()
# print '选择周边游...'
# driver.find_element_by_link_text(u'景点').click()
# print '选择景点...'
#
# while(True):
#     try:
#         driver.find_element_by_css_selector('#app > div > div.J_footer')
#         break
#     except NoSuchElementException as e:
#         print e
#         print '正在下拉店铺页面...'
#         DropDown(driver)
#
# getShopInfo(driver)
# driver.quit()