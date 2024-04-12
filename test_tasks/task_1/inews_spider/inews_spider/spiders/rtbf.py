import scrapy


class RtbfSpider(scrapy.Spider):
    name = "rtbf"
    allowed_domains = ["rtbf.be"]
    start_urls = ["https://www.rtbf.be"]

    user_agent = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    def parse(self, response):
        categories_links = response.xpath("//nav//a[contains(@href, '/info/') or contains(@href, '/sport/') or contains(@href, '/culture/')]/@href").getall()
        for link in categories_links:
            yield response.follow(link, self.parse_category)

        yield response.follow("https://www.rtbf.be/en-continu", self.parse_latest_news)

    def parse_category(self, response):
        for link in response.xpath("//a[contains(@href, '/article/')]/@href").getall():
            yield {
                'base_url': response.url,
                'url': response.urljoin(link),
            }

    def parse_latest_news(self, response):
        for link in response.xpath("//a[contains(@href, '/article/')]/@href").getall():
            yield {
                'base_url': response.url,
                'url': response.urljoin(link),
            }