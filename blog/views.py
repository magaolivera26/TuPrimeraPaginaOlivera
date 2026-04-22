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