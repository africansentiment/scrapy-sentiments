from typing import Any, Optional
import scrapy

from scrapy.loader import ItemLoader
from sentiments.items import PublisherItem


class PublishersSpider(scrapy.Spider):
    name = "publishers"

    def start_requests(self):
        # yield a request for each url
        for url in self.settings.get("PUBLISHERS_TARGET_URLS", "").split():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for publisher in response.css(".publisher"):
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
