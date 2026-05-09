from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required

from .forms import RegistroForm, ProfileForm
from .models import Profile


# =========================
# REGISTRO
# =========================
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


# =========================
# LOGIN
# =========================
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


# =========================
# LOGOUT
# =========================
def logout_view(request):

    logout(request)

    return redirect('inicio')


# =========================
# PERFIL
# =========================
@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, 'accounts/profile.html', {
        'profile': profile
    })


# =========================
# EDIT PROFILE
# =========================
@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {
        'form': form
    })