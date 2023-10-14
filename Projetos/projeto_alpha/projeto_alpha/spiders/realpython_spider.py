import scrapy
class RealpythonSpider(scrapy.Spider):
    name = 'realpython'
    start_urls = ['https://realpython.com/tutorials/python/']

    def parse(self, response):
        # get the links to the tutorials
        tutorial_links = response.xpath('//a[@class="card-link"]/@href')
        yield from response.follow_all(tutorial_links, self.parse_tutorial)
        # get the link to the next page
        next_page_link = response.xpath('//a[@class="pagination-next"]/@href')
        yield from response.follow_all(next_page_link)

    def parse_tutorial(self, response):
        # get the tutorial title and url
        tutorial_title = response.xpath('//h1/text()').get()
        tutorial_url = response.url
        # get the tutorial summary and code
        tutorial_summary = response.xpath('//div[@class="article__summary"]/p/text()')
        tutorial_summary = tutorial_summary.get().strip()
        tutorial_code = response.xpath('//div[@class="article__content"]//pre/code/text()')
        tutorial_code = ''.join(tutorial_code.getall())
        # get the tutorial level and category
        tutorial_level = response.xpath('//span[@class="badge badge--level"]/text()')
        tutorial_level = tutorial_level.get().strip()
        tutorial_category = response.xpath('//span[@class="badge badge--category"]/text()')
        tutorial_category = tutorial_category.get().strip()
        # save the data as a csv row
        yield {
            'site': 'realpython',
            'tutorial_title': tutorial_title,
            'tutorial_url': tutorial_url,
            'tutorial_summary': tutorial_summary,
            'tutorial_code': tutorial_code,
            'tutorial_level': tutorial_level,
            'tutorial_category': tutorial_category
        }
