from django.urls import path
from .views import inicio, cliente, buscar

urlpatterns = [
    path("", inicio),
    path("cliente/", cliente),
    path("buscar/", buscar),
]