# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class PropertiesItem(Item):
 # Primary fields
    title = Field()
    price = Field()
    delay = Field()
    image_url = Field()
