import scrapy


class RealpythonSpider(scrapy.Spider):
    name = "realpython"
    allowed_domains = ["realpython.com"]
    start_urls = ["https://realpython.com/search?kind=article&kind=course&order=newest"]

    def parse(self, response):
        print("Hello World, i Work Baby")
