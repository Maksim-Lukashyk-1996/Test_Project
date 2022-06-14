import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# Connected fields item
from scrapy.item import Item, Field



class PharmaciesparSpider(scrapy.Spider):
    name = 'pharmaciespar'
    allowed_domains = ['https://www.ziko.pl/']
    start_urls = ['https://www.ziko.pl/lokalizator/']

    def parse(self, response):
        pass
