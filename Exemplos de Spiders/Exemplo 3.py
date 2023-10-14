import scrapy
import tldextract
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import logging
import random
import requests
from fake_useragent import UserAgent
from scrapy.utils.project import get_project_settings

class MySpider(scrapy.Spider):
    name = "myspider"
    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.user_agent_generator = UserAgent()

    def obter_tarefas(self):
        search_term = input("Qual é o termo de pesquisa? ")
        sites_pesquisa = input("Digite os sites adicionais para varrer (separados por vírgula): ").split(',')
        return search_term, sites_pesquisa

    def start_requests(self):
        search_term, sites_adicionais = self.obter_tarefas()
        start_urls = [f"https://www.google.com/search?q={search_term}"] + sites_adicionais
        for url in start_urls:
            headers = self.obter_headers()  # Obter os cabeçalhos
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

    def parse(self, response):
        domain = tldextract.extract(response.url).domain
        yield {
            "url": response.url,
            "domain": domain,
            "content": response.css("body::text").get(),  # Usar get() em vez de extract_first()
        }

        if "google.com/search" in response.url:
            for result in response.css("div.g"):
                link = result.css("a::attr(href)").get()  # Simplificar a seleção do link
                if link and link.startswith("http"):
                    headers = self.obter_headers()
                    yield scrapy.Request(link, callback=self.parse, headers=headers)
        else:
            for link in response.css("a::attr(href)").getall():  # Usar getall() para obter todos os links
                if link and link.startswith("http"):
                    headers = self.obter_headers()
                    yield scrapy.Request(link, callback=self.parse, headers=headers)

if __name__ == '__main__':
    process = CrawlerProcess(settings=get_project_settings())
    # Iniciando o spider
    process.crawl(MySpider)
    # Executando o spider
    process.start()