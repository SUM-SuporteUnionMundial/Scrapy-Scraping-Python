import scrapy
class CodejamSpider(scrapy.Spider):
    name = 'codejam'
    start_urls = ['https://codingcompetitions.withgoogle.com/codejam/archive']

    def parse(self, response):
        # get the links to the years
        year_links = response.xpath('//a[contains(@href,"/codejam/archive/")]/@href')
        yield from response.follow_all(year_links, self.parse_year)

    def parse_year(self, response):
        # get the links to the rounds
        round_links = response.xpath('//a[contains(@href,"/codejam/round/")]/@href')
        yield from response.follow_all(round_links, self.parse_round)

    def parse_round(self, response):
        # get the links to the problems
        problem_links = response.xpath('//a[contains(@href,"/codejam/problem/")]/@href')
        yield from response.follow_all(problem_links, self.parse_problem)

    def parse_problem(self, response):
        # get the problem title and url
        problem_title = response.xpath('//h2/text()').get()
        problem_url = response.url
        # get the links to the solutions
        solution_links = response.xpath('//a[contains(@href,"/codejam/submissions")]/@href')
        yield from response.follow_all(solution_links, self.parse_solution,
                                       cb_kwargs={'problem_title': problem_title,
                                                  'problem_url': problem_url})

    def parse_solution(self, response, problem_title, problem_url):
        # get the solution title and url
        solution_title = response.xpath('//h2/text()').get()
        solution_url = response.url
        # get the code and language of the solution
        code = response.xpath('//pre/text()').get()
        language = response.xpath('//span[@class="language"]/text()').get()
        # check if the language is python
        if 'python' in language.lower():
            # save the data as a csv row
            yield {
                'site': 'codejam',
                'problem_title': problem_title,
                'problem_url': problem_url,
                'solution_title': solution_title,
                'solution_url': solution_url,
                'code': code,
                'language': language
            }
