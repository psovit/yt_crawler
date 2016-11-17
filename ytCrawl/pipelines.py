# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymssql

class YtcrawlPipeline(object):
    def __init__(self):
        self.conn = pymssql.connect(host='vcomp-dev1', user='dbadmb', password='', database='PS_Tests')
        self.cursor = self.conn.cursor()
    
    def process_item(self, item, spider):
        try:
            

        except pymssql.Error, e:
            print ("error")

        return item
