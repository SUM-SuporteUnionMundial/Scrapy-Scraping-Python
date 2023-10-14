import scrapy
import tldextract
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from fake_useragent import UserAgent
from scrapy.utils.project import get_project_settings
import logging
logging.getLogger('tldextract').setLevel(logging.ERROR)

class MySpider(scrapy.Spider):
    name = "myspider"
    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.user_agent_generator = UserAgent()
        self.items = []

    def start_requests(self):
        search_term = input("Qual é o termo de pesquisa? ")
        sites_adicionais = input("Digite os sites adicionais para varrer (separados por vírgula): ").split(',')
        start_urls = [f"https://www.google.com/search?q={search_term}"] + sites_adicionais
        for url in start_urls:
            headers = self.obter_headers()
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def obter_headers(self):
        user_agent = self.user_agent_generator.random
        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        return headers

    def collect_items(self, item, response, spider):
        self.items.append(item)
        return item

    def parse(self, response):
        domain = tldextract.extract(response.url).domain
        item = {
            "url": response.url,
            "domain": domain,
            "content": response.css("body::text").get(),
        }
        yield self.collect_items(item, response, spider)

    # Definir as regras de rastreamento
    rules = (
        # Seguir os links dos resultados do Google e usar o método parse_google
        Rule(LinkExtractor(restrict_css="div.g"), callback="parse_google", follow=True),
        # Seguir os links dos outros sites e usar o método parse_site
        Rule(LinkExtractor(), callback="parse_site", follow=True),
    )

    def parse_google(self, response):
        # Usar o método urljoin para construir os links absolutos
        link = response.urljoin(response.css("a::attr(href)").get())
        headers = self.obter_headers()
        yield scrapy.Request(link, callback=self.parse, headers=headers)

    def parse_site(self, response):
        domain = tldextract.extract(response.url).domain
        # Usar uma condição para filtrar os links que pertencem ao mesmo domínio
        if domain in response.url:
            headers = self.obter_headers()
            yield scrapy.Request(response.url, callback=self.parse, headers=headers)

if __name__ == '__main__':
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(MySpider)
    process.start()
