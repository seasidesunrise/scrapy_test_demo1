"""
 
:Author:  逍遥游
:Create:  2022/8/24$ 11:00$
"""

import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }


if __name__ == '__main__':
    # 测试当前spicer、+ debug
    # 或者另一种方式：scrapy crawl quotes
    from scrapy import cmdline

    name = 'author'
    cmd = 'scrapy crawl {0}'.format(name)
    cmdline.execute(cmd.split())