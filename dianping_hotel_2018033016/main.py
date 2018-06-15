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

driver = getChromeHeaderlessWebDriver()
print '进入大众点评移动版主页...'
driver.get('https://m.dianping.com/')
time.sleep(1)
driver.find_element_by_css_selector('body > div.J_header > header > div.search.J_search_trigger').click()
time.sleep(1)
driver.find_element_by_css_selector('body > div.J_search_container.search_container > form > div.head_cnt > div > input.J_search_input').send_keys(u'千岛湖')
print '输入千岛湖...'
driver.find_element_by_css_selector('body > div.J_search_container.search_container > form > div.head_cnt > div > input.J_search_input').send_keys(Keys.ENTER)
print '搜索千岛湖...'
driver.find_element_by_css_selector('#app > div > div.J_searchList > nav > div > a:nth-child(2)').click()
driver.find_element_by_css_selector('#app > div > div.J_searchList > nav > section:nth-child(3) > div.menu.main > div:nth-child(1) > div:nth-child(5)').click()
print '选择酒店...'
driver.find_element_by_link_text(u'全部酒店').click()
print '选择全部酒店...'
time.sleep(1)
while(True):
    try:
        driver.find_element_by_css_selector('#app > div > div.J_footer')
        break
    except NoSuchElementException as e:
        print e
        print '正在下拉店铺页面...'
        DropDown(driver)

getShopInfo(driver)
driver.quit()