# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ProjetoAlphaPipeline:
    def process_item(self, item, spider):
        return item
import csv
import csv

class CsvPipeline(object):
    def __init__(self):
        # abrir o arquivo csv para escrita
        self.file = open('dados.csv', 'w', newline='', encoding='utf-8')
        # criar um objeto writer para escrever as linhas
        self.writer = csv.writer(self.file)
        # escrever a linha com os nomes das colunas
        self.writer.writerow(['site', 'package_name', 'package_url', 'package_description', 'package_code', 'package_downloads', 'package_version', 'package_classifiers',
                              'tutorial_title', 'tutorial_url', 'tutorial_summary', 'tutorial_code', 'tutorial_level', 'tutorial_category'])

    def process_item(self, item, spider):
        # escrever a linha com os dados do item
        self.writer.writerow([item['site'], item.get('package_name'), item.get('package_url'), item.get('package_description'), item.get('package_code'), item.get('package_downloads'), item.get('package_version'), item.get('package_classifiers'),
                              item.get('tutorial_title'), item.get('tutorial_url'), item.get('tutorial_summary'), item.get('tutorial_code'), item.get('tutorial_level'), item.get('tutorial_category')])
        # retornar o item
        return item

    def close_spider(self, spider):
        # fechar o arquivo csv
        self.file.close()
