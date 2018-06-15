#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-05 18:22:42
# Project: 19louNoteAndComment
host = "127.0.0.1"
port = 3306
user = "repository"
passwd = "repository"
db = 'repository'

from pyspider.libs.base_handler import *
import datetime
import time
import pymysql
import json
import sys


class Handler(BaseHandler):
    crawl_config = {
        "headers": {
            'Accept': 'text/css,*/*;q=0.1',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
        }
    }

    @every(minutes=60)
    def on_start(self):
        self.spiderNoteUrl()
        self.spiderContext()
        self.spiderNoteNum()
        self.spiderComment()

    @config(priority=10, age=0)
    def spiderNoteUrl(self):
        prefix = "http://www.19lou.com/forum-269-"
        postfix = ".html"
        for i in range(1, 41):
            url = prefix + str(i) + postfix
            self.crawl(url, fetch_type='js', callback=self.listNotePage)

    @config(priority=9, age=0)
    def listNotePage(self, response):
        for each_tbody in response.doc('tbody').items():
            note_url = each_tbody('tr>th>div>a').attr.href
            note_title = each_tbody('tr>th>div>a').attr.title
            author_href = each_tbody('td.author>a').attr.href
            author_name = each_tbody('td.author>a').attr.title
            author_push_time = each_tbody('td.author>span.color9').text()
            update_time = each_tbody('td.lastpost>span.numeral').text()
            self.insertNote(note_url, note_title, author_href, author_name, author_push_time, update_time)

    def insertNote(self, note_url, note_title, author_href, author_name, push_time, update_time):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()

        # 检查url和title是否有重复
        cur.execute("select * from invitation where (note_title = %s or note_url = %s) and source = '19楼'", (note_title, note_url))
        rows = cur.fetchall()
        if len(rows) == 0:
            now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            cur.execute(
                "insert into invitation(note_title,note_url,source,push_time,crawl_time,push_name) values(%s,%s,'19楼',%s,%s,%s)",
                (note_title, note_url, push_time, now_time, author_name))
            conn.commit()
            cur.close()
            conn.close()

    @config(priority=7)
    def spiderContext(self):
        noteList = self.getContextIsNullNote()
        for row in noteList:
            id = row[0]
            url = row[1] + "?timestamp=" + str(int(time.time()))
            self.crawl(url, fetch_type='js', callback=self.getNoteContext, save={"id": id})

    def getContextIsNullNote(self):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("select id , note_url from invitation where note_context is null and note_id is null and source = '19楼'")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return rows

    @config(priority=6, age=0)
    def getNoteContext(self, response):
        wordStr = ""
        for floor in response.doc('DIV.clearall.floor.first').items():
            for content in floor('DIV.thread-cont').items():
                wordStr = content.text()
                break
            break
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("update invitation set note_context = %s where id = %s and source = '19楼'", (wordStr, response.save["id"]))
        conn.commit()
        cur.close()
        conn.close()

    @config(priority=5, age=0)
    def spiderNoteNum(self):
        auditedNoteList = self.getAuditNote()
        for note in auditedNoteList:
            id = note[0]
            url = note[1] + "?timestamp=" + str(int(time.time()))
            self.crawl(url, fetch_type='js', callback=self.getNoteNums, save={"id": id})

    @config(priority=4, age=0)
    def getNoteNums(self, response):
        for ul in response.doc('ul.fr.clearall.color9.view-hd-num').items():
            lookNum = ul('li:nth-child(1)>i').text()
            replyNum = ul('li:nth-child(2)>i').text()
            self.insertTrend(response.save["id"], lookNum, replyNum)
            break

    def insertTrend(self, id, lookNum, replyNum):
        spiderTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()

        cur.execute("insert into invitation_trend(id , crawl_time , looks_count , comments_count) VALUES (%s,%s,%s,%s)",
                    (str(id), spiderTime, str(lookNum), str(replyNum)))
        conn.commit()
        cur.close()
        conn.close()

    def getAuditNote(self):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("select id , note_url from invitation where audit = 1 and source = '19楼'")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return rows

    @config(priority=3, age=0)
    def spiderComment(self):
        auditedNoteList = self.getAuditNote()
        for note in auditedNoteList:
            id = note[0]
            url = note[1] + "?timestamp=" + str(int(time.time()))
            if self.judgeCommentNum(id):
                self.crawl(url, fetch_type='js', callback=self.analysisPageOne, save={"id": id, "url": url})

    @config(priority=2, age=0)
    def analysisPageOne(self, response):
        page_info = response.doc('a.page-last').items()
        pageNum = 1
        for page in page_info:
            pageNum = int(page.attr.href.split('-')[4])
            break
        result = self.getTimeAndLou(response.save["id"])
        maxCount = result["maxCount"]
        time = result["time"]
        url = response.save["url"]
        for i in range(1, pageNum + 1):
            pageUrl = url[0:len(url) - 8] + str(i) + "-1.html"
            self.crawl(pageUrl, fetch_type='js', callback=self.catchComment,
                       save={"pageNum": i, "count": maxCount, "timeYu": time, "note_id": response.save["id"]})

    def insertComment(id, author_href, author_name, time, json_str):
        lou_id = self.getLouId(id)
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        spider_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        cur.execute("insert into invitation_comment values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (str(id), str(lou_id), str(json_str), str(spider_time), str(time), '19楼', '0', str(author_name)))
        conn.commit()
        cur.close()
        conn.close()

    def getLouId(self, id):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("select max(comment_id) from invitation_comment where id = %s and source = '19楼'", (id))
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return int(rows[0][0]) + 1

    @config(priority=1, age=0)
    def catchComment(self, response):
        pageNum = int(response.save["pageNum"])
        if pageNum != 1:
            for floor_info in response.doc("DIV.clearall.floor.first").items():
                time = floor_info('DIV.cont-hd.clearall>p.fl.link1').text()
                author_href = floor_info('DIV.uname>a').attr.href
                author_href = author_href[2:len(author_href)]
                author_name = floor_info('DIV.uname>a').attr.title
                for content_info in floor_info('DIV.thread-cont').items():
                    for s in content_info('dl'):
                        s.extract()
                    wordStr = content_info.text()
                    wordStr = wordStr.replace('\n', '')
                    wordStr = wordStr.replace('\t', '')
                    wordStr = wordStr.replace(' ', '')
                    if time > response.save["timeYu"]:
                        self.insertComment(response.save["note_id"], author_href, author_name, time, wordStr)
                    break
                break
        for floor_info in response.doc("DIV.clearall.floor").items():
            time = floor_info('DIV.cont-hd.clearall>p.fl.link1').text()
            author_href = floor_info('DIV.uname>a').attr.href
            author_href = author_href[2:len(author_href)]
            author_name = floor_info('DIV.uname>a').attr.title
            for content_info in floor_info('DIV.thread-cont').items():
                for s in content_info('dl'):
                    s.extract()
                wordStr = content_info.text()
                wordStr = wordStr.replace('\n', '')
                wordStr = wordStr.replace('\t', '')
                wordStr = wordStr.replace(' ', '')
                if time > response.save["timeYu"]:
                    self.insertComment(response.save["note_id"], author_href, author_name, time, wordStr)
                break
            break

    def judgeCommentNum(self, id):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from invitation_trend where id = %s order by crawl_time desc limit 2", (str(id),))
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        if len(rows) == 0 or len(rows) == 1:
            return True
        if rows[0][3] == rows[1][3]:
            return True
        return False

    def getTimeAndLou(self, id):
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        cur = conn.cursor()
        cur.execute(
            "select comment_id , crawl_time from invitation_comment where id = %s and source = '19楼' order by comment_id desc limit 1",
            (str(id),))
        rows = cur.fetchall()
        result = {}
        if len(rows) == 0:
            result["maxCount"] = 0
            cur.execute("select push_time from invitation where id = %s and source = '19楼'", (str(id),))
            rows = cur.fetchall()
            result["time"] = str(rows[0][0]) + " 00:00"
        else:
            result["maxCount"] = int(rows[0][0]) + 1
            result["time"] = rows[0][1]
        conn.commit()
        cur.close()
        conn.close()
        return result