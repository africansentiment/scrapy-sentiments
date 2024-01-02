# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class SentimentsPipeline:
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):
    collection_name = "scrapy_items"

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB"),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

        # Ensure a unique index on the 'unique_field'
        self.db[spider.name].create_index("identifier", unique=True)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.db[spider.name].insert_one(dict(item))
        except DuplicateKeyError:
            spider.logger.debug(f"Duplicate item found: {item['identifier']}")

        return item
