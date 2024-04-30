from django.contrib import admin
from .models import *


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = [
        "documento",
        "apellidos",
        "nombres",
        "fecha_nacimiento",
        "correo",
        "telefono",
        "ultima_actualizacion",
    ]
    search_fields = ["documento", "apellidos", "nombres", "correo"]
