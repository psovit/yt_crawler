import scrapy
import re
from ytCrawl.items import YtcrawlItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class yTSpider(scrapy.Spider):
    name = "yTSpider"
    allowed_domains = ["youtube.com"]
    
    start_urls = [
        "https://www.youtube.com/results?search_query=c%23"
    ]
    
    def __init__(self, query=None, *args, **kwargs):
        super(yTSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.youtube.com/results?search_query=%s' % query]

    def parse(self, response):
        for sel in response.xpath('//div[@class="yt-lockup-dismissable yt-uix-tile"]'):
            viewMeta = sel.css('ul.yt-lockup-meta-info li::text').extract()
            # get videos only and not the playlists   
            if(len(viewMeta) == 2):
                # get links that have more than 100,000 views
                viewCounts = re.findall(r'\d+', viewMeta[1])
                viewCounts = ''.join(viewCounts)  
                if(int(viewCounts) > 100000):
                    videoLink = response.urljoin(sel.css('h3.yt-lockup-title  a::attr(href)').extract_first())                    
                    yield scrapy.Request(videoLink, callback=self.parse_contents)        
         
        checkNextPage = response.xpath('//span[contains(text(), "Next")]').extract_first()
        
        if(len(checkNextPage)>0):            
            nextPageLink = response.xpath('//span[contains(text(), "Next")]/ancestor::a/@href').extract_first()            
            nextPageFullUrl = response.urljoin(nextPageLink)
                                   
            yield scrapy.Request(nextPageFullUrl, self.parse)
                
            
    def parse_contents(self, response):
        item = YtcrawlItem()
        item['title'] = str(response.css("span.watch-title::text").extract_first()).replace("|","-")                  
        item['videoLink'] = response.url
        item['channel'] = str(response.css('div.yt-user-info a::text').extract_first()).replace("|","-")   
        item['channelLink'] = response.urljoin(response.css('div.yt-user-info a::attr(href)').extract_first())
        item['viewCount'] = str(response.css('div.watch-view-count::text').extract_first()).replace("|","-")   
        item['postedDate'] = str(response.css('strong.watch-time-text::text').extract_first()).replace("|","-")   
        item['description'] = str(''.join(response.xpath('//p[@id="eow-description"]/text()').extract())).replace("|","-")   
        item['imagePath'] = response.xpath('//div[@id="watch7-user-header"]/a/span/span/span/img/@data-thumb').extract_first()
        item['subscriberCount'] = str(response.css('span.yt-subscriber-count::text').extract_first()).replace("|","-")   
        item['totalLikes'] = str(response.css('span.like-button-renderer button span::text')[0].extract()).replace("|","-")   
        item['totalDislikes'] = str(response.css('span.like-button-renderer button span::text')[2].extract()).replace("|","-")   
        yield item
                
        
        
            
