# -*- coding: utf-8 -*-
import scrapy
from jiangsuhospital.items import JiangsuhospitalItem

class HospitalSpider(scrapy.Spider):
    name = 'hospital'
    allowed_domains = ['99.com.cn']
    start_urls = ['https://yyk.99.com.cn/jiangsu/']

    def parse(self, response):
        divs = response.xpath("//html/body//div[@class='m-table-2']//tr")


        #拼接各家医院的url      
        for div in divs:
            trs = div.xpath('.//td')
            for tr in trs:
                href = tr.xpath('.//a/@href').extract_first()
                next_url = 'https://yyk.99.com.cn'+href+'jianjie.html'

                #请求所有医院的url
                yield scrapy.Request(next_url,callback=self.parse_detail)



    def parse_detail(self,response):
        mingcheng = response.xpath("//html/body//div[@class='wrap-mn']/h1/text()").extract_first()
        bieming = response.xpath("//html/body//div[@class='wrap-hd']//p[1]/text()").extract_first()
        shuxing = response.xpath("//html/body//div[@class='wrap-hd']//p[2]/text()").extract_first()
        dianhua = response.xpath("//html/body//div[@class='wrap-hd']//p[3]/em/text()").extract_first()
        dizhi = response.xpath("//html/body//div[@class='wrap-hd']//p[4]/em/text()").extract_first()
        
        chengshi = response.xpath("//html/body//div[@class='present-cont']//tr[1]//td[4]/a/text()").extract_first()
        yuanzhang = response.xpath("//html/body//div[@class='present-cont']//tr[2]//td[2]/span/text()").extract_first()
        jianyuan = response.xpath("//html/body//div[@class='present-cont']//tr[2]//td[4]/span/text()").extract_first()
        leixing = response.xpath("//html/body//div[@class='present-cont']//tr[2]//td[6]/span/text()").extract_first()
        dengji = response.xpath("//html/body//div[@class='present-cont']//tr[3]//td[2]/span/text()").extract_first()
        keshi = response.xpath("//html/body//div[@class='present-cont']//tr[3]//td[4]/a/text()").extract_first()
        renshu = response.xpath("//html/body//div[@class='present-cont']//tr[3]//td[6]/a/text()").extract_first()
        bingchuang = response.xpath("//html/body//div[@class='present-cont']//tr[4]//td[2]/span/text()").extract_first()
        nianmenzhen = response.xpath("//html/body//div[@class='present-cont']//tr[4]//td[4]/span/text()").extract_first()
        yibao = response.xpath("//html/body//div[@class='present-cont']//tr[4]//td[6]/span/text()").extract_first()

        item =  JiangsuhospitalItem(mingcheng=mingcheng,bieming=bieming,shuxing=shuxing,dianhua=dianhua,dizhi=dizhi,chengshi=chengshi,yuanzhang=yuanzhang,jianyuan=jianyuan,leixing=leixing,dengji=dengji,keshi=keshi,renshu=renshu,bingchuang=bingchuang,nianmenzhen=nianmenzhen,yibao=yibao)

        yield item