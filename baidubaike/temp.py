#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-12-22 08:43:22
# Project: test

from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        import pymysql
        river_list = ['长江流域','太湖流域','鄱阳湖水系','球川溪','大桥溪','古溪','苏庄溪','京杭运河','杭州塘','内排港','沿山河','莲花港','禾丰港','亭趾港','京杭运河二通道','泥北港','苏州塘','北郊河','东环河','南郊河','余杭塘河','中泰溪','上埠河','西塘河','三墩港','七贤桥港','良渚港','九曲港','东塘港','十字港','德博港','横塘港','含山塘','三环洞桥港','慕仁桥港','白马塘','金牛塘','北永兴港','新塍塘','分乡港','新塍北支','太浦河','大坝水路','斜路水道','芦墟塘','坟墩港','丁栅港','西溪','西苕溪','晓墅分支','南溪','大溪','浒溪','递溪','浑泥港','晓墅港','和平港','南苕溪','东苕溪','导流港','龙溪','环城河','旄儿港','机坊港','长兜港','余英溪','东塘港','茅山港','龙山港','洛州河','中苕溪','北苕溪','湘溪','埭溪','观音港','夹浦港','双港','沉渎港','合溪新港','合溪','长兴港','姚家桥港','长兴港（小浦～画溪桥）','张王塘港','杨家浦港','胥仓桥港','吕山港','南横港','泗安塘','大钱港','老龙溪','漾溪港','练市塘','双林塘','頔塘','南横塘','北横塘','罗溇','幻溇','濮溇','汤溇','白米塘','吴溇','薛塘','阳安塘','盐官下河','崇长港','长山河','新板桥港','南日港','南永兴港','毛竹港','绵长港','长水塘','洛塘河','庆长港','麻泾桥港','辛江塘','海盐塘','濮庙塘','余风港','孔庙港','日月港','大横港','莲花桥港','濮院港','百步亭港','白杨河','吕塚塘','里洪塘','酱园港','武通港','盐平塘','牛桥港','俞汇塘','大寨河','红旗塘','新农港','鳗鲤港','铁店港','茜泾塘','三店塘','伍子塘','嘉善塘','枫泾','上海塘','中心河','白水塘','步善塘','嘉平申河','广陈塘','丰收河','盐船河','放港河','黄姑塘','平湖塘','南市河','东市河','乍浦塘','新港河','上塘河','备塘河','白石港','和睦港','新塘河','新建河','浙、闽、台诸河','钱塘江水系','齐溪','何田溪','村头溪','马金溪','中村溪','池淮溪','长虹溪','张湾溪','龙山溪','常山港','马尫溪','龙绕溪','南门溪','虹桥溪','芳村溪','衢江','江山港','峡口溪','定村溪','周村溪','广渡溪','长台溪','石达河溪','大头源','乌溪江','住溪','碧龙溪','关川','湖山源','周公源','洋溪源','邵源溪','铜山源','上山溪','下山溪','芝溪','塔石溪','灵山港','桃溪','官溪','模环溪','罗家溪','社阳溪','莘畈溪','厚大溪','游埠溪','赤溪','兰江','金华江','东阳江','北江','西溪','八达溪','白溪','南江','文溪','柽溪','吴溪','航慈溪','孝顺溪','芗溪','武义江','永康江','南溪','杨溪','华溪','酥溪','熟溪','麻阳溪','乌溪','小白溪','白鹭溪','八仙溪','梅溪','白沙溪','马达溪','甘溪','梅溪','大溪','富春江','新安江','七都源','云源港','梓桐源','东源港','秋源','瑶山溪','郁川','武强溪','樟村溪','凤林港','铜山溪','白马溪','商家源','清平源','寿昌江','莲花溪','长宁溪','后源溪','胥溪','芦茨溪','清渚港','分水江','昌化溪','昌北溪','昌西溪','顺溪','蒲溪','昌南溪','天目溪','东关溪','丰陵溪','藻溪','太阳溪','后溪','前溪','罗溪','大源溪','渌渚江','葛溪','松溪','壶源江','龙门溪','上里溪','青云浦','新桥江','大源溪','浦阳江','东江','蜈蚣溪','义乌溪','王沙溪','大陈江','楂林溪','开化江','陈蔡江','璜山江','小东溪','高湖南渠','五泄江','枫桥江','栎江','枫江','店口溪','凰桐江','永兴河','钱塘江','沿山浦','小砾山输水河','新浦河','永久河','北塘河','后解放河','利民河','前解放河','五堡直河','先锋河','长山直河','大治河','四工段直河','六工段直河','八工段直河','盛陵湾','梅林湾','十工段直河','沿塘抢险河','十八工段河','十七工段河','廿二工段河','义南横河','三官埠直湾','白洋川','曹娥江','澄潭江','夹溪','左纡江','小乌溪','新昌江','长乐江','西溪','南溪','剡源','石璜江','崇仁江','黄泽江','结溪','合溪','上东江','嵊溪','隐潭溪','下管溪','范洋江','小舜江','南溪','北溪','萧曹运河','杭甬运河','石泄江','东关西直江','楝树下闸江','马山大河','富盛江','马山闸西闸江','东小江','平水江','外官塘','狭犭茶湖直江','南池江','坡塘江','娄宫江','漓渚江','项里江','瓜渚湖直江','青墩江','大坂湖直江','夏履江','南运河','进化溪','西小江','峙山河','南门江','史家桥河','红旗闸江','瓯江水系','梅溪','龙泉溪','八都溪','桑溪','均溪','锦溪','岩樟溪','大贵溪','白雁溪','道太溪','安仁溪','大石溪','浮云溪','泉溪','松阴溪','成屏溪','高碧溪','濂溪','十二都源','梧桐源','十三都源','庄门源','六都源','东坞源','四都源','竹溪源','小港','玉岩溪','安民溪','雅溪','靖居源','大溪','高溪','宣平溪','东溪','西溪','小溪','小安溪','南溪','好溪','冷水溪','盘溪','贞溪','方溪','官庄源','祯埠溪','海溪','雄溪','船寮溪','瓯江','小溪','毛垟溪','南阳溪','左溪','叶桥溪','英川溪','标溪','际坑源','上标溪','梧桐源','大赤坑','鹤溪','炉西坑','大顺源','小顺源','小吾坑','阜口源','张口坑','大奕坑','四都港','贵岙源','菇溪','西溪','戌浦江','仙门河','瞿溪','楠溪江','大源溪','岩坦溪','张溪','东皋溪','五尺溪','花坦溪','小楠溪','石染溪','黄坦溪','陡门溪','鹅浦溪','中塘溪','下塘溪','罗溪','温瑞塘河','永强塘河','乌牛溪','柳市塘河','浙东、闽东及台湾沿海诸河水系','甬江','鄞东中塘河','鄞东后塘河','江北大河','甬新河','东大河','小浃江','奉化江','晦溪','剡江','康岭溪','县江','东江','鄞江','大皎溪','小皎溪','鄞西南塘河','鄞西新塘河','鄞东前塘河','姚江','四明江','通明江','西江闸干河','百崧河','西横河','西港','中港','东港','龙坑溪','陆埠溪','慈江','大隐溪','鄞西后塘河','鄞西中塘河','盖北河','临海浦','陶家路江','建塘江','三八江','陆中湾','四灶浦','水云浦','半掘浦','徐家浦','高背浦','淞浦','淡水泓','镇龙浦','八塘横江','三塘横江','大古塘','澥浦','椒江','金坑','永安溪','麻车坑','雅溪','四都坑','郑桥溪','六都坑','九都坑','十三都坑','十都坑','十八都坑','北岙坑','二十都坑','盂溪','朱溪','双港溪','方溪','灵江','始丰溪','茶山溪','雷马溪','黄水溪','西坑','乌岩溪','王里溪','崔岙溪','三茅溪','小清溪','螺溪','苍山溪','大田港','义成港','永宁江','西江','龙溪','飞云江','三插溪','里光溪','洪口溪','莒江溪','峃作口溪','泗溪','玉泉溪','高楼溪','曹村港','金潮港','林溪','桐溪','瑞平塘河','中塘河','鳌江','顺溪','岳溪','北港','怀溪','凤卧溪','鹤溪','沪山内河','萧江塘河','梅溪','南港','藻溪','江南塘河','鳌江塘河','岩河','芦江','大嵩江','梅溪','凫溪','白溪','大溪','清溪','珠游溪','亭旁溪','健跳溪','金清港','江厦大港','南官河','永宁河','海门河','东官河','月河','葭芷泾','木城河','箬松大河','三才泾','二条河','三条河','五弯河','洞港','桃渚港','大荆溪','双峰溪','清江','淡溪','银溪','泰顺氡泉、彭溪','寿泰溪','仕阳溪','龙溪','八炉溪']

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='repository', passwd='repository', db='repository',charset='utf8mb4')
        cur = conn.cursor()
        try:
            sql = 'REPLACE INTO river values(%s)'
            cur.executemany(sql, river_list)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()



    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
