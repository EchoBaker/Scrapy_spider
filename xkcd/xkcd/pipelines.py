# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import json
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class XkcdImgPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None,):

        # print dir(request)
        image_guid = request.url.split('/')[-1]
        return 'images/%s' % (image_guid)


class HtmlPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        if re.search(r'\d', request.url):
            media_guid = re.search(r'\d', request.url).group(1)
        else:
            media_guid = '0'
        return 'web/%s.html' % (media_guid)

        #
        # def get_media_requests(self, item, info):
        #     for image_url in item['image_urls']:
        #         yield scrapy.Request(image_url)

        # def item_completed(self, results, item, info):
        #     image_paths = [x['path'] for ok, x in results if ok]
        #     if not image_paths:
        #         raise DropItem("Item contains no images")
        #     # item['image_paths'] = image_paths
        #     yield item

        # # # # # # # # # # # # # ## # # # # # # # # # # ## # # # # # # # # # # # # # #
        # #  Configure item pipelines                                                 #
        # #  See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html    #
        #   ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}            #
        #   IMAGES_STORE = 'C:/Users/Echo/Documents/GitHub/Scrapy_spider/xkcd/images' #
        #   IMAGES_EXPIRES = 90                                                       #
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
