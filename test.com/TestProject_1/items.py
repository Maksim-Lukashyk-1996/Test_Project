# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# rename class to product
class Product(scrapy.Item):
   product_url = scrapy.Field()
   address = scrapy.Field()
   name = scrapy.Field()
   phones = scrapy.Field()
   working_hours = scrapy.Field()