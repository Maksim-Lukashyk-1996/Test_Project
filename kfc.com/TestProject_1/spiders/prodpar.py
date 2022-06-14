import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# Connected fields item
from scrapy.item import Item, Field

# Connected file items.py and imported Product Fields
from TestProject_1.items import Product


class ProdparSpider(scrapy.Spider):
    name = 'prodpar'
    allowed_domains = ['https://www.kfc.ru/restaurants/']
    start_urls = ['https://www.kfc.ru/restaurants/1251']

    # rules = (Rule(LinkExtractor(allow='prod',), deny=('/filter', '/?arrFilter', '/?register=', '/auth/', '/?backurl=', '/?forgot_password', '/?VIEW=LINE', '/VIEW=TABLE', '/VIEW=',)), ),)

    def parse(self, response):
        item = Product()
        item['product_url'] = response.url
        item['address'] = response.xpath('//div[@class="Mujm2VkJ7g"]//div[@class="_21yFN5Npiv"]/text()').get
        item['name'] = response.xpath('//div[@class="Mujm2VkJ7g"]//div[@class="_3zgUWz1HVh t-xl mb-24 condensed"]/text()').get
        item['phones'] = response.xpath('//div[@class="Mujm2VkJ7g"]//div[@class="_2I2E1lZDf7 t-m-sm mt-8"]/text()').get
        item['working_hours'] = response.xpath('//div[@class="Mujm2VkJ7g"]//div[@class="_2I2E1lZDf7 t-m-sm mt-8"]/text()').get
        return item
