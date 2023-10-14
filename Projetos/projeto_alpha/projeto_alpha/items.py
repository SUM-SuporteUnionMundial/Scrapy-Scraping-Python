# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjetoAphaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PackageItem(scrapy.Item):
    # definir os campos para o item de pacote
    site = scrapy.Field()
    package_name = scrapy.Field()
    package_url = scrapy.Field()
    package_description = scrapy.Field()
    package_code = scrapy.Field()
    package_downloads = scrapy.Field()
    package_version = scrapy.Field()
    package_classifiers = scrapy.Field()

class TutorialItem(scrapy.Item):
    # definir os campos para o item de tutorial
    site = scrapy.Field()
    tutorial_title = scrapy.Field()
    tutorial_url = scrapy.Field()
    tutorial_summary = scrapy.Field()
    tutorial_code = scrapy.Field()
    tutorial_level = scrapy.Field()
    tutorial_category = scrapy.Field()
