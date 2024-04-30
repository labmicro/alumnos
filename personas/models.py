from django.db import models


class Persona(models.Model):
    documento = models.CharField(
        max_length=15,
        verbose_name="Numero de documento",
        blank=False,
        null=False,
        unique=True,
    )
    apellidos = models.CharField(
        max_length=30,
        verbose_name="Apellidos de la persona",
        blank=False,
        null=False,
    )
    nombres = models.CharField(
        max_length=30,
        verbose_name="Nombres de la persona",
        blank=False,
        null=False,
    )
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de nacimiento",
        blank=False,
        null=False,
    )
    nacionalidad = models.CharField(
        max_length=30,
        verbose_name="Nacionalidad",
        blank=True,
        null=True,
    )
    correo = models.EmailField(
        max_length=64,
        verbose_name="Correo electronico",
        blank=True,
        null=True,
        unique=True,
    )
    telefono = models.CharField(
        max_length=64,
        verbose_name="Teléfono",
        blank=True,
        null=True,
    )
    ultima_actualizacion = models.DateField(
        verbose_name="Ultima actualizacion",
        blank=False,
        null=False,
    )

    @property
    def nombre_completo(self):
        return f"{self.apellidos}, {self.nombres}"

    def __str__(self):
        return self.nombre_completo
