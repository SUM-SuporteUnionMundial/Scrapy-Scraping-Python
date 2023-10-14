from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from projeto_alpha.spiders.stackoverflow_spider import StackoverflowSpider
from projeto_alpha.spiders.codejam_spider import CodejamSpider
from projeto_alpha.spiders.pypi_spider import PypiSpider
from projeto_alpha.spiders.realpython_spider import RealpythonSpider

# Adicione outras spiders aqui conforme necessário

def run_spiders():
    process = CrawlerProcess(get_project_settings())
    process.crawl(StackoverflowSpider)
    process.crawl(CodejamSpider)
    process.crawl(PypiSpider)
    process.crawl(RealpythonSpider)
    process.start()

if __name__ == "__main__":
    run_spiders()
