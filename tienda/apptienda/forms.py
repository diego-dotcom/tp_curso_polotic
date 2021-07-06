from django import forms
from django.forms import fields
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormProducto(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Producto
        fields = ('categoria', 'titulo', 'imagen', 'descripcion', 'precio', 'fecha_publicacion')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'prod_titulo'}),
            'imagen': forms.FileInput(attrs={'name':'imagen_adjunta', 'class': 'prod_imagen'}),
            'descripcion': forms.Textarea(attrs={'class': 'prod_descripcion'}),
            'precio': forms.TextInput(attrs={'class': 'prod_precio'}),
            'fecha_publicacion': forms.SelectDateWidget(attrs={'class': 'prod_fecha_publicacion'}),     
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
