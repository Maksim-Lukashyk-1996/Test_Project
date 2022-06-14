import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from TestProject_1.items import Product


class ProdparSpider(scrapy.Spider):
    name = 'prodpar'
    allowed_domains = ['https://www.kfc.ru/restaurants/']
    start_urls = ['https://www.kfc.ru/restaurants/1251']

    # rules = (Rule(LinkExtractor(allow='prod',), deny=('/filter', '/?arrFilter', '/?register=', '/auth/', '/?backurl=', '/?forgot_password', '/?VIEW=LINE', '/VIEW=TABLE', '/VIEW=',)), ),)

    def parse(self, response):
        item = Product()
        item['product_url'] = response.url
        return item