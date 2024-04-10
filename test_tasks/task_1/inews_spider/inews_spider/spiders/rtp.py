import scrapy


class RtpSpider(scrapy.Spider):
    name = "rtp"
    allowed_domains = ["rtp.pt"]
    start_urls = ["https://www.rtp.pt/"]

    user_agent = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    def parse(self, response):
        for link in response.xpath("//a/@href").getall():
            if '/noticias/' in link:
                yield {
                    'base_url': response.url,
                    'url': response.urljoin(link),
                }