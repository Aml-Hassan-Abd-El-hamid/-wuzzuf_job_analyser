import scrapy


class WuzzufspiderSpider(scrapy.Spider):
    name = "wuzzufspider"
    allowed_domains = ["wuzzuf.net"]
    start_urls = ["https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=Machine%20learning"]

    def parse(self, response):
        pass
