from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields='__all__'

    # first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'ri','placeholder':'Nombre*'}))
    # last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'ri','placeholder':'Apellido*'}))
    # user_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'ri','placeholder':'Nombre de Usuario*'}))
    # email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'ri','placeholder':'Email*'}))
    # password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'ri','placeholder':'Contraseña*'}))

