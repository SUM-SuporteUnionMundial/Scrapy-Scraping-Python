import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class SiteSpider(scrapy.Spider):
    name = "site_spider"
    custom_settings = {
        'ROBOTSTXT_OBEY': False  # Para ignorar as restrições do robots.txt
    }

    def start_requests(self):
        sites = input("Quais são os sites que você quer varrer? (separe por vírgula) ")
        sites = sites.split(",") # Transformando a entrada em uma lista de sites
        for site in sites:
            site = site.strip() # Removendo espaços em branco
            yield scrapy.Request(site, callback=self.scrape_page, dont_filter=True)

    def scrape_page(self, response):
        # Criando um objeto Item para armazenar os dados raspados
        item = scrapy.Item()
        item['url'] = response.url # Salvando a url da página
        item['title'] = response.css('title::text').get() # Extraindo o título da página usando o seletor CSS
        item['text'] = response.css('::text').getall() # Extraindo todo o texto da página usando o seletor CSS
        item['codes'] = response.css('code::text').getall() # Extraindo todo o código de programação da página usando o seletor CSS
        item['links'] = response.css('a::attr(href)').getall() # Extraindo todos os links da página usando o seletor CSS
        
        # Retornando o item com os dados raspados
        return item


if __name__ == '__main__':
    process = CrawlerProcess(settings=get_project_settings())

    process.crawl(SiteSpider)
    process.start()
