#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-07 17:10:26
# Project: test

from pyspider.libs.base_handler import *
import sys,re,time,os,urlparse,pymysql
from pyquery import PyQuery as pq
reload(sys)
sys.setdefaultencoding('utf-8')

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://baike.baidu.com/item/钱塘江', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):

        with open('temp.txt','w+') as f:
            p = response.doc('body > div.body-wrapper > div.content-wrapper > div > div.main-content')
            p('div.top-tool').remove()#删除点赞数
            p('span.lemma-pinyin').remove()#删除拼音
            p('div.lemma-map').remove()#删除地图
            # p('div > div.album-list').remove()#删除图册
            content = '<div class=\"main-content\">{}</div>'.format(p.html(method='html'))
            content = content.replace('>编辑<','><')
            content = content.replace('>锁定<', '><')
            content = "<link rel=\"stylesheet\" type=\"text/css\" href=\"baidubaike.css\">"+content
            content = re.sub(r'href=\"[^\"<>]*baike.baidu.com/item/[^\"<>]*\"',r'',content)
            content = content.replace('data-src=\"','src=\"')
            content= re.sub(r'src=\"data:image/[^\"<>]*\"', r'', content)
            origin_pic_url_list = re.findall(r'src=\"([^\"<>]*.jpg)\"',content)
            server_path = '/picture_hzz/'  # 图片的服务器路径
            local_path = os.environ['HOME'] + '/.picture_hzz/'  # 图片的本地路径
            for url in origin_pic_url_list:
                pic_name = url.split('/')[-1]#得到图片的名称
                content = content.replace(url,server_path+pic_name)#修改网页的图片链接
                os.system("wget {} -O {}".format(url,local_path+pic_name))#下载图片
            f.write(content)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }