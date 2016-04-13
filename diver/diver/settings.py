
BOT_NAME = 'diver'

SPIDER_MODULES = ['diver.spiders']
NEWSPIDER_MODULE = 'diver.spiders'
ITEM_PIPELINES = {
    'diver.pipelines.JsonWithEncodingPipeline': 1
}
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'diver.rotate_useragent.RotateUserAgentMiddleware': 403
# }
