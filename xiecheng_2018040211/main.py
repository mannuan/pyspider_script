# -*- coding:utf-8 -*-

from driver import *
from util import *

def main():
    driver = getChromeWebDriver()
    driver.get("https://www.baidu.com")
    time.sleep(1)
    driver.find_element_by_id("kw").send_keys(u"携程")
    time.sleep(1)
    driver.find_element_by_id("su").click()
    time.sleep(1)
    driver.find_elements_by_partial_link_text(u"携程")[0].click()
    driver.close()
    driver.switch_to_window(driver.window_handles[0])
    driver.find_element_by_id("nav_ticket").click()
    driver.find_element_by_id("mainInput").clear()
    driver.find_element_by_id("mainInput").send_keys(u"千岛湖")#搜索目的地
    driver.find_element_by_css_selector('#base_bd > div:nth-child(1) > div > div.main_right > div.search_wrap.basefix > a').click()#点击搜索
    try:
        driver.find_element_by_css_selector('#chosenFilterContainer > ul:nth-child(3) > li > span.area_box > a:nth-child(1)').click()
    except Exception:
        pass

    while(True):
        getShopInfo(driver)
        try:#检查有没有结束页的标志
            driver.find_element_by_css_selector('#searchResultContainer > div.pkg_page.basefix > a.down.down_nocurrent')
            break
        except Exception:#没有下一页,继续点击
            driver.find_element_by_css_selector('#searchResultContainer > div.pkg_page.basefix > a.down').click()
    driver.quit()

if __name__ == '__main__':
    main()