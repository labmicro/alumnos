import scrapy


class Guarani(scrapy.Spider):
    name = "guarani"
    allowed_domains = ["guarani.unt.edu.ar"]
    start_urls = ["https://guarani.unt.edu.ar/guarani/"]
    login_url = "https://guarani.unt.edu.ar/guarani/"
    user = "23517968"
    password = "neqpuF-4hocnu-rerdog"

    def start_requests(self):
        login_url = "https://guarani.unt.edu.ar/guarani/"
        return [
            scrapy.Request(login_url, callback=self.send_login),
        ]

    def send_login(self, response):
        token = response.css("form input[name=cstoken]::attr(value)").extract_first()
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                "cstoken": token,
                "form_5000221_datos": "ingresar",
                "form_5000221_datos_implicito": "",
                "ef_form_5000221_datosusuario": self.user,
                "ef_form_5000221_datosclave": self.password,
            },
            callback=self.get_main_page,
        )

    def get_main_page(self, response):
        return scrapy.Request(
            "https://guarani.unt.edu.ar/guarani/aplicacion.php?ah=st6537e7596791a9.30917761&ai=guarani%7C%7C2",
            callback=self.get_requested_urls,
        )

    def get_requested_urls(self, response):
        for url in self.start_urls:
            return scrapy.Request(url)
