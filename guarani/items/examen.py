# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Examen(scrapy.Item):
    propuesta = scrapy.Field()
    codigo = scrapy.Field()
    actividad = scrapy.Field()
    fecha = scrapy.Field()
    origen = scrapy.Field()
    instancia = scrapy.Field()
    nota = scrapy.Field()
    resultado = scrapy.Field()
    turno = scrapy.Field()
    acta = scrapy.Field()
    libro = scrapy.Field()
    folio = scrapy.Field()
