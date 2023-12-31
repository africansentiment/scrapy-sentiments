# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PublisherItem(scrapy.Item):
    identifier = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    website = scrapy.Field()
    languages = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
    is_in_africa = scrapy.Field()


class ArticleItem(scrapy.Item):
    identifier = scrapy.Field()
    publisher_identifier = scrapy.Field()
    date = scrapy.Field()
    authors = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    description = scrapy.Field()
    summary = scrapy.Field()
    title_sentiment = scrapy.Field()
    text_sentiment = scrapy.Field()
    summary_sentiment = scrapy.Field()
    keywords = scrapy.Field()
    tags = scrapy.Field()
    language = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
