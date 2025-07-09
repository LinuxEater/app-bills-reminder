from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contas, name='lista_contas'),
]