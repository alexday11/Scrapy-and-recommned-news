import scrapy

class NewspiderSpider(scrapy.Spider):
    name = "newspider"
    allowed_domains = ["www.lemonde.fr"]
    start_urls = ["https://www.lemonde.fr/en/"]

    def parse(self, response):
        news_types = response.css('.old__nav-content-list-container li.old__nav-content-list-item a::attr(href)').extract()
        
        for relative_url in news_types:
            if not relative_url.endswith('/About Us/'):
                absolute_url = response.urljoin(relative_url)
                # Pass the current news type as metadata
                yield scrapy.Request(absolute_url, callback=self.parse_news, meta={'news_type': relative_url})

    def parse_news(self, response):
        links = response.css('div.thread .teaser__link::attr(href)').extract()
        for link in links:
            if link is not None:
                yield scrapy.Request(link, callback=self.parse_detail, meta={'news_type': response.meta['news_type']})

    def parse_detail(self, response):
        yield {
            'title': response.css('h1.article__title ::text').get(),
            'short_content': response.css('p.article__desc ::text').get(),
            'content': ''.join(response.css('p.article__paragraph ::text').extract()),
            'types': response.meta.get('news_type', None)
        }
