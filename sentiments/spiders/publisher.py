import scrapy
import os

from scrapy.loader import ItemLoader
from dotenv import load_dotenv

from sentiments.items import PublisherItem

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
        for publisher in response.css("div.publisher"):
            # create an item loader for publiser items
            loader = ItemLoader(item=PublisherItem(), response=publisher)

            # load the response into the item loader
            loader.add_css("identifier", "")
            loader.add_css("name", "")
            loader.add_css("description", "")
            loader.add_css("website", "")
            loader.add_css("languages", "")
            loader.add_css("city", "")
            loader.add_css("country", "")

            # yield the item
            yield loader.load_item()
