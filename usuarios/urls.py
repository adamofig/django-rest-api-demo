from django.urls import path
from . import views
urlpatterns = [
path("", views.getUsuarios),
path("<int:param>/", views.getUsuarioDetail)]