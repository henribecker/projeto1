from django.shortcuts import render
from utils.receitas.factore import *


def home(request):
    return render(request, 'receita/pages/home.html', context={
        'receitas': [make_receita() for _ in range(10)]
    })


def receita(request, id):
    return render(request, 'receita/pages/receita-page.html', context={'receita': make_receita(), 'is_detail': True,
    })
