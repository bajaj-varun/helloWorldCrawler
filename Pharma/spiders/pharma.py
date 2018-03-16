# -*- coding: utf-8 -*-
import scrapy
#from scrapy.selector import Selector

class PharmaSpider(scrapy.Spider):
    name = 'pharma'
    #allowed_domains = ['pharma']
    start_urls = [
    	'https://www.pfizer.com/news',
    ]

    def parse(self, response):
        print ("URL ", response.url) 
        
        for links in response.xpath('//a'):
            link = links.xpath('@href').extract_first()
            txt  = links.xpath('text()').extract_first()
            
            if txt is not None:
                txt = txt.encode("utf-8").strip()
                
            print('Link', link.encode("utf-8"), 'Text', txt)

            #links.xpath('//a[text()[re:test(.,"news|media|person|people|invest|science|health|partner*|research")]]').extract()
            