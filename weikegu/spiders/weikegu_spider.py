# -*- coding: utf-8 -*-
import scrapy
from weikegu.items import WeikeguItem
import time
import re
from weikegu.cookie import account
from weikegu import sendwechar
from scrapy.conf import settings

class WeikeguSpiderSpider(scrapy.Spider):
    name = "weikegu_spider"
    allowed_domains = ["www.315wkg.com"]
    start_urls = (
        'http://www.315wkg.com/index.php?s=/Index/productcontent/gId/124',
        'http://www.315wkg.com/index.php?s=/Index/productcontent/gId/320',
        #'http://www.315wkg.com/index.php/Index/productcontent/gId/124',
        #'http://www.315wkg.com/index.php/Index/productcontent/gId/320',
        #'http://www.315wkg.com/index.php/Index/productcontent/gId/707',
    )
# 添加购物车 10个 http://www.315wkg.com/index.php/Index/cart/control/Index/tel/productcontent/gId/320/gNum/10

    def parse(self, response):
        # time.sleep(10)
        surplus = response.xpath('/html/body/div[3]/div[1]/span/text()')[0].extract()
        # print('==========>', surplus)
        pattern = re.compile(r'[-]{0,1}\d+')

        r = re.findall(pattern, surplus)
        # print(response.url())
        print(int(r[0])>0)
        if r[0] > '0':
            articlenum = str(response.url).split('/')[-1]
            print('!!!!have cards!!!! ', articlenum)
            u = 'http://www.315wkg.com/index.php/Index/cart/control/Index/tel/productcontent/gId/{}/gNum/{}'.format(articlenum, settings['SHOPPING_NUM'])

            mailcontext = '共有物品数量:{}\n物品连接: {}\n'.format(r[0], response.url)

            sendmail = sendwechar.Mail()
            sendmail.send_text('微客谷有卡了 {}'.format(articlenum), mailcontext)
            # sendmail.sendm(mailcontext)
            # yield scrapy.Request(u, callback=self.addcart)
        else:
            print('!!!!None!!!!')
    #
    # def addcart(self,response):
    #     print("账号", account, '添加购物车成功')
