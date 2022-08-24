"""
 
:Author:  逍遥游
:Create:  2022/8/24$ 10:44$
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }


if __name__ == '__main__':
    # 测试当前spicer、+ debug
    # 或者另一种方式：scrapy crawl quotes
    from scrapy import cmdline

    name = 'quotes2'
    cmd = 'scrapy crawl {0}'.format(name)
    cmdline.execute(cmd.split())