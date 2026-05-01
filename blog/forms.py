from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()


class ProductoForm(forms.Form):
    nombre = forms.CharField()
    precio = forms.FloatField()


class PedidoForm(forms.Form):
    cliente = forms.CharField()
    producto = forms.CharField()
    cantidad = forms.IntegerField()


class BuscarClienteForm(forms.Form):
    nombre = forms.CharField()
