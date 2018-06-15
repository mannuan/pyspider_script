#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# modified on 2018-04-27 15:57:58
# Project: 百度百科网站版_未设置延迟v2

from pyspider.libs.base_handler import *
import pymysql,time,re,os,sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository', charset='utf8')
        cur = conn.cursor()
        cur.execute("select name,url,state from baidubaike_entry")
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        for row in rows:
            if row[2] == 1:
                self.crawl(row[1], save={'river_name':row[0]}, callback=self.find_page)
        # self.crawl('http://baike.baidu.com/item/西塘河',save={'river_name':'西塘河'},callback=self.find_page)

    @config(age=10 * 24 * 60 * 60)
    def find_page(self, response):#寻找一个词条的多个同义词
        title_url_list = list()
        for each in response.doc('body > div.body-wrapper > div.before-content > div > ul').items('li.item > a'):
            title = each.attr('title')
            url = each.attr('href')
            title_url_list.append((title,url))
            self.crawl(url,save={'river_name':title},callback=self.index_page)
        if title_url_list:#如果为空
            river_name = response.save['river_name']
            self.crawl(response.url,save={'river_name':river_name},callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        entry_name = response.doc('body > div.body-wrapper > div.content-wrapper > div > div.main-content > '
                                  'dl.lemmaWgt-lemmaTitle.lemmaWgt-lemmaTitle- > dd > h1').html()#词条名称
        if not entry_name:#词条名称不存在,直接结束爬虫
            return
        entry_mark = response.doc('body > div.body-wrapper > div.content-wrapper > div > '
                                  'div.main-content > dl.lemmaWgt-lemmaTitle.lemmaWgt-lemmaTitle- > dd > h2').html()#词条角标
        if entry_mark:#如果词条的角标存在
            if '河' not in entry_mark and '溪' not in entry_mark and\
                '江' not in entry_mark and '海' not in entry_mark and '地名' not in entry_mark:
                #如果"河"&&"溪"&&"江"&&"海"&&"地名"都不在词条的角标里面, 直接结束怕爬虫
                return
        else:#如果词条角标不存在
            entry_mark = ''
        title = entry_name + entry_mark
        url = response.url
        text = response.doc('body > div.body-wrapper > div.content-wrapper').text()
        text = re.sub(u'[^\u4e00-\u9fa5]*','', text)
        try:
            status = int(os.popen('python3 %s/SVD/heliufenlei.py %s'%(os.environ['HOME'],str(text))).read())#河流分类的状态
        except Exception as e:
            status = 0
        if not status:
            return
        spider_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        type_id = 0
        source = '百度百科'
        #百度百科的html格式
        p = response.doc('body > div.body-wrapper > div.content-wrapper > div > div.main-content')
        p('div.top-tool').remove()#删除点赞数
        p('span.lemma-pinyin').remove()#删除拼音
        p('div.lemma-map').remove()#删除地图
        # p('div > div.album-list').remove()#删除图册
        content = '<div class=\"main-content\">{}</div>'.format(p.html(method='html'))
        content = content.replace('>编辑<','><')
        content = content.replace('>锁定<', '><')
        content = "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/baidubaike.css\">"+content
        content = re.sub(r'href=\"[^\"<>]*baike.baidu.com/item/[^\"<>]*\"',r'',content)
        content = content.replace('data-src=\"','src=\"')
        content= re.sub(r'src=\"data:image/[^\"<>]*\"', r'', content)
        origin_pic_url_list = re.findall(r'src=\"([^\"<>]*.jpg)\"',content)
        server_path = 'http://122.224.129.35:28080/picture_hzz/'  # 图片的服务器路径
        local_path = os.environ['HOME'] + '/.picture_hzz/'  # 图片的本地路径
        for pic_url in origin_pic_url_list:
            pic_name = pic_url.split('/')[-1]#得到图片的名称
            content = content.replace(pic_url,server_path+pic_name)#修改网页的图片链接
            os.system("wget {} -O {}".format(pic_url,local_path+pic_name))#下载图片
        #结果
        result = [title,url, '', content, '', '', type_id, spider_time, source]
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        cur.execute('select * from website where title = %s' , result[0])
        rows = cur.fetchall()
        if len(rows) == 0:
            try:
                sql = 'INSERT INTO website(title,url,push_time,context,come_from,page_type,type_id,spider_time,source) ' \
                      'values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 批量插入
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        else:
            result = result[::-1]
            try:
                sql = 'UPDATE website SET source=%s,spider_time=%s,type_id=%s,page_type=%s,come_from=%s,' \
                      'context=%s,push_time=%s,url=%s WHERE title=%s'
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