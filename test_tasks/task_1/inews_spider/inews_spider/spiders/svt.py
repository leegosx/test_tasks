import scrapy


class SvtSpider(scrapy.Spider):
    name = "svt"
    allowed_domains = ["svt.se"]
    start_urls = ["http://svt.se/"]
    
    def parse(self, response):
        for link in response.xpath("//a/@href").getall():
            if '/nyheter/' in link:
                yield {
                    'base_url': response.url,
                    'url': response.urljoin(link),
                }