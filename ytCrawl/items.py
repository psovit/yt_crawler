# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YtcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    channel = scrapy.Field()
    viewCount = scrapy.Field()
    postedDate = scrapy.Field()
    description = scrapy.Field()
    imagePath = scrapy.Field()
    videoLink = scrapy.Field()
    channelLink = scrapy.Field()
    subscriberCount = scrapy.Field()
    totalLikes = scrapy.Field()
    totalDislikes = scrapy.Field()

