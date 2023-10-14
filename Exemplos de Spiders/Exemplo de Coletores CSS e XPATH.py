
#com seletor css
        def parse(self, response):
            domain = tldextract.extract(response.url).domain
            # Extraindo o texto da página
            text = response.css("::text").getall()
            
            # Extraindo os códigos da página
            codes = response.css("code::text").getall()
            
            # Extraindo os links da página
            links = response.css("a::attr(href)").getall()
            
            # Extraindo os links para downloads da página
            downloads = response.css("a[href*='download']::attr(href)").getall()

            yield {
                "url": response.url,
                "domain": domain,
                "content": response.css("body::text").get(),
                "text": text,
                "codes": codes,
                "links": links,
                "downloads": downloads
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


#com seletor xpath
        def parse(self, response):
            domain = tldextract.extract(response.url).domain
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
