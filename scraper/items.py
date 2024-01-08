# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    site = scrapy.Field()
    id = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    title = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    condition = scrapy.Field()
    in_stock = scrapy.Field()
