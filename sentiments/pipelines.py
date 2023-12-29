# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import os

from itemadapter import ItemAdapter
from dotenv import load_dotenv


class SentimentsPipeline:
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    collection_name = "scrapy_items"  # Collection name

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(os.getenv("MONGO_URI"))

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collections = {
            "publisher": "publishers",
            "article": "articles",
        }
        self.db[collections[spider.name]].insert_one(dict(item))
        return item
