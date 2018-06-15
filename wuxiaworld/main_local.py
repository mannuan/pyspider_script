# -*- coding:utf-8 -*-

from pymongo import MongoClient
import json,sys
reload(sys)
sys.setdefaultencoding('utf8')

conn = MongoClient('localhost', 27017)
db = conn.wuxiaworld  # 连接wuxiaworld数据库，没有则自动创建
novels = db.novels  # 使用novels集合,没有则自动创建
#寻找有几本小说
novels_title_set = set()
for novel in novels.find():
    novels_title_set.add(novel.get('novel_title'))
#寻找每一本小说里面有几个部分
for novel_title in novels_title_set:
    f = open('/home/mininet/文档/武侠世界小说/{}.txt'.format(novel_title),'w+')
    print '标题 : '+novel_title
    chapter_count = 0
    parts_num_set = set()
    for part in novels.find({'novel_title':novel_title}):
        parts_num_set.add(part.get('part_num'))
    parts_num_list = list(parts_num_set)
    parts_num_list.sort()
    #寻找每一个部分里面有多少章节
    for part_num in parts_num_list:
        part_title = list(novels.find({'novel_title': novel_title, 'part_num': part_num}))[0].get('part_title')
        f.write('第{}部分\n{}\n'.format(part_num,part_title))
        print '第{}部分 : {}'.format(part_num,part_title)
        texts_chapter_list = list()
        for text in novels.find({'novel_title':novel_title,'part_title':part_title}):
            texts_chapter_list.append(text.get('text_chapter'))
        texts_chapter_list.sort()
        for text_chapter in texts_chapter_list:
            text = novels.find({'novel_title': novel_title, 'part_title': part_title, 'text_chapter':text_chapter})[0]
            text_title = text.get('text_title')
            text_text = text.get('text')
            chapter_count += 1
            f.write('第{}章\n{}\n'.format(chapter_count,text_title))
            print '第{}章 : {}'.format(chapter_count,text_title)
            f.write(text_text+'\n\n')