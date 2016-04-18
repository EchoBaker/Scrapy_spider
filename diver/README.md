# __Recursively Scrape Web Pages With Scrapy__
## 1. Create a Project
Open your terminal and create a Scrapy project by navigating to the directory you'd like to store your project in and then running the following command:

`$ scrapy startproject diver`

`$ cd diver`

### 1.1 Item Class:
 Open the `items.py` file within the "diver" directory. Edit the file to define the fields that you want contained within the Item. Since we want the post title and subsequent URL, the Item class looks like this:

```
from scrapy.item import Item, Field

class CraigslistSampleItem(Item):
    title = Field()
    link = Field()
```

### 1.2 The Spider:
## **CrawlSpider**
Last time, we created a new Scrapy project, updated the Item Class, and then wrote the spider to pull jobs from a single page. This time, we just need to do some basic changes to add the ability to _follow links_ and scrape more than one page. The first change is that this spider will inherit from **CrawlSpider** and not **BaseSpider**.
