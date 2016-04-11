
BOT_NAME = 'diver'

SPIDER_MODULES = ['diver.spiders']
NEWSPIDER_MODULE = 'diver.spiders'
ITEM_PIPELINES = {
    'diver.pipelines.JsonWithEncodingPipeline': 300,
}
LOG_LEVEL = 'INFO'
