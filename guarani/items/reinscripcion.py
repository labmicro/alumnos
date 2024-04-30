# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Reinscripcion(scrapy.Item):
    codigo = scrapy.Field()
    nombre = scrapy.Field()
    año = scrapy.Field()
    fecha = scrapy.Field()
    transaccion = scrapy.Field()
