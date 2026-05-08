from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from .forms import RegistroForm


def register(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

            return redirect('inicio')

    else:

        form = RegistroForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=password)

            if user is not None:

                login(request, user)

                return redirect('inicio')

    else:

        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form': form
    })


def logout_view(request):

    logout(request)

    return redirect('inicio')