import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# Connected fields item
from scrapy.item import Item, Field

# Connected file items.py and imported Product Fields
from monomakh.items import Pharmacies


class JewelersSpider(scrapy.Spider):
    name = 'jewelers'
    allowed_domains = ['https://monomax.by']
    start_urls = ['https://monomax.by/map']

    def parse(self, response):
        item = Pharmacies()
        item['product_url'] = response.url
        item['address'] = response.xpath('//div[@class="Mujm2VkJ7g"]//div[@class="_21yFN5Npiv"]/text()').get
        item['name'] = response.xpath(
            '//div[@class="Mujm2VkJ7g"]//div[@class="_3zgUWz1HVh t-xl mb-24 condensed"]/text()').get
        item['phones'] = response.xpath('//div[@class="Mujm2VkJ7g"]//div[@class="_2I2E1lZDf7 t-m-sm mt-8"]/text()').get
        item['working_hours'] = response.xpath(
            '//div[@class="Mujm2VkJ7g"]//div[@class="_2I2E1lZDf7 t-m-sm mt-8"]/text()').get
        return item
