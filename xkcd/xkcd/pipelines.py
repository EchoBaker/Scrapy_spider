# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
from scrapy.conf import settings
from scrapy.http import Request
import psycopg2
from cStringIO import StringIO
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class XkcdPipelinee(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['link']:
            return scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def convert_image(self, image, size=None):
        buf = StringIO()
        try:
            image.save(buf, image.format)
        except Exception, ex:
            raise ImageException("Cannot process image. Error: %s" % ex)
        return image, buf

    def image_key(self, url):
        image_guid = hashlib.sha1(url).hexdigest()
        return 'full/%s.jpg' % (image_guid)
