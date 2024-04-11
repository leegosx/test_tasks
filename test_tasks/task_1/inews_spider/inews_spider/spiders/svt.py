import scrapy


class SvtSpider(scrapy.Spider):
    name = "svt"
    allowed_domains = ["svt.se"]
    start_urls = ["http://svt.se/"]
    already_seen = set()
    
    def parse(self, response):
        categories = response.xpath("//nav//a[contains(@href, '/nyheter/')]/@href").getall()
        for category in categories:
            yield response.follow(category, self.parse_category)

        news_links = response.xpath("//a[contains(@href, '/nyheter/')]/@href").getall()
        for link in news_links:
            full_url = response.urljoin(link)
            if full_url not in self.already_seen:
                yield {
                    'base_url': response.url,
                    'url': full_url,
                }

    def parse_category(self, response):
        news_links = response.xpath("//a[contains(@href, '/nyheter/')]/@href").getall()
        for link in news_links:
            yield {
                'base_url': response.url,
                'url': response.urljoin(link),
            }