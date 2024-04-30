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


class Certificado(scrapy.Item):
    titulo = scrapy.Field()
    promedio = scrapy.Field()
    egreso = scrapy.Field()
    expediente = scrapy.Field()
    estado = scrapy.Field()


class Reinscripcion(scrapy.Item):
    codigo = scrapy.Field()
    nombre = scrapy.Field()
    año = scrapy.Field()
    fecha = scrapy.Field()
    transaccion = scrapy.Field()


class Avance(scrapy.Item):
    codigo = scrapy.Field()
    propuesta = scrapy.Field()
    titulo = scrapy.Field()
    orientacion = scrapy.Field()
    avance = scrapy.Field()
    aprobadas = scrapy.Field()


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


class Actividad(scrapy.Item):
    codigo = scrapy.Field()
    actividad = scrapy.Field()
    inscripcion = scrapy.Field()
    aprobacion = scrapy.Field()
    calificacion = scrapy.Field()
