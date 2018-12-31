# Django Rest Framework + MySql

Este proyecto es una demostración de una Api en Django RestFramework ya configurada para desplegar en AppEngine.

## Ejecución 

Primero agrega una base de datos en la linea 93 de MiApiRest/settings.py
Luego ejecuta los camandos siguientes que realizaran las tareas de:

1) Crea un ambiente virtual
2) Activa tu ambiente virtual
3) Instala las librerias
4) ejecuta

  
  ```sh
python -m venv env

.\env\Scripts\activate

pip install -r requirements.txt

python manage.py runserver
```

## Proyecto base
Si deseas usar este proyecto como base para crear el tuyo deberás

1) Agregar las configuraciones para conectarse a tu base de datos mysql en MiApiRest/settings.
2) Eliminar las aplicaciones innecesarias, directorios /usuarios y /videojuegos.
3) Corregir los archivos urls.py y settings.py que quedaran afectados por la eliminación de aplicaciones
4) Inicia la construcción de tu Api

Visita los tutoriales para saber cómo se construyó este proyecto.

https://medium.com/@jordan.figu/django-fundamentos-de-rest-apis-d136072fbaed
https://medium.com/@jordan.figu/django-rest-framework-despliegue-en-google-cloud-app-engine-21a9ca20d082
