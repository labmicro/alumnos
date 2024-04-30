# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Alumno(scrapy.Item):
    documento = scrapy.Field()
    apellidos = scrapy.Field()
    nombres = scrapy.Field()
    fecha_nacimiento = scrapy.Field()
    nacionalidad = scrapy.Field()
    telefono = scrapy.Field()
    correo = scrapy.Field()
    ultima_actualizacion = scrapy.Field()
