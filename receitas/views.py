from django.shortcuts import render


def home(request):
    return render(request, 'receita/pages/home.html')
