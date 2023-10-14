import scrapy
class PypiSpider(scrapy.Spider):
    name = 'pypi'
    start_urls = ['https://pypi.org/search/?q=python']

    def parse(self, response):
        # get the links to the packages
        package_links = response.xpath('//a[@class="package-snippet"]/@href')
        yield from response.follow_all(package_links, self.parse_package)
        # get the link to the next page
        next_page_link = response.xpath('//a[@class="button button-group__button button--small button--primary next"]/@href')
        yield from response.follow_all(next_page_link)

    def parse_package(self, response):
        # get the package name and url
        package_name = response.xpath('//h1/text()').get()
        package_url = response.url
        # get the package description and code
        package_description = response.xpath('//p[@class="package-description__summary"]/text()')
        package_description = package_description.get().strip()
        package_code = response.xpath('//div[@class="highlight"]/pre/text()')
        package_code = ''.join(package_code.getall())
        # get the package downloads and version
        package_downloads = response.xpath('//span[@class="package-header__downloads"]/text()')
        package_downloads = int(package_downloads.get().replace(',',''))
        package_version = response.xpath('//p[@class="package-header__version"]/text()')
        package_version = package_version.get().strip()
        # get the package classifiers
        package_classifiers = response.xpath('//p[@class="package-header__pip-instructions"]/text()')
        package_classifiers = ','.join(package_classifiers.getall())
        # save the data as a csv row
        yield {
            'site': 'pypi',
            'package_name': package_name,
            'package_url': package_url,
            'package_description': package_description,
            'package_code': package_code,
            'package_downloads': package_downloads,
            'package_version': package_version,
            'package_classifiers': package_classifiers
        }
