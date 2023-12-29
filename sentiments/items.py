# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SentimentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PublisherItem(scrapy.Item):
    identifier = scrapy.Field()
    date = scrapy.Field()
    publisher = scrapy.Field()
    authors = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    summary = scrapy.Field()
    keywords = scrapy.Field()
    languages = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
