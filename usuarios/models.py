from django.db import models

# Create your models here.

class Usuarios(models.Model):
  nombre = models.CharField(max_length=200)
  fechaCreacion = models.DateField()
  fechaCreacion = models.IntegerField(default=0)
  
  def __str__(self):
    return f"Nombre: {self.nombre}, Fecha: {self.fechaCreacion}"