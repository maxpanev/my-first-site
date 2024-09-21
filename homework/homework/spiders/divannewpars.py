import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/krasnodar/category/svet"]

    def parse(self, response):
        lightings = response.css('div._Ud0k')  # предполагаемый селектор для карточек товаров
        for lighting in lightings:
            yield {
                'name': lighting.css('div.lsooF span::text').get(),
                'price': lighting.css('div.pY3d2 span::text').get(),
                'url': lighting.css('a').attrib['href']
            }
