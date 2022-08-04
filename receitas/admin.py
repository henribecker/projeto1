from tabnanny import verbose
from django.contrib import admin

from .models import Categoria, Receita
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    ...
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class ReceitaAdmin(admin.ModelAdmin):
    ...
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)
