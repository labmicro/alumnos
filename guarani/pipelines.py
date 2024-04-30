import django
import os
from asgiref.sync import sync_to_async


class DjangoPipeline:
    def open_spider(self, spider):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alumnos.settings")
        django.setup()

    @sync_to_async
    def process_item(self, item, spider):
        from personas.models import Persona

        fields = dict(item)
        documento = fields.pop("documento")
        Persona.objects.update_or_create(defaults=fields, documento=documento)
        return item
