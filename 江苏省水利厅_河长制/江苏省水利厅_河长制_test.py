#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-25 15:24:21
# Project: test8

from pyspider.libs.base_handler import *
import os


class Handler(BaseHandler):
    crawl_config = {
        "headers":{
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1',
        "Accept": "*/*",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://jswater.jiangsu.gov.cn/art/2017/8/7/art_42975_5629714.html', fetch_type='js', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        selectors = [
            ('#barrierfree_container > div.w1100.center > div.main-fl.bt-left > div:nth-child(6)', 'p', 'a>img'),
            ('#zoom', 'p', 'img'),
            ('#barrierfree_container > div.w1100.center > div.main-fl.bt-left > div:nth-child(6)', 'span', 'a>img')]
        text = ''
        for (selector1, selector2, selector3) in selectors:
            for each in response.doc(selector1).items(selector2):
                img_url = each(selector3).attr.src
                if img_url is not None:
                    img_url_tmp = img_url.split('?')[0]  # 去除url后面的参数部分
                    img_name = img_url_tmp.replace('http://', '').replace('https://', '').replace('/', '_')
                    img_tail = '.' + img_name.split('.')[-1]
                    img_head = img_name.replace(img_tail, '').replace('.', '-')
                    img_name = img_head + img_tail
                    server_path = '/picture_hzz/' + img_name
                    local_path = os.environ['HOME'] + '/.picture_hzz/' + img_name
                    os.system('wget {} -O {}'.format(img_url, local_path))
                    part = "<p><img src={}></p>".format(server_path)  # 为了显示图片更加清楚把img标签加入p标签里面
                else:
                    part = '<p>{}</p>'.format(each.text())
                    part = part.replace('\'', '\\\'').replace('\"', '\\\"')
                text += part
            if text.replace(' ', '').replace('　', '').replace('\n', '').replace('\r', '') != '':
                break
        if text.replace(' ', '').replace('　', '').replace('\n', '').replace('\r', '') == '':  # 如果text仍然为空
            text = '<p>' + response.doc(
                '#barrierfree_container > div.w1100.center > div.main-fl.bt-left > div:nth-child(6)').text() + '</p>'
        print text

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }