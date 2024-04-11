import scrapy


class InewsSpider(scrapy.Spider):
    name = "inews"
    allowed_domains = ["inews.co.uk"]
    start_urls = ["http://inews.co.uk/"]

    def parse(self, response):
        categories_links = response.xpath("//nav//a[contains(@href, '/category/')]/@href").getall()
        for link in categories_links:
            category_url = response.urljoin(link)
            yield scrapy.Request(category_url, callback=self.parse_category)

    def parse_category(self, response):
        for link in response.xpath("//a/@href").getall():
            if '/news/' in link:
                yield {
                    'base_url': response.url,
                    'url': response.urljoin(link),
                }