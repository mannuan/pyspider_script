#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-02-04 10:34:58
# Project: 百度百科网站版

from pyspider.libs.base_handler import *
import pymysql,time,re,os,urlparse,sys
from pyquery import PyQuery
reload(sys)
sys.setdefaultencoding('utf-8')

class Handler(BaseHandler):
    crawl_config = {
    }

    context_css = "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/style.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/bootstrap.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/font-awesome.min.css\">"
    context_html_tmp = "<article class=\"entry\">{}</article>"

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
                self.crawl(row[1], save={'river_name':row[0]}, callback=self.index_page)

    def filter_page(self, response, *args):
        server_path = '/picture_hzz/'
        local_path = os.environ['HOME'] + '/.picture_hzz/'
        content = ''
        for cs in args:
            p = response.doc(cs)  # rd是一个PyQuery对象
            p('script').remove()  # 去除script标签
            p('style').remove()  # 去除style标签
            content += (
                lambda x: '' if x is None else re.sub(
                    r'[ ]+[^ \"</>=]+[ ]*=[ ]*?\"(?!https://|http://)[^\"<>]*?\"|[\f\n\r]+', '', x))(
                p.html())  # 先去除没有用的class和style属性
        original_url_list = []
        regex = re.compile(
            r'<(?!div|img)[^ </>\"]+([^<>]*)[ ]+(?!href)[^ </>\"]+[ ]*=[ ]*?\"((?=https://|http://)[^ \"<>]+)?\"([^<>]*)[/]{0,1}?>')  # 标签不是img
        content = regex.sub(r'<img\1 src="\2"\3>', content)  # 更改为img标签
        original_url_list.extend([url[1] for url in regex.findall(content)])  # 原始的img url
        regex = re.compile(
            r'<(?=img)[^ </>\"]+([^<>]*)[ ]+(?=src|data-src)[^ </>\"]+[ ]*=[ ]*?\"((?=https://|http://)[^ \"<>]+)?\"([^<>]*)[/]{0,1}?>')  # 标签是img
        content = regex.sub(r'<img\1 src="\2"\3>', content)  # 更改为img标签
        original_url_list.extend([url[1] for url in regex.findall(content)])  # 原始的img url
        url_list = []  # 可用于下载的img url
        for i in range(len(original_url_list)):  # 过滤img url
            params = dict(
                [(k, v[0]) for k, v in urlparse.parse_qs(urlparse.urlparse(original_url_list[i]).query).items()])
            if len(params) != 0:
                url = (lambda url, src: url.split('?')[0] if src is None else src)(original_url_list[i],
                                                                                   params.get('src'))  # 修改后的img url
                url_list.append(url)
                content = content.replace(original_url_list[i], url)
            else:
                url_list.append(original_url_list[i])
        time_list = []
        for i in range(len(original_url_list)):
            name = str(time.time()).replace('.', '')
            time_list.append(name)
            time.sleep(0.01)
        pic_list = []
        download_pic_list = []
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',
                               charset='utf8')
        cur = conn.cursor()
        for i in range(len(original_url_list)):
            cur.execute("select name,url from hzz_local_picture where url = %s", url_list[i])
            row = cur.fetchone()
            if row is None:
                cur.execute("insert into hzz_local_picture values(%s,%s)", [time_list[i], url_list[i]])
                pic_list.append((time_list[i], url_list[i]))
                download_pic_list.append((time_list[i], url_list[i]))
            else:
                pic_list.append((row[0].encode('utf-8'), row[1].encode('utf-8')))
            conn.commit()
        cur.close()
        conn.close()
        for pic in pic_list:
            content = content.replace(pic[1], server_path + pic[0])
        for pic in download_pic_list:
            os.system('wget {} -O {}'.format(pic[1], local_path + pic[0]))
        return content

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        title = response.save['river_name']
        url = response.url
        spider_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 爬虫的时间
        type_id = 0
        source = '百度百科'
        if url.find('https://baike.baidu.com/error.html') == 0:
            result = None
        else:
            context = self.filter_page(response,'body > div.body-wrapper > div.content-wrapper > div > div.main-content')
            for i in ['em','span','a']:
                context = re.sub(r'<{}[^<>]*>'.format(i),r'',context)#删除a标签
                context = re.sub(r'</{}>'.format(i), r'', context)#删除a标签
            for i in ['em','div','span']:#替换成p标签
                context = re.sub(r'<([/]*){}([/]*)>'.format(i),r'<\1p\2>',context)
            context = re.sub(r'<p></p>', r'', context)#删除空标签
            context = re.sub(r'<p/>', r'', context)#删除空标签
            for i in range(10):#去除多层多余标签
                context = re.sub(r'<p>(<p>(?!<p>|</p>)[^<>]+<p/>)<p/>',r'\1',context)
            context = re.sub(r'<[/]*(?=span|em)[^ \"</>]+[/]*>',r'',context)#删除span和em
            for count in range(10):
                for i in re.findall(r'<([^ \"<>]+)></\1>',context):#删除空标签
                    context = context.replace('<{}></{}>'.format(i,i),'')
                    context = context.replace('<{}/>'.format(i), '')
            context = re.sub(r'<a[^<>]*>', r'', context)#删除链接
            context = re.sub(r'</a>', r'', context)#删除链接
            context = re.sub(r'<div>',r'<p>',context)
            context = re.sub(r'</div>', r'</p>', context)
            context = re.sub(r'<p>([^<>]*)<img src=\"([^ \"<>]+)\"/></p>',r'<p>\1</p><img src="\2" alt="" class="entry__img"/>',context)
            py = PyQuery(context)
            context = py.html()
            context = re.sub(r'(<img[^<>]+/>)<p>([^<>]+)</p>',r'\1<figcaption>\2</figcaption>',context)
            context = re.sub(r'<p></p>',r'',context)
            py = PyQuery(context)
            context = py.html()
            context = re.sub(r'<p></p>', r'', context)
            context = re.sub(r'<p/>', r'', context)
            context = re.sub(r'(<p>[^<>]*)<img',r'\1</p><img',context)
            context = re.sub(r'(</p>(?!</p>).*)</p>',r'\1',context)
            context = re.sub(r'(<p>(?!</p>).*)<p>', r'\1', context)
            context = re.sub(r'<([/]*)h[1-9]>',r'<\1h3>',context)
            context = re.sub(r'<h3>',r'<h3 class="text-center">',context)
            context = re.sub('^<h3', '<div class=\"entry__article\"><h3', context)  # 开头就是标题
            context = re.sub('</h3>$', '</div></h3>', context)  # 以标题结尾
            context = re.sub('^<img', '<div class=\"entry__img-holder text-center\"><img', context)  # 开头就是图片
            context = re.sub('\">$', '\"></div>', context)  # 图片后面没有图片名并且是最后一个
            context = re.sub('</figcaption>$', '</figcaption></div>', context)  # 图片后面有图片名并且是最后一个
            context = re.sub('^<p>', '<div class=\"entry__article\"><p>', context)  # 开头就是正文
            context = re.sub('</p>$', '</p></div>', context)  # 以正文结尾
            context = re.sub('</p><img', '</p></div><div class=\"entry__img-holder text-center\"><img', context)  # 图片在正文的后面
            context = re.sub('</figcaption><p>', '</figcaption></div><div class=\"entry__article\"><p>',
                             context)  # 有图片名的图片在正文的前面
            context = re.sub('\"><p>', '\"></div><div class=\"entry__article\"><p>', context)  # 没有图片名的图片在正文的前面
            context = re.sub('</h3><img', '</h3></div><div class=\"entry__img-holder text-center\"><img', context)  # 图片在标题的后面
            context = re.sub('</figcaption><h3', '</figcaption></div><div class=\"entry__article\"><h3',
                             context)  # 有图片名的图片在标题的前面
            ##############
            context = self.context_css+self.context_html_tmp.format(context)
            context = re.sub(
                r'(<link rel=\"stylesheet\" type=\"text/css\" href=\"css/style.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/bootstrap.css\"><link rel=\"stylesheet\" type=\"text/css\" href=\"css/font-awesome.min.css\"><article class=\"entry\"><div class=\"entry__article\"></div><div class=\"entry__article\">).*<p>[\d]+</p>',
                r'\1', context)
            # with open('/home/mininet/test.txt','w+') as f:
            #     f.write(context)
            # print context
            context = context.replace('data-src','src')
            result = [title,url, '', context, '', '', type_id, spider_time, source]
        return result

    def on_result(self, result):
        if not result:
            return
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8')
        cur = conn.cursor()
        cur.execute("select * from website where url = %s" , result[1])
        rows = cur.fetchall()
        if len(rows) == 0:
            try:
                sql = 'INSERT INTO website(title,url,push_time,context,come_from,page_type,type_id,spider_time,source) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                # 批量插入
                cur.execute(sql,result)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        else:
            result = result[::-1]
            try:
                sql = 'UPDATE website SET source=%s,spider_time=%s,type_id=%s,page_type=%s,come_from=%s,context=%s,push_time=%s,url=%s WHERE title=%s'
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