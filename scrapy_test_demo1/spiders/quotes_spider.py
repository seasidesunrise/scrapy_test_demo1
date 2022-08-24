"""
 
:Author:  逍遥游
:Create:  2022/8/24$ 10:44$
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


if __name__ == '__main__':
    # 测试当前spicer、+ debug
    # 或者另一种方式：scrapy crawl quotes
    from scrapy import cmdline

    name = 'quotes'
    cmd = 'scrapy crawl {0}'.format(name)
    cmdline.execute(cmd.split())