import scrapy


class RtbfSpider(scrapy.Spider):
    name = "rtbf"
    allowed_domains = ["rtbf.be"]
    # use 'en-continu' because it contains all articles
    start_urls = ["https://www.rtbf.be/en-continu"]

    user_agent = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    def parse(self, response):
        for link in response.xpath("//a/@href").getall():
            if '/article/' in link:
                yield {
                    'base_url': response.url,
                    'url': response.urljoin(link),
                }
