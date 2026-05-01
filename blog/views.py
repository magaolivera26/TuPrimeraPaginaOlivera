from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm, BuscarClienteForm

def inicio(request):
    return render(request, "blog/inicio.html")


def cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            edad = form.cleaned_data["edad"]

            nuevo_cliente = Cliente(nombre=nombre, email=email, edad=edad)
            nuevo_cliente.save()

            form = ClienteForm()
    else:
        form = ClienteForm()

    return render(request, "blog/cliente.html", {"form": form})


def buscar(request):
    form = BuscarClienteForm(request.GET)
    resultado = []

    if form.is_valid():
        nombre = form.cleaned_data["nombre"]
        resultado = Cliente.objects.filter(nombre__icontains=nombre)

    return render(request, "blog/buscar.html", {
        "form": form,
        "resultado": resultado
    })

from .models import Producto
from .forms import ProductoForm

def producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            precio = form.cleaned_data["precio"]

            nuevo_producto = Producto(nombre=nombre, precio=precio)
            nuevo_producto.save()

            form = ProductoForm()
    else:
        form = ProductoForm()

    return render(request, "blog/producto.html", {"form": form})

from .models import Pedido
from .forms import PedidoForm

def pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data["cliente"]
            producto = form.cleaned_data["producto"]
            cantidad = form.cleaned_data["cantidad"]

            nuevo_pedido = Pedido(
                cliente=cliente,
                producto=producto,
                cantidad=cantidad
            )
            nuevo_pedido.save()

            form = PedidoForm()
    else:
        form = PedidoForm()

    return render(request, "blog/pedido.html", {"form": form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "blog/lista_clientes.html", {"clientes": clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "blog/lista_productos.html", {"productos": productos})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "blog/lista_pedidos.html", {"pedidos": pedidos})