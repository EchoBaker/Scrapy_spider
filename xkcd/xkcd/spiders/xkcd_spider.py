import scrapy
import os
import requests
from xkcd.items import XkcdItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request, Response


class XkcdSpider(scrapy.Spider, Request, Response):
    name = 'xkcd'
    allowed_domains = ["xkcd.com/"]
    # start_urls = ["http://xkcd.com"]
    # rules = (
    #     Rule(LxmlLinkExtractor(allow))
    # )
    start_urls = ["http://xkcd.com/%d/" % num for num in xrange(1, 30)]

    def parse(self, response):
        # filename = response.url.split("/")[3] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # for href in response.css("ul.comicNav > li > a[rel='prev']::attr('href')"):
        name = response.css('div#comic > img::attr("alt")').extract()
        link = response.css('div#comic > img::attr("src")').extract()
        desc = response.css('div#comic > img::attr("title")').extract()

        item = XkcdItem()
        item['name'] = response.css('div#comic > img::attr("alt")').extract()
        item['link'] = ["http:" + response.css('div#comic > img::attr("src")').extract()[0]]
        item['desc'] = response.css('div#comic > img::attr("title")').extract()
        # print item['link'][0]
        # res = requests.get(item['link'])
        # imageFile = open(os.path.join('.\\images', item['name'][0] + '.jpg'), 'wb')
        # for chunk in res.iter_content(100000):
        #     imageFile.write(chunk)
        # # imageFile.close()
        print item['link']
        yield Request(item['link'][0],
                      meta={'item': item},
                      callback=self.product_detail_page)

    def product_detail_page(self, response):
        # hxs=HtmlXpathSelector(response)
        item = response.request.meta['item']
        # add all images url's in item['image_urls']
        yield item

        # yield item
        # f = open('item.json', 'ab')
        # # print(item['name'][0])
        # line = ",".join([i[0]for i in item.values()])
        # f.write(line)
        # t = Request(url, callback=self.parse_extract_item)
        # print t  # yield Response(url, callback=self.parse)
