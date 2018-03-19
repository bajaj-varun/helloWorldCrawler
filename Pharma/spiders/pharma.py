# -*- coding: utf-8 -*-
import scrapy
import re

# from scrapy.selector import Selector

class PharmaSpider(scrapy.Spider):
    name = 'pharma'
    # allowed_domains = ['pharma']
    start_urls = [
        'https://www.pfizer.com/news',
    ]

    aList = []
    mList = []
    KW = r"news|media|person|people|invest|science|health|partner*|research"

    def parse(self, response):
        print("URL %s" %response.url)

        for links in response.xpath('//a'):
            link = links.xpath('@href').extract_first()
            txt = links.xpath('text()').extract_first()

            if txt is not None:
                txt = txt.encode("utf-8").strip()

            lnk = link.encode("utf-8")
            # Print all the links
            print('Link', lnk, 'Text', txt)
            self.aList.append(lnk)

            if self.isKWExist(lnk):
                self.mList.append(lnk)

        print("Total number of records = %d" % self.aList.__len__())
        print("Total matching records = %d" % self.mList.__len__())

    def isKWExist(self, seed):
        return re.search(self.KW, seed, flags=re.IGNORECASE)