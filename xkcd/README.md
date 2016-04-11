# **Spider Constructed by scrapy**
## 1. Create your Spider Project
Open bash (linux) or cmd (Windows)

```
$ active snakes # launch py2.7 env
```

Scrapy now can only work perfectly with python2.x, so we activate the env of python2.7.

```
$ scrapy startproject xkcd
```

Thus, we 've already generated a Project named xkcd, we are going to make it more powerful.

```
$ cd xkcd
```

**Note :** you must change to xkcd dir, otherwise the project can't execute.

## 2. Define your Structured Data
Edit`.\items.py` to define fields of scraped items like this.

```
import scrapy


class XkcdItem(scrapy.Item):

    # define the fields for your item here like:
    name = scrapy.Field()
    image_urls = scrapy.Field()
    desc = scrapy.Field()
    file_paths = scrapy.Field()
```

The example code define a structured data form like this:
<center>
<table>
<tr><td><b>name</b></td><td><b>owner</b></td><td><b>price</b></td>
</tr><tr><td>Coffee</td><td>John</td><td>$ 10</td></tr><tr><td>...</td><td>...</td><td>...</td></tr>
</table>
</center>

Later, we will use well-defined XkcdItem class to instantiate items with scraped data in `xkcd_spider.py`

## 3. Create your Spiders
Define the spiders' behavious to extract the data you wanted. A example to scrape all the link of images in XKCD.com

```
import os
import scrapy
from xkcd.items import XkcdItem
from scrapy.spiders import Spider
from scrapy.http import Request


class XkcdSpider(scrapy.Spider):
    name = 'xkcd'
    allowed_domains = ["xkcd.com/"]
    start_urls = ["http://xkcd.com"] + ["http://xkcd.com/%d/" % num for num in xrange(1, 4)]

    def parse(self, response):

        # Code Here to instantiate item
        item = XkcdItem()
        item['name'] = response.css('div#comic > img::attr("alt")').extract()
        item['image_urls'] = ["http:" + response.css('div#comic > img::attr("src")').extract()[0]]
        item['desc'] = response.css('div#comic > img::attr("title")').extract()

        yield item
```

Well Done! we 've had a spider to work for us for get wanted item filled with scraped data.

## 4. Customize File Pipelines to Stroe Data
* #### FilesPipeline
```
def file_path(self, request, response=None, info=None):
      if re.search(r'\d', request.url):
          media_guid = re.search(r'\d+', request.url).group()
      else:
          media_guid = '0'
      return 'web/%s.html' % (media_guid)
```
* #### ImagesPipeline
```
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class XkcdImgPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None,):
        image_guid = request.url.split('/')[-1]
        return 'images/%s' % (image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        yield item
  ```

## 5. Configure Setting of Project
:sunglasses:

`$ scrapy crawl xkcd --logfile="xkcd_log.log" -o xkcd.json -t json`

`$ scrapy crawl xkcd -a end=10`
