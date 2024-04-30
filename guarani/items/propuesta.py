# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Propuesta(scrapy.Item):
    codigo = scrapy.Field()
    nombre = scrapy.Field()
    año = scrapy.Field()
    inscripcion = scrapy.Field()
    ingreso = scrapy.Field()
    calidad = scrapy.Field()
    motivo = scrapy.Field()
