# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VintedItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    is_visible = scrapy.Field()
    discount = scrapy.Field()
    currency = scrapy.Field()
    brand_title = scrapy.Field()
    is_for_swap = scrapy.Field()
    user = scrapy.Field()
    url = scrapy.Field()
    promoted = scrapy.Field()
    photo = scrapy.Field()
    favourite_count = scrapy.Field()
    is_favourite = scrapy.Field()
    badge = scrapy.Field()
    conversion = scrapy.Field()
    service_fee = scrapy.Field()
    total_item_price = scrapy.Field()
    total_item_price_rounded = scrapy.Field()
    view_count = scrapy.Field()
    size_title = scrapy.Field()
    content_source = scrapy.Field()
    status = scrapy.Field()
    icon_badges = scrapy.Field()
    search_tracking_params = scrapy.Field()
