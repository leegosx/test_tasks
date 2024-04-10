import scrapy


class InewsSpider(scrapy.Spider):
    name = "inews"
    allowed_domains = ["inews.co.uk"]
    start_urls = ["http://inews.co.uk/"]

    def parse(self, response):
        for link in response.xpath("//a/@href").getall():
            if '/news/' in link:
                yield {
                    'base_url': response.url,
                    'url': response.urljoin(link), 
                }