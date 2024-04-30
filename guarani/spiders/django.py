import scrapy

from . import alumno


class Importar(alumno.Alumno):
    name = "importador"
    actions_list = [
        alumno.propuestas,
        # FichaAlumno.reinscripciones,
        # FichaAlumno.certificados,
        # FichaAlumno.avance,
        # FichaAlumno.historial,
    ]
    students_list = [
        "41533618",
    ]

    def process_metadata(self, **kwargs) -> list:
        resultado = []
        resultado.append(kwargs["alumno"])
        # for _, valor in kwargs.items():
        #     if issubclass(valor.__class__, scrapy.Item):
        #         resultado.append(valor)
        #     elif issubclass(valor.__class__, list):
        #         for entrada in valor:
        #             resultado.append(entrada)
        return resultado
