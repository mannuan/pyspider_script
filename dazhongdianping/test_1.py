# -*- coding:utf-8 -*-

import requests

def get_content(url,headers=None):
    response = requests.get(url,headers=headers)#发起了一次请求
    return response.content

start_url = "https://m.dianping.com/shop.sql/7740326/review_all"

if __name__ == '__main__':
    headers = {
        # 'Host': 'www.dianping.com',
        # 'Connection': 'keep-alive',
        # Cache-Control: max-age=0
        # Upgrade-Insecure-Requests: 1
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept': 'application/json, text/javascript',
        # 'Referer': 'http://www.dianping.com/search/category/344/10/r6023',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cookie': 'showNav=#nav-tab|0|0; navCtgScroll=0; _lxsdk_cuid=15fe3fc3ed0c8-026fd89dad80db-1f2a1709-1aeaa0-15fe3fc3ed0c8; _lxsdk=15fe3fc3ed0c8-026fd89dad80db-1f2a1709-1aeaa0-15fe3fc3ed0c8; _hc.v=5e7e0724-a23e-9959-4d71-7e62c30bcd1f.1511358480; __mta=55958036.1512546479523.1512546479523.1512546479523.1; switchcityflashtoast=1; pvhistory="6aaW6aG1Pjo8Lz46PDE1MTI1NjE2NjAwMDZdX1s="; m_flash2=1; cityid=3; source=m_browser_test_33; default_ab=shop.sql%3AA%3A1%7Cindex%3AA%3A1%7CshopList%3AA%3A1%7Cshopreviewlist%3AA%3A1; _dp.ac.v=e0096bdb-f7b6-495b-8c97-3c7e48a732cb; thirdtoken=A0147C35E5B5F792F398BD2C1ADA1958; _thirdu.c=023528ce4bf93564efbc7e2d3f007520; dper=0c98df72d34b20bdc9d46a1872710ee5cdf90328c62ae1dd54bda9ede4f17ea5; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_0198477750; ctu=6f5c321e57fb5447cae079cc45db42fe86be844db21774a18318126fc97a76d3; JSESSIONID=433FE9537A57A087F197E889A5EDDE16; aburl=1; cye=hangzhou; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cy=344; s_ViewType=10; _lxsdk_s=1602e6a3b07-c02-20b-4ef%7C%7C62',
    }
    html = get_content(start_url, headers)  # 地区主页
    f = open('/home/mininet/test.html','w')
    f.write(html)
    f.close()
