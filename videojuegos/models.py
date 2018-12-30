from django.db import models

# Create your models here.
class VideoJuego(models.Model):
  nombre = models.CharField(max_length=200)
  anio = models.DateField()
  costo = models.IntegerField()