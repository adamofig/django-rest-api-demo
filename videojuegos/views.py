from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import VideoJuego
from .serializers import VideoJuegoSerializer
class VideoJuegosView(viewsets.ModelViewSet):
  queryset = VideoJuego.objects.all()
  serializer_class = VideoJuegoSerializer