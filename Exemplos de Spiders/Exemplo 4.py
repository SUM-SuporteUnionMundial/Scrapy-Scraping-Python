# Importando as bibliotecas necessárias
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Definindo a classe do spider
class DataSpider(scrapy.Spider):
    # Nomeando o spider
    name = "data_spider"
    # Definindo os domínios permitidos
    allowed_domains = ["gharchive.org", "codingcompetitions.withgoogle.com", "stackoverflow.com", "pypi.org", "cran.r-project.org", "npmjs.com"]
    # Definindo as URLs iniciais
    start_urls = ["https://www.gharchive.org/", "https://codingcompetitions.withgoogle.com/codejam", "https://stackoverflow.com/", "https://pypi.org/", "https://cran.r-project.org/", "https://www.npmjs.com/"]

    # Definindo o método de parseamento
    def parse(self, response):
        # Extraindo o texto da página
        text = response.xpath("//text()").getall()
        # Extraindo os códigos da página
        codes = response.xpath("//code/text()").getall()
        # Extraindo os links da página
        links = response.xpath("//a/@href").getall()
        # Extraindo os links para downloads da página
        downloads = response.xpath("//a[contains(@href, 'download')]/@href").getall()
        # Retornando os dados raspados como um dicionário
        yield {
            "url": response.url,
            "text": text,
            "codes": codes,
            "links": links,
            "downloads": downloads
        }
        # Seguindo os links da página para raspar mais dados
        for link in links:
            # Verificando se o link é absoluto ou relativo
            if link.startswith("http"):
                # Seguindo o link absoluto
                yield scrapy.Request(url=link, callback=self.parse)
            else:
                # Seguindo o link relativo
                yield response.follow(url=link, callback=self.parse)

# Criando um objeto da classe CrawlerProcess com as configurações predefinidas
process = CrawlerProcess(settings=get_project_settings())
# Iniciando o spider
process.crawl(DataSpider)
# Executando o spider
process.start()