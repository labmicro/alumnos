# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Estado(scrapy.Item):
    año = scrapy.Field()
    documento = scrapy.Field()
    apellidos = scrapy.Field()
    nombres = scrapy.Field()
    inscripcion = scrapy.Field()
    propuestas = scrapy.Field()
    examenes = scrapy.Field()
    aprobadas = scrapy.Field()
    primero = scrapy.Field()
    ultimo = scrapy.Field()
    avance = scrapy.Field()
    duracion = scrapy.Field()
    activo = scrapy.Field()
    egresado = scrapy.Field()
    graduacion = scrapy.Field()
    expediente = scrapy.Field()
    certificado = scrapy.Field()
