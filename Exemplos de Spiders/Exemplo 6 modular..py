import scrapy
import tldextract
from scrapy.crawler import CrawlerProcess
from scrapy import signals
import cachetools
import networkx as nx
import csv
import logging
from fake_useragent import UserAgent
import json
from scrapy.utils.project import get_project_settings

def Coletar_dados():
    dados_coletados = {}
    tipos_dados = []
    search_term = input("Qual é o termo de pesquisa? ")
    sites_pesquisa = input("Digite os sites adicionais para varrer (separados por vírgula): ").split(',')
    sites_adicionais = sites_pesquisa
    seletores = int(input("Escolha um dos seletores:\n1. CSS\n2. XPATH\nEscolha o seletor desejado: "))
    metodo = int(input("Escolha um dos métodos:\n1. Completo \n2. Modo site \n3. Pesquisa\nDigite o número do método desejado: "))
    print("\nEscolha os tipos de dados que deseja coletar (digite os números separados por vírgula):")
    print("1. Títulos\n2. Texto\n3. Código\n4. Links de Download\n5. Imagens\n6. Tabelas")
    opcoes = {
        1: 'titulos',
        2: 'texto',
        3: 'codigo',
        4: 'links_download',
        5: 'imagens',
        6: 'tabelas'
    }
    opcao = input("Digite os números das opções desejadas (exemplo: 1, 3, 5): ")
    opcoes_selecionadas = [int(op.strip()) for op in opcao.split(',')]
    tipos_dados = [opcoes[op] for op in opcoes_selecionadas]

    tipo_armazenamento = int(input("\nEscolha o tipo de armazenamento:\n1. JSON\n2. CSV\nDigite o número do tipo de armazenamento desejado: "))
    nome_arquivo = input("Digite o nome do arquivo: ")
    local_armazenamento = input("Digite o local onde os arquivos serão salvos: ")

    for tipo in tipos_dados:
        if tipo == 'titulos':
            dados_coletados['titulos'] = ('h1::text, h2::text, h3::text, h4::text, h5::text, h6::text')
        elif tipo == 'texto':
            dados_coletados['texto'] = ('p::text')
        elif tipo == 'codigo':
            dados_coletados['codigo'] = ('code::text')
        elif tipo == 'links_download':
            dados_coletados['links_download'] = ('a[href$=".zip"]::attr(href)')
        elif tipo == 'imagens':
            dados_coletados['imagens'] = ('img::attr(src)')
        elif tipo == 'tabelas':
            dados_coletados['tabelas'] = ('table')

    return {
        "metodo": metodo,
        "dados_coletados": dados_coletados,
        "tipo_armazenamento": tipo_armazenamento,
        "nome_arquivo": nome_arquivo,
        "local_armazenamento": local_armazenamento,
        "search_term": search_term,
        "sites_adicionais": sites_adicionais,
        "tipos_dados": tipos_dados,
        "seletores" : seletores
    }

class MySpider(scrapy.Spider):
    name = "myspider"

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.dados_user = kwargs['dados_user']
        self.cache = cachetools.LRUCache(maxsize=1000)
        self.graph = nx.DiGraph()
        self.user_agent_generator = UserAgent()
        self.headers = self.obter_headers()
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)

    def start_requests(self):
        tarefas = self.dados_user
        metodo = tarefas["metodo"]
        self.search_term = tarefas["search_term"]
        self.sites_adicionais = tarefas["sites_adicionais"]

        if metodo == 1:
            start_urls = [f"https://www.google.com/search?q={self.search_term}"] + self.sites_adicionais
        elif metodo == 2:
            start_urls = self.sites_adicionais
        elif metodo == 3:
            start_urls = [f"https://www.google.com/search?q={self.search_term}"]

        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=self.headers)

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
        dados_coletados = {
            "url": response.url,
            "domain": domain
        }
        tipos_dados = self.dados_user["dados_coletados"]
        seletores = self.dados_user["seletores"]
        if seletores == 1:
            for tipo, selector in tipos_dados.items():
                dados_coletados[tipo] = response.css(selector).get()
        elif seletores == 2:
            for tipo, selector in tipos_dados.items():
                dados_coletados[tipo] = response.xpath(selector).get()

        yield dados_coletados
        
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

    def spider_closed(self, spider, reason):
        armazenagem_dados = self.dados_user
        self.pos_execucao_codigo(armazenagem_dados)

    def pos_execucao_codigo(self, armazenagem_dados):
        self.dados_coletados = armazenagem_dados["dados_coletados"]
        self.tipo_armazenamento = armazenagem_dados["tipo_armazenamento"]
        self.tipos_dados = armazenagem_dados["tipos_dados"]
        self.nome_arquivo = armazenagem_dados["nome_arquivo"]
        self.local_armazenamento = armazenagem_dados["local_armazenamento"]

        if self.tipo_armazenamento == 1:
            caminho_completo = f"{self.local_armazenamento}/{self.nome_arquivo}.json"
            with open(caminho_completo, 'w') as json_file:
                json.dump(self.dados_coletados, json_file, ensure_ascii=False, indent=4)
            print("Dados armazenados em formato JSON.")
        elif self.tipo_armazenamento == 2:
            caminho_completo = f"{self.local_armazenamento}/{self.nome_arquivo}.csv"
            with open(caminho_completo, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)

                cabecalho = ['url', 'domain']
                cabecalho.extend(self.tipos_dados)

                csv_writer.writerow(cabecalho)

                for dados in self.dados_coletados:
                    linha = [dados['url'], dados['domain']]
                    linha.extend(dados[tipo] if tipo in dados else "" for tipo in self.tipos_dados)
                    csv_writer.writerow(linha)

                print(f"Dados armazenados em formato CSV no caminho: {caminho_completo}")


if __name__ == '__main__':
    dados_user = Coletar_dados()
    process = CrawlerProcess(settings=get_project_settings())
    # Iniciando o spider com as configurações coletadas
    process.crawl(MySpider, dados_user=dados_user)
    # Executando o spider
    process.start()
