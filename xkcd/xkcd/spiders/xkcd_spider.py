import scrapy


class XkcdSpider(scrapy.Spider):
    name = 'xkcd'
    allowed_domains = ["xkcd.com/"]
    start_urls = ["http://xkcd.com/"]

    def parse(self, response):
        filename = response.url.split("/")[2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
