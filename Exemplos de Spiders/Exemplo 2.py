import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.project import get_project_settings

class GoogleSpider(scrapy.Spider):
    name = "google_spider"
    custom_settings = {
        'ROBOTSTXT_OBEY': False  # Para ignorar as restrições do robots.txt
    }

    def start_requests(self):
        search_term = input("Qual é o termo de pesquisa? ")
        start_url = f"https://www.google.com/search?q={search_term}"
        yield scrapy.Request(start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        link_extractor = LinkExtractor(restrict_css="div.g")
        links = link_extractor.extract_links(response)
        
        for index, link in enumerate(links[:10]):
            url = response.urljoin(link.url) # Usa o método urljoin
            yield {"rank": index + 1, "url": url}
            yield scrapy.Request(url, callback=self.scrape_page) # Inicia o processo de scrapy
            
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

    process.crawl(GoogleSpider)
    process.start()
