from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.receitas.factore import *

from .models import Receita


def home(request):
    receita = Receita.objects.filter(is_publicado=True).order_by('-id')
    return render(request, 'receita/pages/home.html', context={
        'receitas': receita
    })


def categoria(request, id_cat):
    receita = get_list_or_404(
        Receita.objects.filter(
            categoria__id=id_cat,
            is_publicado=True).order_by('-id')
    )

    return render(request, 'receita/pages/categoria.html', context={
        'receitas': receita,
        'titulo': f'{receita[0].categoria.name}',
        })


def receita(request, id):

    receita = Receita.objects.filter(id=id).first()

    return render(request, 'receita/pages/receita-page.html', context={'receita': receita, 'is_detail': True,
                                                                       })
