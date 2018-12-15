from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Usuarios
def getUsuarios(request):
  users = Usuarios.objects.all()
  data = list(users.values("id","nombre","fechaCreacion"))
  return JsonResponse(data, safe=False)

def getUsuarioDetail(request, param):
  data = Usuarios.objects.filter(id=param)
  return JsonResponse(list(data.values("id","nombre")),safe=False)