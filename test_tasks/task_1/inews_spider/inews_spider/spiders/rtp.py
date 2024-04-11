import scrapy


class RtpSpider(scrapy.Spider):
    name = "rtp"
    allowed_domains = ["rtp.pt"]
    start_urls = ["https://www.rtp.pt/"]

    user_agent = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    def parse(self, response):
        category_links = response.xpath("//nav//a[contains(@href, '/noticias/')]/@href").getall()
        for link in category_links:
            yield response.follow(link, self.parse_category)

        news_links = response.xpath("//a[contains(@href, '/noticias/')]/@href").getall()
        for link in news_links:
            yield {
                'base_url': response.url,
                'url': response.urljoin(link),
            }

    def parse_category(self, response):
        news_links = response.xpath("//a[contains(@href, '/noticias/')]/@href").getall()
        for link in news_links:
            yield {
                'base_url': response.url,
                'url': response.urljoin(link),
            }