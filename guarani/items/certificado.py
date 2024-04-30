# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Certificado(scrapy.Item):
    titulo = scrapy.Field()
    promedio = scrapy.Field()
    egreso = scrapy.Field()
    expediente = scrapy.Field()
    estado = scrapy.Field()
