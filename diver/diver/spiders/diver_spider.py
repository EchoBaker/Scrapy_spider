# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as lket
from diver.items import DoubanBookItem


class DiverSpider(CrawlSpider):

    name = "diver"
    allowed_domains = ["douban.com", "book.douban.com"]
    start_urls = ["https://book.douban.com/tag/"]  # the root url
    handle_httpstatus_list = [403]
    rules = [
        Rule(lket(allow=("/tag/$", )), follow=True),
        # follow start_urls https://book.douban.com/tag/
        Rule(lket(allow=("/tag/[^/]+/\?focus=book$", )), follow=True),
        # follow tag url: https://www.douban.com/tag/东野圭吾/?focus=book
        Rule(lket(allow=("/subject/\d+/\?from=tag$")), callback='parse_book'),
        # follow book url: https://book.douban.com/subject/10554308/?from=tag
    ]
    #

    def parse_book(self, response):

        print response.url
        self.logger.info('Hi, this is an item page! %s', response.url)
        site = response.css('#wrapper')
        item = DoubanBookItem()
        item['title'] = site.css('h1 span::text').extract()
        item['link'] = response.url
        item['content_intro'] = site.css('#link-report .intro p::text').extract()
        yield item
