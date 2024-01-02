import scrapy

from scrapy.loader import ItemLoader
from sentiments.items import ArticleItem


class ArticlesSpider(scrapy.Spider):
    name = "articles"

    def start_requests(self):
        # yield a request for each url
        for url in self.settings.get("ARTICLES_SOURCE_URLS", "").split():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # create an item loader for article items
        loader = ItemLoader(item=ArticleItem(), response=response)

        # load the response into the item loader
        loader.add_css("identifier", "")
        loader.add_css("publisher_identifier", "")
        loader.add_css("date", "")
        loader.add_css("authors", "")
        loader.add_css("title", "")
        loader.add_css("text", "")
        loader.add_css("summary", "")
        loader.add_css("title_sentiment", "")
        loader.add_css("text_sentiment", "")
        loader.add_css("summary_sentiment", "")
        loader.add_css("keywords", "")
        loader.add_css("language", "")
        loader.add_css("city", "")
        loader.add_css("country", "")
        
        # yield the item
        yield loader.load_item()
            
