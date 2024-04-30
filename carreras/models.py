from django.db import models


class Carrera(models.Model):
    codigo = models.CharField(
        max_length=6,
        verbose_name="Codigo",
        blank=False,
        null=False,
        unique=True,
    )
    nombre = models.CharField(
        max_length=30,
        verbose_name="Nombre",
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self):
        return f"{self.nombre}"


class Asignatura(models.Model):
    codigo = models.CharField(
        max_length=6,
        verbose_name="Codigo",
        blank=False,
        null=False,
        unique=True,
    )
    nombre = models.CharField(
        max_length=80,
        verbose_name="Nombre",
        blank=False,
        null=False,
        unique=True,
    )
    carreras = models.ManyToManyField(
        Carrera,
        through="AsignaturaCarrera",
        related_name="asignaturas",
    )

    def __str__(self):
        return f"{self.nombre}"
