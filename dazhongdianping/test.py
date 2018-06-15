# -*- coding:utf-8 -*-

# 第三方模块 requests bs4 xlwt json
#
# 自带的模块urllib python2 pycharm

import requests
from bs4 import BeautifulSoup

start_url = "http://www.dianping.com/search/category/344/10/"

def get_content(url,headers=None):
    response = requests.get(url,headers=headers)#发起了一次请求
    return response.content

def region_url(html):
    soup = BeautifulSoup(html,'lxml')
    url_list = [i['href'] for i in soup.find('div',id='region-nav').find_all('a')]
    # url = soup.find('div',id='region-nav').find_all('a')
    return url_list

def get_shop_url(html):
    '''
    获取商户的详情页url地址
    :param html:
    :return:
    '''
    soup = BeautifulSoup(html, 'lxml')
    shop_list_url = soup.find_all('div',class_='tit')
    return [i.find('a')['href'] for i in shop_list_url]

def get_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find('div',class_='breadcrumb').find('span').text
    price = soup.find('span',id='avgPriceTitle').text #价格
    evaluation = soup.find('span',id='comment_score').find_all('span',class_='item')#评分的list
    comments = soup.find('span',id='reviewCount').text #评分的数量
    address = soup.find('span',itemprop='street-address').text
    print('店名:'+title)
    for ev in evaluation:
        print(ev.text)
    print('评论数量:'+comments)
    print('地址:'+address.strip())
    print('人均价格:'+price)
    return (title,evaluation[0],evaluation[1],evaluation[2],comments,address,price)

if __name__ == '__main__':
    headers = {
        'Host': 'www.dianping.com',
        'Connection': 'keep-alive',
        # Cache-Control: max-age=0
        # Upgrade-Insecure-Requests: 1
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept': 'application/json, text/javascript',
        'Referer': 'http://www.dianping.com/search/category/344/10/r6023',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'showNav=#nav-tab|0|0; navCtgScroll=0; _lxsdk_cuid=15fe3fc3ed0c8-026fd89dad80db-1f2a1709-1aeaa0-15fe3fc3ed0c8; _lxsdk=15fe3fc3ed0c8-026fd89dad80db-1f2a1709-1aeaa0-15fe3fc3ed0c8; _hc.v=5e7e0724-a23e-9959-4d71-7e62c30bcd1f.1511358480; __mta=55958036.1512546479523.1512546479523.1512546479523.1; switchcityflashtoast=1; pvhistory="6aaW6aG1Pjo8Lz46PDE1MTI1NjE2NjAwMDZdX1s="; m_flash2=1; cityid=3; source=m_browser_test_33; default_ab=shop.sql%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cshopreviewlist%3AA%3A1; _dp.ac.v=e0096bdb-f7b6-495b-8c97-3c7e48a732cb; thirdtoken=A0147C35E5B5F792F398BD2C1ADA1958; _thirdu.c=023528ce4bf93564efbc7e2d3f007520; dper=0c98df72d34b20bdc9d46a1872710ee5cdf90328c62ae1dd54bda9ede4f17ea5; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_0198477750; ctu=6f5c321e57fb5447cae079cc45db42fe86be844db21774a18318126fc97a76d3; JSESSIONID=433FE9537A57A087F197E889A5EDDE16; aburl=1; cye=hangzhou; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cy=344; s_ViewType=10; _lxsdk_s=1602e6a3b07-c02-20b-4ef%7C%7C62',
    }
    # base_url = 'http://www.dianping.com'
    headers['Referer']="http://www.dianping.com/"
    # headers['Referer']=""
    html = get_content(start_url,headers)#地区主页
    region_url_list = region_url(html)

    for url in region_url_list:#遍历行政区
        for i in range(1,51):#遍历50页
            if i == 1:
                headers['Referer'] = "http://www.dianping.com/"
                shop_url_list = get_shop_url(get_content(url+'p'+str(i)))
            elif i == 2:
                headers['Referer'] = "http://www.dianping.com/search/category/344/10/r6026"
                shop_url_list = get_shop_url(get_content(url + 'p' + str(i)))
            elif i>= 3:
                headers['Referer'] = "http://www.dianping.com/search/category/344/10/r6026p"+str(i-1)
                shop_url_list = get_shop_url(get_content(url + 'p' + str(i)))
            for shop_url in shop_url_list:#遍历店铺
                # print shop_url
                detail_html = get_content(shop_url,headers)
                print(detail_html)
                items = get_detail(detail_html)