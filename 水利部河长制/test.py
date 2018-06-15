# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-01-31 10:56:25
# Project: 20180131105623

from pyspider.libs.base_handler import *
import re,json,os
from pyquery import PyQuery as pq

class Handler(BaseHandler):
    crawl_config = {
    }

    context_css = "<link rel=\"stylesheet\" type=\"text/css\" href=\"web_hzz/css/style.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"web_hzz/css/bootstrap.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"web_hzz/css/font-awesome.min.css\">"
    context_html_tmp = "<article class=\"entry\">{}</div>"

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.mwr.gov.cn/ztpd/gzzt/hzz/mtjj/201708/t20170811_973456.html', fetch_type='js',callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        p = response.doc('body > div.main1')
        text_list = [each for each in p('p').items()]
        text = ''
        for i in range(len(text_list)):
            #(位置属性,图片url,一段话的内容,上一个图片的url)
            flag = (text_list[i].attr.align,
                    text_list[i]('img').attr.src,
                    (lambda x:None if x == '' else x)(text_list[i].text().strip()),
                    (lambda x:text_list[x-1]('img').attr.src if x>=1 else None)(i))
            if flag[0] == 'center' and flag[1] != None and flag[2] == None:#如果是图片
                img_url = flag[1]
                img_name = img_url.split('/')[-1]
                local_path = os.environ['HOME'] + '/.picture_hzz/{}'.format(img_name)
                server_path = '/picture_hzz/{}'.format(img_name)
                text += "<img src=\"{}\" alt="" class=\"entry__img\">".format(server_path)
                os.system('wget {} -O {}'.format(img_url, local_path))
            elif flag[0] == 'center' and flag[1] == None and flag[2] != None and flag[3] == None:#如果是标题
                text+="<h3 class=\"text-center\">{}</h3>".format(flag[2])
            elif flag[0] == 'center' and flag[1] == None and flag[2] != None and flag[3] != None:#如果是图片下的文字
                text+="<figcaption>{}</figcaption>".format(flag[2])
            elif flag[0] != 'center' and flag[1] == None and flag[2] != None:#如果是正文
                text+="<p>{}</p>".format('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'+flag[2])
        text = re.sub('^<h3','<div class=\"entry__article\"><h3',text)#开头就是标题
        text = re.sub('</h3>$', '</div></h3>', text)#以标题结尾
        text = re.sub('^<img','<div class=\"entry__img-holder text-center\"><img',text)#开头就是图片
        text = re.sub('\">$', '\"></div>', text)#图片后面没有图片名并且是最后一个
        text = re.sub('</figcaption>$', '</figcaption></div>', text)#图片后面有图片名并且是最后一个
        text = re.sub('^<p>', '<div class=\"entry__article\"><p>', text)#开头就是正文
        text = re.sub('</p>$', '</p></div>', text)#以正文结尾
        text = re.sub('</p><img','</p></div><div class=\"entry__img-holder text-center\"><img',text)#图片在正文的后面
        text = re.sub('</figcaption><p>','</figcaption></div><div class=\"entry__article\"><p>',text)#有图片名的图片在正文的前面
        text = re.sub('\"><p>', '\"></div><div class=\"entry__article\"><p>', text)#没有图片名的图片在正文的前面
        text = re.sub('</h3><img','</h3></div><div class=\"entry__img-holder text-center\"><img',text)#图片在标题的后面
        text = re.sub('</figcaption><h3','</figcaption></div><div class=\"entry__article\"><h3',text)#有图片名的图片在标题的前面
        text = self.context_css + self.context_html_tmp.format(text)
        with open('/home/mininet/test.txt', 'w+') as f:
            f.write(text)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }