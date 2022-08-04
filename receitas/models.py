from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Categoria(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Receita(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField()
    tempo_prep = models.IntegerField()
    unidade_tempo = models.CharField(max_length=10)
    porcoes = models.IntegerField()
    unidade_porcao = models.CharField(max_length=10)
    modo_preparo = models.TextField()
    modo_preparo_is_html = models.BooleanField(default=False)
    criacao = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_publicado = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='receita/covers/%Y/%m/%d/', blank=True, default='')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.titulo
