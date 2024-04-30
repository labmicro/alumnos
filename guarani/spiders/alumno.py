import re, datetime, collections
import scrapy
import guarani.items

from .guarani import Guarani

Action = collections.namedtuple("Action", ["name", "formdata", "callback", "parser"])

propuestas = Action(
    name="propuestas",
    formdata={
        "cstoken": None,
        "ci_41000611": "",
        "ci_41000611__param": "",
        "ci_41000614_ci_reportes_ficha_alumno": "cambiar_tab_propuestas",
        "ci_41000614_ci_reportes_ficha_alumno__param": "undefined",
        "ci_41000615_rep_datos_personales": "",
        "ci_41000615_rep_datos_personales__param": "",
        "form_41000616_form_foto": "",
        "form_41000616_form_foto_implicito:": "",
    },
    callback="get_action_results",
    parser="pase_student_degrees",
)

reinscripciones = Action(
    name="reinscripciones",
    formdata={
        "cstoken": None,
        "ci_41000611": "",
        "ci_41000611__param": "",
        "ci_41000614_ci_reportes_ficha_alumno": "cambiar_tab_reinscripcion_propuesta",
        "ci_41000614_ci_reportes_ficha_alumno__param": "undefined",
        "ci_41000615_rep_datos_personales": "",
        "ci_41000615_rep_datos_personales__param": "",
        "form_41000616_form_foto": "",
        "form_41000616_form_foto_implicito:": "",
    },
    callback="get_action_results",
    parser="parse_student_reinscriptions",
)

certificados = Action(
    name="certificados",
    formdata={
        "cstoken": None,
        "ci_41000611": "",
        "ci_41000611__param": "",
        "ci_41000614_ci_reportes_ficha_alumno": "cambiar_tab_certificados_obtenidos",
        "ci_41000614_ci_reportes_ficha_alumno__param": "undefined",
        "ci_41000615_rep_datos_personales": "",
        "ci_41000615_rep_datos_personales__param": "",
        "form_41000616_form_foto": "",
        "form_41000616_form_foto_implicito:": "",
    },
    callback="get_action_results",
    parser="parse_student_certificates",
)

avance = Action(
    name="avance",
    formdata={
        "cstoken": None,
        "ci_41000611": "",
        "ci_41000611__param": "",
        "ci_41000614_ci_reportes_ficha_alumno": "cambiar_tab_avance_x_propuesta",
        "ci_41000614_ci_reportes_ficha_alumno__param": "undefined",
        "ci_41000615_rep_datos_personales": "",
        "ci_41000615_rep_datos_personales__param": "",
        "form_41000616_form_foto": "",
        "form_41000616_form_foto_implicito:": "",
    },
    callback="get_action_results",
    parser="parse_student_advance",
)

historial = Action(
    name="historial",
    formdata={
        "cstoken": None,
        "ci_41000611": "",
        "ci_41000611__param": "",
        "ci_41000614_ci_reportes_ficha_alumno": "cambiar_tab_historia_academica",
        "ci_41000614_ci_reportes_ficha_alumno__param": "undefined",
        "ci_41000615_rep_datos_personales": "",
        "ci_41000615_rep_datos_personales__param": "",
        "form_41000616_form_foto": "",
        "form_41000616_form_foto_implicito:": "",
    },
    callback="get_action_results",
    parser="parse_student_history",
)


class Alumno(Guarani):
    name = "alumnos"
    start_urls = [
        "https://guarani.unt.edu.ar/guarani/aplicacion.php?tm=1&tcm=central&ai=guarani||41000086",
    ]

    actions_list = []
    students_list = []

    def __init__(self, *args, **kwargs):
        self.current_student = None
        self.student_iterator = iter(self.students_list)

        self.current_action = None
        self.actions_iterator = iter(self.actions_list)

        self.spider_id = kwargs.pop("spider_id", None)
        super().__init__(*args, **kwargs)

    def parse(self, response):
        token = response.css("form input[name=cstoken]::attr(value)").extract_first()

        try:
            self.current_student = next(self.student_iterator)
        except StopIteration:
            return None

        return scrapy.FormRequest.from_response(
            response,
            formid="formulario_toba",
            formdata={
                "cstoken": token,
                "ei_41000612_filtro": "filtrar",
                "ei_41000612_filtro_implicito": "",
                "js_ei_41000612_filtro_listafilas": "nro_documento",
                "js_ei_41000612_filtro__parametros": "",
                "col_ei_41000612_filtroapellido": "contiene",
                "ef_ei_41000612_filtroapellido": "",
                "col_ei_41000612_filtronombres": "contiene",
                "ef_ei_41000612_filtronombres": "",
                "col_ei_41000612_filtronro_documento": "contiene",
                "ef_ei_41000612_filtronro_documento": self.current_student,
                "col_ei_41000612_filtrolegajo": "contiene",
                "ef_ei_41000612_filtrolegajo": "",
                "js_ei_41000612_filtro_nuevo": "nopar",
                "cuadro_41000613_cuadro": "",
                "cuadro_41000613_cuadro__seleccion": "",
                "cuadro_41000613_cuadro__extra": "",
                "cuadro_41000613_cuadro__orden_columna": "",
                "cuadro_41000613_cuadro__orden_sentido": "",
                "cuadro_41000613_cuadro__ordenamiento_multiple": "",
            },
            callback=self.select_student_from_list,
        )

    def select_student_from_list(self, response):
        token = response.css("form input[name=cstoken]::attr(value)").extract_first()
        return scrapy.FormRequest.from_response(
            response,
            formid="formulario_toba",
            formdata={
                "cstoken": token,
                "ei_41000612_filtro": "",
                "ei_41000612_filtro_implicito": "",
                "js_ei_41000612_filtro_listafilas": "",
                "js_ei_41000612_filtro__parametros": "",
                "col_ei_41000612_filtroapellido": "contiene",
                "ef_ei_41000612_filtroapellido": "",
                "col_ei_41000612_filtronombres": "contiene",
                "ef_ei_41000612_filtronombres": "",
                "col_ei_41000612_filtronro_documento": "contiene",
                "ef_ei_41000612_filtronro_documento": self.current_student,
                "col_ei_41000612_filtrolegajo": "contiene",
                "ef_ei_41000612_filtrolegajo": "",
                "js_ei_41000612_filtro_nuevo": "nopar",
                "cuadro_41000613_cuadro": "seleccion",
                "cuadro_41000613_cuadro__seleccion": "0",
                "cuadro_41000613_cuadro__extra": "",
                "cuadro_41000613_cuadro__orden_columna": "",
                "cuadro_41000613_cuadro__orden_sentido": "",
                "cuadro_41000613_cuadro__ordenamiento_multiple": "",
            },
            callback=self.get_student_main_data,
        )

    def get_student_main_data(self, response):
        alumno = self.pase_student_data(response)

        self.current_action = next(self.actions_iterator)
        formdata = self.current_action.formdata
        formdata["cstoken"] = response.css(
            "form input[name=cstoken]::attr(value)"
        ).extract_first()
        callback = getattr(self, self.current_action.callback)

        return scrapy.FormRequest.from_response(
            response,
            formid="formulario_toba",
            formdata=formdata,
            callback=callback,
            meta={"alumno": alumno},
        )

    def get_action_results(self, response):
        parser = getattr(self, self.current_action.parser)
        meta = parser(response)

        try:
            self.current_action = next(self.actions_iterator)
            formdata = self.current_action.formdata
            formdata["cstoken"] = response.css(
                "form input[name=cstoken]::attr(value)"
            ).extract_first()
            callback = getattr(self, self.current_action.callback)

            yield scrapy.FormRequest.from_response(
                response,
                formid="formulario_toba",
                formdata=formdata,
                callback=callback,
                meta=meta,
            )
        except StopIteration:
            result = self.process_metadata(**meta)
            for item in result:
                if issubclass(item.__class__, scrapy.Item):
                    yield item

            self.actions_iterator = iter(self.actions_list)
            yield scrapy.Request(
                self.start_urls[0], callback=self.parse, dont_filter=True
            )

    def pase_student_data(self, response):
        celdas = response.xpath(
            '//tr[@class="ei-form-fila"]/td[2]/span/text()'
        ).getall()
        apellidos, nombres = celdas[0].strip().split(",", maxsplit=1)
        return guarani.items.Alumno(
            documento=celdas[1].strip(),
            apellidos=apellidos.replace(",", " ").strip().upper(),
            nombres=nombres.replace(",", " ").strip().title(),
            fecha_nacimiento=datetime.datetime.strptime(
                celdas[-20].strip(), "%d/%m/%Y"
            ).date(),
            nacionalidad=celdas[7].strip(),
            telefono=celdas[-3].strip(),
            correo=celdas[-2].strip(),
            ultima_actualizacion=datetime.datetime.strptime(
                celdas[-1].strip(), "%d/%m/%Y"
            ).date(),
        )

    def pase_student_degrees(self, response):
        meta = response.meta
        propuestas = []
        filas = response.xpath('//table[@class="tabla-0"]/tr')
        for fila in filas:
            titulo = fila.xpath(
                'td[@class="ei-cuadro-cc-tit-nivel-0"]/strong/text()'
            ).extract_first()
            if titulo:
                codigo, nombre = re.findall(r"\((.+)\) - (.+)", titulo)[0]
            else:
                celdas = fila.xpath(
                    f"td[not(@class='ei-cuadro-col-tit')]/text()"
                ).getall()
                if len(celdas) == 15:
                    propuestas.append(
                        guarani.items.Propuesta(
                            codigo=codigo,
                            nombre=nombre,
                            año=celdas[0].strip(),
                            inscripcion=datetime.datetime.strptime(
                                celdas[2].strip(), "%d/%m/%Y"
                            ).date(),
                            ingreso=datetime.datetime.strptime(
                                celdas[1].strip(), "%d/%m/%Y"
                            ).date(),
                            calidad=celdas[-5].strip(),
                            motivo=celdas[-4].strip(),
                        )
                    )
        meta["propuestas"] = propuestas
        return meta

    def parse_student_reinscriptions(self, response):
        meta = response.meta
        reinscripciones = []
        filas = response.xpath('//table[@class="tabla-0"]/tr')
        for fila in filas:
            titulo = fila.xpath(
                'td[@class="ei-cuadro-cc-tit-nivel-0"]/strong/text()'
            ).extract_first()
            if titulo:
                codigo, nombre = re.findall(r"\((.+)\) - (.+)", titulo)[0]
            else:
                celdas = fila.xpath(
                    f"td[not(@class='ei-cuadro-col-tit')]/text()"
                ).getall()
                if len(celdas) == 3:
                    reinscripciones.append(
                        guarani.items.Reinscripcion(
                            codigo=codigo,
                            nombre=nombre,
                            año=celdas[0].strip(),
                            fecha=datetime.strptime(
                                celdas[1].strip(), "%d/%m/%Y %H:%M:%S"
                            ),
                            transaccion=celdas[2].strip(),
                        )
                    )
        meta["reinscripciones"] = reinscripciones
        return meta

    def parse_student_certificates(self, response):
        meta = response.meta
        certificados = []
        filas = response.xpath('//table[@class="tabla-0"]/tr')

        for fila in filas:
            celdas = fila.xpath(f"td[not(@class='ei-cuadro-col-tit')]/text()").getall()
            if len(celdas) == 5:
                certificados.append(
                    guarani.items.Certificado(
                        titulo=celdas[0].strip(),
                        promedio=celdas[1].strip(),
                        egreso=datetime.strptime(celdas[2].strip(), "%d/%m/%Y").date(),
                        expediente=celdas[3].strip(),
                        estado=celdas[4].strip(),
                    )
                )

        meta["certificados"] = certificados
        return meta

    def parse_student_advance(self, response):
        meta = response.meta
        avances = []
        filas = response.xpath('//table[@class="tabla-0"]/tr')
        for fila in filas:
            titulo = fila.xpath(
                'td[@class="ei-cuadro-cc-tit-nivel-0"]/strong/text()'
            ).extract_first()
            if titulo:
                codigo, nombre = re.findall(r"\((.+)\) (.+)", titulo)[0]
            else:
                celdas = fila.xpath(
                    f"td[not(@class='ei-cuadro-col-tit')]/text()"
                ).getall()
                if len(celdas) == 5:
                    avances.append(
                        guarani.items.Avance(
                            codigo=codigo,
                            propuesta=nombre,
                            titulo=celdas[0].strip(),
                            orientacion=celdas[1].strip(),
                            avance=celdas[-2].strip(),
                            aprobadas=celdas[-1].strip(),
                        )
                    )
        meta["avances"] = avances
        return meta

    def parse_student_history(self, response):
        meta = response.meta
        examenes = []
        filas = response.xpath('//table[@class="tabla-0"]/tr')
        for fila in filas:
            titulo = fila.xpath(
                'td[@class="ei-cuadro-cc-tit-nivel-0"]/strong/text()'
            ).extract_first()
            if titulo:
                nombre = titulo
            else:
                celdas = fila.xpath(
                    f"td[not(@class='ei-cuadro-col-tit')]/text()"
                ).getall()
                if len(celdas) == 15:
                    campos = re.findall(r"\((.+)\) (.+)", celdas[0].strip())[0]
                    examenes.append(
                        guarani.items.Examen(
                            propuesta=nombre,
                            codigo=campos[0].strip(),
                            actividad=campos[1].strip(),
                            fecha=datetime.strptime(
                                celdas[1].strip(), "%d/%m/%Y"
                            ).date(),
                            origen=celdas[2].strip(),
                            instancia=celdas[3].strip(),
                            nota=celdas[4].strip(),
                            resultado=celdas[5].strip(),
                            turno=celdas[-4].strip(),
                            acta=celdas[-3].strip(),
                            libro=celdas[-2].strip(),
                            folio=celdas[-1].strip(),
                        )
                    )
        meta["examenes"] = examenes
        return meta

    def process_metadata(self, **kwargs) -> list:
        return None


class PruebaAlumno(Alumno):
    name = "prueba_alumno"
    actions_list = [
        propuestas,
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
        for _, valor in kwargs.items():
            if issubclass(valor.__class__, scrapy.Item):
                resultado.append(valor)
            elif issubclass(valor.__class__, list):
                for entrada in valor:
                    resultado.append(entrada)
        return resultado
