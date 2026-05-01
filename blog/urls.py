from django.urls import path
from .views import inicio, cliente, buscar, producto, pedido, lista_clientes, lista_productos, lista_pedidos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cliente/', cliente, name='cliente'),
    path('buscar/', buscar, name='buscar'),
    path('producto/', producto, name='producto'),
    path('pedido/', pedido, name='pedido'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('productos/', lista_productos, name='lista_productos'),
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
]