from rest_framework import serializers
from .models import VideoJuego
class VideoJuegoSerializer(serializers.ModelSerializer):
  class Meta:
    model = VideoJuego
    fields = '__all__'