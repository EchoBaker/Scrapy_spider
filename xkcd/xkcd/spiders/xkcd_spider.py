#-*-utf-8-*-
import os
import scrapy
import requests
from xkcd.items import XkcdItem
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request, Response
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class XkcdSpider(scrapy.Spider):
    name = 'xkcd'
    allowed_domains = ["xkcd.com/"]
    # start_urls = ["http://xkcd.com"]
    # rules = (
    #     Rule(LxmlLinkExtractor(allow))
    # )
    start_urls = ["http://xkcd.com/%d/" % num for num in xrange(1, 30)]

    def parse(self, response):

        item = XkcdItem()
        item['name'] = response.css('div#comic > img::attr("alt")').extract()
        item['image_urls'] = ["http:" + response.css('div#comic > img::attr("src")').extract()[0]]
        item['desc'] = response.css('div#comic > img::attr("title")').extract()

        yield item

    def product_detail_page(self, response):
        # hxs=HtmlXpathSelector(response)
        item = response.request.meta['item']
        # add all images url's in item['image_urls']
        yield item
