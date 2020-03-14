# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import csv

class JiangsuhospitalPipeline(object):
    
    def open_spider(self,spider):
        store_file = os.path.dirname(__file__) + '\\result\\result.csv'
        self.file = open(store_file,'w',newline='')
        self.writer = csv.writer(self.file)


    def process_item(self, item, spider):
        if item['mingcheng'] :
            self.writer.writerow((item['mingcheng'],item['bieming'],item['shuxing'],item['dianhua'],item['dizhi'],item['chengshi'],item['yuanzhang'],item['jianyuan'],item['leixing'],item['dengji'],item['keshi'],item['renshu'],item['bingchuang'],item['nianmenzhen'],item['yibao']))
        return item 

    def close_spider(self,spider):
        self.file.close()