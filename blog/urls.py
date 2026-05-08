from django.urls import path
from .views import (
    inicio,
    cliente,
    buscar,
    producto,
    pedido,
    lista_clientes,
    lista_productos,
    lista_pedidos,
    pages,
    detalle_post,

    CrearPost,
    EditarPost,
    BorrarPost,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cliente/', cliente, name='cliente'),
    path('buscar/', buscar, name='buscar'),
    path('producto/', producto, name='producto'),
    path('pedido/', pedido, name='pedido'),
    
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('productos/', lista_productos, name='lista_productos'),
    path('pedidos/', lista_pedidos, name='lista_pedidos'),

    path('pages/', pages, name='pages'),
    path('pages/<int:id>/', detalle_post, name='detalle_post'),
    path('crear-post/', CrearPost.as_view(), name='crear_post'),

    path('editar-post/<int:pk>/', EditarPost.as_view(), name='editar_post'),

    path('borrar-post/<int:pk>/', BorrarPost.as_view(), name='borrar_post'),
]