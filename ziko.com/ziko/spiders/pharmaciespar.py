import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# Connected fields item
from scrapy.item import Item, Field

# Connected file items.py and imported Product Fields
from ziko.items import Pharmacies


class PharmaciesparSpider(scrapy.Spider):
    name = 'pharmaciespar'
    allowed_domains = ['https://www.ziko.pl/']
    start_urls = ['https://www.ziko.pl/lokalizator/']

    def parse(self, response):
        item = Pharmacies()
        item['product_url'] = response.url
        item['address'] = response.xpath('//tr[@class="1628 Bielsko-Biała mp-pharmacy-element"]//td[@class="mp-table-address"]/text()').get
        item['name'] = response.xpath('//tr[@class="1628 Bielsko-Biała mp-pharmacy-element"]//td[@class="mp-table-dermo"]/text()').get
        item['phones'] = response.xpath('//tr[@class="1628 Bielsko-Biała mp-pharmacy-element"]//br/text()').get
        item['working_hours'] = response.xpath('//tr[@class="Mujm2VkJ7g"]//td[@class="mp-table-hours"]/text()').get
        return item
