#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-05-09 16:46:49
# Project: weixin

from pyspider.libs.base_handler import *
from pyspider.libs.weixin.header_switch import HeadersSelector
from pyspider.libs.mycommon.util import *
from pyspider.libs.mycommon.regex import Regex
import time
import json
import re
import os
from pymongo import MongoClient

class Handler(BaseHandler):
    MONGODB_PORT = 27017
    MONGODB_HOST = '10.1.17.15'
    CONN = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = CONN.weixin
    imgs = db.imgs
    host = '122.224.129.35'
    port = 23306
    @every(minutes=24 * 60 * 10)
    def on_start(self):#对数据库里面的关键字进行公众号的搜索
        for row in query_data(host=self.host,port=self.port,table='weixin_public',field='public_name'):
            url = str("http://weixin.sogou.com/weixin?type=1&s_from=input&query=%s&ie=utf8&_sug_=n&_sug_type_="%row)
            self.crawl(url, callback=self.index_page,headers=HeadersSelector.headers_sougou)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):#进入每个搜索出来的公众号
        for each in response.doc('div > ul > li > div > div.txt-box > p.tit > a').items():
            public_name = each.text().strip().replace(' ','')
            self.crawl(each.attr.href, callback=self.list_page,save={'public_name':public_name},headers=HeadersSelector.headers_weixin)

    @config(priority=3)
    def list_page(self, response):#进入每个公众号的每一篇文章
        text = response.text
        for line in text.split('\n'):
            if 'msgList' in line:
                _json = re.sub('^[^{]+?({.*});$', r'\1', line.strip())
                _json = json.loads(_json)
                for i in _json.get('list'):
                    title = i.get('app_msg_ext_info').get('title')
                    _time = time.strftime('%Y-%m-%d %H:%M:%S',
                                          time.localtime(int(i.get('comm_msg_info').get('datetime'))))
                    url = 'https://mp.weixin.qq.com%s' % i.get('app_msg_ext_info').get('content_url').replace('amp;','')
                    save = merge_dict(response.save,{'title':title,'time':_time})
                    self.crawl(url,callback=self.detail_page,save=save,headers=HeadersSelector.headers_weixin)

    @config(priority=2)
    def detail_page(self, response):
        result = response.save
        content = (lambda c:c.html().strip())((lambda p:p.remove('script'))((lambda css:response.doc(css))('#js_content')))
        content = "<div class=\"rich_media_content\">%s</div>" % content
        content = re.sub(r' id=\".*?\"|id=\".*?\" |&#13;|[\f\n\r\t\v]*', '', content)  # 去除id
        content = re.sub('[ ]{2,}', '', content)
        img_list = re.findall(Regex.HTML_IMG_SRC_REGEX,content)
        img_name_list = [list(filter(lambda d: True if len(d) >= max([len(i) for i in img.split('/')]) else False, img.split('/')))[0] for img in img_list]
        for i in range(len(img_list)):
            content = content.replace(img_list[i], 'http://122.224.129.35:28080/picture_hzz/%s' % img_name_list[i])
            save_data_to_mongodb(target=self.imgs,key={'url':img_list[i]},data={'url':img_list[i],'name':img_name_list[i],
                                                                                'path':'%s/.picture_hzz/%s'%(os.environ['HOME'], img_name_list[i])})
        result = merge_dict(result,{'main_body':content,'spider_time':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),'url':response.url})
        return result

    def on_result(self, result):
        save_data(host=self.host,port=self.port,table='weixin_info',key='url',data=result)