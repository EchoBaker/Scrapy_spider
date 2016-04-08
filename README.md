# **Spider Constructed by scrapy**
## 1. Create your Spider Project
Open bash (linux) or cmd (Windows)

```
$ active snakes # launch py2.7 env
$ scrapy startproject boom
$ cd boom
```

## 2. Create your Structured DataEdit
`.\items.py` to define fields of scraped items like this.

```
from scrapy import Item, Field
class BoomItem(Item):    
# define the fields for your item here like:    
  name = Field()    
  owner = Field()    
  price = Field()
```

The example code make a structured data form like this:
<center><table><tr><td>**name**</td><td>**owner**</td><td>**price**</td></tr><tr><td>Coffee</td><td>John</td><td>$ 10</td></tr><tr><td>...</td><td>...</td><td>...</td></tr></table></center>

## 3. Create your Spiders
Define the spiders' behavious to extract the data you wanted."
