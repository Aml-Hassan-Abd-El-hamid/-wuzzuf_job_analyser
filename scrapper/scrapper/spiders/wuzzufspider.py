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
    def __init__(self):
        self.o=[]
        self.jobs_names=0
        self.jobs_locations=0
        self.jobs_typesxpath=0
        self.company_namest=0
        self.job_urls=0
        self.company_urls=0        
        
    def parse(self, response):
        self.jobs_names=response.css('h2.css-m604qf a::text').getall()
        self.jobs_locations= response.css('span.css-5wys0k').xpath('string()').getall()
        self.jobs_types=response.css('div.css-1lh32fc').xpath('string()').getall()
        self.company_names=response.css("a.css-17s97q8::text").getall()
        self.job_urls=response.css('h2.css-m604qf a::attr(href)').getall()
        self.company_urls=response.css('h2.css-m604qf a')
        for url in self.job_urls:
            yield scrapy.Request(url, callback=self.parse_job_page)
        next_page = response.css('[rel="next"] ::attr(href)').get()
        if next_page is not None:
            next_page_url = next_page
            yield response.follow(next_page_url, callback=self.parse)
    
    def parse_job_page(self,response):
        job_body=response.css("section.css-ghicub").get()
        for i in range(len(self.jobs_names)):
            yield{
                    'name':self.jobs_names[i],
                    'job_location' :self.jobs_locations[i],
                    'job_type' : str(self.jobs_types[i]).split("}")[-1],
                    'company_name': self.company_names[i],
                    'job_url': self.job_urls[i],
                    'company_url': self.company_urls[i].attrib['href'],
                    "job_body":job_body
                }
           