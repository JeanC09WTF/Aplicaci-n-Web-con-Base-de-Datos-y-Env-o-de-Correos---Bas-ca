from django.contrib import admin
from Modulos.Academica.models import * #importarlo  de models
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)
