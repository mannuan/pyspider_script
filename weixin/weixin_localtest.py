# -*- coding:utf-8 -*-

from selenium import webdriver
import time,json

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_xpath('//*[@id="account"]').clear()
driver.find_element_by_xpath('//*[@id="account"]').send_keys('1192328490@qq.com')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="pwd"]').clear()
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('password')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/label').click()#点击
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginBt"]').click()

time.sleep(15)
cookies = driver.get_cookies()

cookie = {}
for items in cookies:
    cookie[items.get('name')] = items.get('value')
with open('cookies.txt','wb') as file:
    file.write(json.dumps(cookie))

driver.close()

