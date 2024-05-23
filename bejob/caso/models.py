from typing import Any
from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
           return self.titulo