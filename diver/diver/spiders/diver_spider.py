# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from diver.items import DoubanSubjectItem


class DiverSpider(CrawlSpider):

    name = "diver"
    allowed_domains = ["douban.com"]
    start_urls = ["http://book.douban.com/tag/"]  # the root url
    rules = [
        Rule(LinkExtractor(allow=("/tag/[^/]+/\?focus=book$")), follow=True),
        # 第一步：跟踪文学分类标签，到书目页面 example url: https://www.douban.com/tag/东野圭吾/?focus=book
        Rule(LinkExtractor(allow=("/tag/$")), follow=True),
        #
        Rule(LinkExtractor(allow=("/subject/\d+/\?from=tag$")), callback='parse_book'),
        # 第二步：跟踪书单页面，到单个书本的页面 example url: https://book.douban.com/subject/10554308/?from=tag
    ]

    def parse_book(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        sel = Selector(response)
        site = sel.css('#wrapper')
        item = DoubanSubjectItem()
        item['title'] = site.css('h1 span::text').extract()
        item['link'] = response.url
        item['content_intro'] = site.css('#link-report .intro p::text').extract()
        print response.url
        return item
