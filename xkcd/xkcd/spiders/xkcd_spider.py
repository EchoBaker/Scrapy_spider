
import scrapy
from xkcd.items import XkcdItem  # XkcdItem class in xkcd/xkcd/items.py
from scrapy.spiders import Spider  # the most basic Spider class
from scrapy.http import Request  # Requset class to get Request object of a URL
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


class XkcdSpider(scrapy.Spider):
    name = 'xkcd'
    allowed_domains = ["xkcd.com/"]  # only urls in this domains can be requested

    def __init__(self, end=6, *args, **kwargs):
        super(XkcdSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["http://xkcd.com"] + ["http://xkcd.com/%s/" % num for num in xrange(1, int(end))]

    def parse(self, response):  # the method utilized to parse the response of an url requset

        # Code Here to instantiate item
        item = XkcdItem()
        item['name'] = response.css('div#comic > img::attr("alt")').extract()
        item['file_urls'] = [response.url]
        # alt attribute of img tags
        item['image_urls'] = ["http:" + response.css('div#comic > img::attr("src")').extract()[0]]
        # src(url) attribute of the img tags
        item['desc'] = response.css('div#comic > img::attr("title")').extract()
        # description of images

        yield item
        # indispensable sentence to yield (less memory used) or return item object to pipelines
