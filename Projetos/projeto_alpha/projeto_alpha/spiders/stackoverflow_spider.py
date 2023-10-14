import scrapy
class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['https://stackoverflow.com/questions/tagged/python']

    def parse(self, response):
        # get the links to the questions
        question_links = response.xpath('//a[@class="question-hyperlink"]/@href')
        yield from response.follow_all(question_links, self.parse_question)
        # get the link to the next page
        next_page_link = response.xpath('//a[@rel="next"]/@href')
        yield from response.follow_all(next_page_link)

    def parse_question(self, response):
        # get the question title and url
        question_title = response.xpath('//h1/a/text()').get()
        question_url = response.url
        # get the question body and code
        question_body = response.xpath('//div[@id="question"]//div[@class="post-text"]/p//text()')
        question_body = ''.join(question_body.getall())
        question_code = response.xpath('//div[@id="question"]//div[@class="post-text"]//pre/code/text()')
        question_code = ''.join(question_code.getall())
        # get the question votes and views
        question_votes = response.xpath('//div[@id="question"]//span[@itemprop="upvoteCount"]/text()')
        question_votes = int(question_votes.get())
        question_views = response.xpath('//div[@id="qinfo"]//p/b/text()')
        question_views = int(question_views.get().replace(',',''))
        # get the question tags
        question_tags = response.xpath('//div[@id="question"]//div[@class="post-taglist"]/a/text()')
        question_tags = ','.join(question_tags.getall())
        # get the links to the answers
        answer_links = response.xpath('//a[@name="tab-top"]/@href')
        yield from response.follow_all(answer_links, self.parse_answer,
                                       cb_kwargs={'question_title': question_title,
                                                  'question_url': question_url,
                                                  'question_body': question_body,
                                                  'question_code': question_code,
                                                  'question_votes': question_votes,
                                                  'question_views': question_views,
                                                  'question_tags': question_tags})

    def parse_answer(self, response, question_title, question_url, question_body, question_code, question_votes, question_views, question_tags):
        # get the answer body and code
        answer_body = response.xpath('//div[@id="answers"]//div[@class="post-text"]/p//text()')
        answer_body = ''.join(answer_body.getall())
        answer_code = response.xpath('//div[@id="answers"]//div[@class="post-text"]//pre/code/text()')
        answer_code = ''.join(answer_code.getall())
        # get the answer votes
        answer_votes = response.xpath('//div[@id="answers"]//span[@itemprop="upvoteCount"]/text()')
        answer_votes = int(answer_votes.get())
        # save the data as a csv row
        yield {
            'site': 'stackoverflow',
            'question_title': question_title,
            'question_url': question_url,
            'question_body': question_body,
            'question_code': question_code,
            'question_votes': question_votes,
            'question_views': question_views,
            'question_tags': question_tags,
            'answer_body': answer_body,
            'answer_code': answer_code,
            'answer_votes': answer_votes
        }