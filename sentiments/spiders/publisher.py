import scrapy
import os

from scrapy.loader import ItemLoader
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# get the target domain and url from environment variables
target_domains = os.getenv("TARGET_DOMAINS").split(" ")
target_urls = os.getenv("TARGET_URLS").split(" ")


class PublisherSpider(scrapy.Spider):
    name = "publisher"
    allowed_domains = target_domains

    def start_requests(self):
        # yield a request for each url
        for url in target_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # create an item loader for publiser items

        # load the response into the item loader
        # yield the item

        pass
