#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-03-12 20:08:17
# Project: 20180312200815

from pyspider.libs.base_handler import *
import json,re,sys,time
reload(sys)
sys.setdefaultencoding('utf8')
from pymongo import MongoClient


class Handler(BaseHandler):
    crawl_config = {
    }
    conn = MongoClient('localhost', 27017)
    db = conn.wuxiaworld #连接wuxiaworld数据库，没有则自动创建
    novels = db.novels #使用novels集合,没有则自动创建

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.wuxiaworld.com/language/chinese', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('body > div.main > div > div > div > div.col-lg-9.col-md-8 > div.section.mb-0 > div > div > div > ul > li').items():
            novel_url = each('div.media-body > div > a').attr.href#书对应的url
            novel_title = each('div.media-body > div > a > h4').text()  # 书名
            novel_pic = each('div.media-left > a > img').attr.src,#书对应的图片
            novel_chapter_count = int((lambda x:0 if x == '' else x)(filter(str.isdigit, each('div.media-body > div > ul > li').text())))#章节数
            novel_synopsis = each('div.media-body').text().replace(novel_title,'').split('Chapters')[-1].strip()#概述
            self.crawl(novel_url, callback=self.part_page, save={
                    'novel_url' : novel_url,
                    'novel_title':novel_title,
                    'novel_pic':novel_pic,
                    'novel_chapter_count':novel_chapter_count,
                    'novel_synopsis':novel_synopsis
                }
            )

    @config(priority=2)
    def part_page(self, response):
        novel_url = response.save['novel_url']
        novel_title = response.save['novel_title']
        novel_pic = response.save['novel_pic']
        novel_chapter_count = response.save['novel_chapter_count']
        novel_synopsis = response.save['novel_synopsis']
        for each in response.doc('#accordion > div').items():
            part_num = int((lambda x:0 if filter(str.isdigit, x) == '' else x)(each('div > h4 > span.book').text()))#书的部分编号
            part_title = each('div > h4 > span.title > a').text().split(':')[-1].strip()#书的部分题目
            text_chapter = 0
            for each1 in each('ul.list-unstyled.list-chapters > li > a').items():
                text_title = each1.text()#正文标题
                text_url = each1.attr.href#正文链接
                # text_chapter = float((lambda x:0 if x == [] else x[0])(re.findall(r'[\d.]+',text_title)))#正文的章节数
                text_chapter += 1
                self.crawl(text_url, callback=self.text_page, save = {
                    'novel_url' : novel_url,
                    'novel_title': novel_title,
                    'novel_pic': novel_pic,
                    'novel_chapter_count': novel_chapter_count,
                    'novel_synopsis': novel_synopsis,
                    'part_num' : part_num,
                    'part_title' : part_title,
                    'text_url' : text_url,
                    'text_title' : text_title,
                    'text_chapter' : text_chapter
                })

    @config(priority=3)
    def text_page(self, response):
        novel_url = response.save['novel_url']
        novel_title = response.save['novel_title']
        novel_pic = response.save['novel_pic']
        novel_chapter_count = response.save['novel_chapter_count']
        novel_synopsis = response.save['novel_synopsis']
        part_num = response.save['part_num']
        part_title = response.save['part_title']
        text_url = response.save['text_url']
        text_title = response.save['text_title']
        text_chapter = response.save['text_chapter']
        text = ''
        for each in response.doc('#chapterContent > p').items():
            text += each.text() + '\n'
        if text == '':
            for each in response.doc('body > div.main > div > div > div > div.col-lg-9.col-md-8 > div.section > div > div.panel.panel-default > div.p-15 > div.fr-view > p').items():
                text += each.text() + '\n'
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        data = {
            'novel_url': novel_url,
            'novel_title': novel_title,
            'novel_pic': novel_pic,
            'novel_chapter_count': novel_chapter_count,
            'novel_synopsis': novel_synopsis,
            'part_num': part_num,
            'part_title': part_title,
            'text_url': text_url,
            'text_title': text_title,
            'text_chapter' : text_chapter,
            'text':text,
            'crawl_time': crawl_time
        }
        if len(list(self.novels.find({
            'novel_url': novel_url,
            'part_num': part_num,
            'text_url': text_url,
        }))) == 0:
            self.novels.insert(data)
        else:
            self.novels.update({
                'novel_url': novel_url,
                'part_num': part_num,
                'text_url': text_url,
            },{'$set':{
                'novel_title': novel_title,
                'novel_pic': novel_pic,
                'novel_synopsis': novel_synopsis,
                'novel_chapter_count': novel_chapter_count,
                'part_title': part_title,
                'text_title': text_title,
                'text_chapter': text_chapter,
                'text':text,
                'crawl_time': crawl_time
            }
        })
