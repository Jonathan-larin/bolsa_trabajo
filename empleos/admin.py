
# Register your models here.
from django.contrib import admin
from .models import Empresa, Categoria, Vacante, Candidato, Postulacion,Perfil

admin.site.register(Empresa)
admin.site.register(Categoria)
admin.site.register(Vacante)
admin.site.register(Candidato)
admin.site.register(Postulacion)
admin.site.register(Perfil)
