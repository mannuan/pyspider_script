# -*- coding: utf-8-*-
from selenium import webdriver
import os
from pyquery import PyQuery as pq
import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver')
driver.get("http://wapbaike.baidu.com/item/京杭大运河")

#或得js变量的值
# r = driver.execute_script("return newsJason")
# time.sleep(1)
# print driver.page_source
# driver.quit()

# p = pq(text)
# content = p('BK-content-wrapper').html()
# print content