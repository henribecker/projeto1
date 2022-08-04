from django.urls import path
from . import views

app_name = 'receita'


urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/categoria/<int:id_cat>/', views.categoria, name='categoria'),
    path('receitas/<int:id>/', views.receita, name='detalhe'),
]
