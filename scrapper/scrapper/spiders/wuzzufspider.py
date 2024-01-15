import scrapy


class WuzzufspiderSpider(scrapy.Spider):
    name = "wuzzufspider"
    allowed_domains = ["wuzzuf.net"]
    start_urls = ["https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=Machine%20learning",]
    """
    "https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=ai%20developer",
    "https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=computer%20vision",
    "https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=data%20science"]
    """

    def parse(self, response):
        jobs_names=response.css('h2.css-m604qf a::text').getall()
        jobs_locations= response.css('span.css-5wys0k').xpath('string()').getall()
        jobs_types=response.css('div.css-1lh32fc').xpath('string()').getall()
        company_names=response.css("a.css-17s97q8::text").getall()
        company_urls=response.css('h2.css-m604qf a')
        job_urls=response.css('a.css-o171kl ::attr(href)').getall()
        for i in range(len(jobs_names)):
            yield{
                    'name':jobs_names[i],
                    'job_location' :jobs_locations[i],
                    'job_type' : str(jobs_types[i]).split("}")[-1],
                    'company_name': company_names[i],
                    'job_url': job_urls[i],
                    'company_url': company_urls[i].attrib['href']
                }
            next_page = response.css('[rel="next"] ::attr(href)').get()
            if next_page is not None:
                next_page_url = next_page
                yield response.follow(next_page_url, callback=self.parse)