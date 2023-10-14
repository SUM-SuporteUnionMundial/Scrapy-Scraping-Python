import scrapy


class RealpythonSpider(scrapy.Spider):

    name = "realpython"
    start_urls = ["https://realpython.com/search?kind=article&kind=course"]

    def parse(self, response):
        print("Hello World!")