from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass