# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Avance(scrapy.Item):
    codigo = scrapy.Field()
    propuesta = scrapy.Field()
    titulo = scrapy.Field()
    orientacion = scrapy.Field()
    avance = scrapy.Field()
    aprobadas = scrapy.Field()
