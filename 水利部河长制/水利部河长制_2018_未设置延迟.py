#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-21 16:41:40
# Project: 水利部河长制

from pyspider.libs.base_handler import *
import time,pymysql,sys,random,re,os
reload(sys)
sys.setdefaultencoding('utf8')

class Handler(BaseHandler):
    crawl_config = {
        "headers":{
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Accept": "*/*",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    }
    }

    list_forums = [{'forum':'zyjs','forum_num':1,'forum_type':u'中央精神','forum_id':0},
                   {'forum':'zydt','forum_num':2,'forum_type':u'重要动态','forum_id':1},
                   {'forum':'gzbs/slb','forum_num':2,'forum_type':u'工作部署-水利部','forum_id':1},
                   {'forum':'gzbs/ly','forum_num':5,'forum_type':u'工作部署-流域','forum_id':1},
                   {'forum':'gzbs/df','forum_num':25,'forum_type':u'工作部署-地方','forum_id':1},
                   {'forum':'gzjz/gzfa','forum_num':2,'forum_type':u'工作进展-工作方案','forum_id':1},
                   # {'forum':'gzjz/zztx','forum_num':1,'forum_type':u'工作进展-组织体系','forum_id':1},
                   {'forum':'gzjz/gzzd','forum_num':1,'forum_type':u'工作进展-工作制度','forum_id':1},
                   {'forum':'gzjz/sjhzxh','forum_num':1,'forum_type':u'工作进展-省级河长巡河','forum_id':1},
                   {'forum':'dfldt','forum_num':2,'forum_type':u'地方领导谈','forum_id':1},
                   {'forum':'jcsj','forum_num':3,'forum_type':u'基层实践','forum_id':1},
                   {'forum':'mtjj','forum_num':13,'forum_type':u'媒体聚焦','forum_id':1},
                   {'forum':'gzjb','forum_num':10,'forum_type':u'工作简报','forum_id':1}]

    context_css = "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/articleDetail.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/bootstrap.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/font-awesome.min.css\">"
    context_html_tmp = "<article class=\"entry\">{}</article>"

    @every(minutes=24 * 60)
    def on_start(self):
        for forum in self.list_forums:
            url = 'http://www.mwr.gov.cn/ztpd/gzzt/hzz/{}/index.html'.format(forum.get('forum'))
            self.crawl(url, fetch_type='js', callback=self.index_page, save={'forum_type':forum.get('forum_type'),'forum_id':forum.get('forum_id')})
            for p in range(1,forum.get('forum_num')):
                url = 'http://www.mwr.gov.cn/ztpd/gzzt/hzz/{}/index_{}.html'.format(forum.get('forum'),p)
                self.crawl(url, fetch_type='js', callback=self.index_page, save={'forum_type':forum.get('forum_type'),'forum_id':forum.get('forum_id')})

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('body > div.main1 > table > tbody > tr > td > table:nth-child(2) > tbody > tr').items():
            url = each('td:nth-child(2)>a').attr.href
            if '.html' in url:
                title = each('td:nth-child(2)>a').text().strip()
                created_at = each('td:nth-child(3)').text().strip()
                forum_type = response.save['forum_type']
                forum_id = response.save['forum_id']
                self.crawl(url, fetch_type='js', callback=self.detail_page, save={'title':title,'created_at':created_at,'forum_type':forum_type,'forum_id':forum_id})

    @config(priority=2)
    def detail_page(self, response):
        url = response.url
        title = response.save['title']
        created_at = response.save['created_at']
        ###############
        p = response.doc('body > div.main1')
        p('script').remove()
        p('style').remove()
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
                server_path = 'http://122.224.129.35:28080/picture_hzz/{}'.format(img_name)
                text += "<img src=\"{}\" alt="" class=\"entry__img\">".format(server_path)
                os.system('wget {} -O {}'.format(img_url, local_path))
            elif flag[0] == 'center' and flag[1] == None and flag[2] != None and flag[3] == None:#如果是标题
                text+="<h3 class=\"text-center\">{}</h3>".format(flag[2])
            elif flag[0] == 'center' and flag[1] == None and flag[2] != None and flag[3] != None:#如果是图片下的文字
                text+="<figcaption>{}</figcaption>".format(flag[2])
            elif flag[0] != 'center' and flag[1] == None and flag[2] != None:#如果是正文
                text+="<p>{}</p>".format('&nbsp;&nbsp;&nbsp;&nbsp;'+flag[2])
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
        ###############
        forum_type = response.save['forum_type']
        forum_id = response.save['forum_id']
        crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#爬虫的时间
        result = [url,title,created_at,text,'',forum_type,forum_id,crawl_time,u'水利部河长制']
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from website where title = %s" , result[1])
        rows = cur.fetchall()
        if len(rows) == 0:
            try:
                sql = 'INSERT INTO website(url,title,push_time,context,come_from,page_type,type_id,spider_time,source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 批量插入
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        else:
            result = result[::-1]
            try:
                sql = 'UPDATE website SET source=%s,spider_time=%s,type_id=%s,page_type=%s,come_from=%s,context=%s,push_time=%s,title=%s WHERE url=%s'
                # 批量更新
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()