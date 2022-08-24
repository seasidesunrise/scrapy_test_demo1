"""
 
:Author:  逍遥游
:Create:  2022/8/24$ 10:44$
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes4"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


if __name__ == '__main__':
    # 测试当前spicer、+ debug
    # 或者另一种方式：scrapy crawl quotes
    from scrapy import cmdline

    name = 'quotes4'
    cmd = 'scrapy crawl {0}'.format(name)
    cmdline.execute(cmd.split())