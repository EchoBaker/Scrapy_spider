BOT_NAME = 'xkcd'

SPIDER_MODULES = ['xkcd.spiders']
NEWSPIDER_MODULE = 'xkcd.spiders'


ITEM_PIPELINES = {'xkcd.pipelines.XkcdImgPipeline': 1, 'xkcd.pipelines.HtmlPipeline': 2,
                  'xkcd.pipelines.JsonWriterPipeline': 3, }
IMAGES_STORE = 'C:/Users/Echo/Documents/GitHub/Scrapy_spider/xkcd/downloaded'
FILES_STORE = 'C:/Users/Echo/Documents/GitHub/Scrapy_spider/xkcd/downloaded'
