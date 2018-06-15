# -*- coding:utf-8 -*-

from selenium import webdriver
import time,random
driver = webdriver.Chrome()
driver.get("http://m.dianping.com/shoplist/3602/search?from=m_search&keyword=义乌")
while(True):
    try:#到达页面底端,结束下拉
        tail = driver.find_element_by_css_selector('#app > div > div.J_footer > footer > p')
        break
    except Exception:#没有找到页面底端的元素,继续下拉
        driver.execute_script('window.scrollBy(0, 50000)')
        time.sleep(0.5)
for each in driver.find_elements_by_css_selector('#app > div > div.J_searchList > ul > li'):
    shop_url = each.find_element_by_css_selector('a').get_attribute('href')
    shop_id = shop_url.split('?')[0].split('/')[-1]
    shop_name = shop
