import scrapy


class WuzzufspiderSpider(scrapy.Spider):
    name = "wuzzufspider"
    allowed_domains = ["wuzzuf.net"]
    start_urls = ["https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=Machine%20learning"]

    def parse(self, response):
        jobs_names=response.css('h2.css-m604qf a::text').getall()
        jobs_locations= response.css('span.css-5wys0k').xpath('string()').getall()
        jobs_types=response.css('div.css-1lh32fc').xpath('string()').getall()
        for i in range(len(jobs_names)):
            yield{
                    'name':jobs_names[i],
                    'job_location' :jobs_locations[i],
                    'job_type' : str(jobs_types[i]).split("}")[-1],
                }
