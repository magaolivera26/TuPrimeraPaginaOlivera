from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


#  Registro de usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


#  Editar perfil (avatar)
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']