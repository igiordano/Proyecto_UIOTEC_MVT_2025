from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm


class ProductosForm(forms.Form):
    nombre_producto = forms.CharField(max_length=30, label="Nombre del producto")
    marca_producto = forms.CharField(max_length=20, label="Marca del producto")
    descripcion = forms.CharField(widget=forms.Textarea, required=False, label="Descripción")
    stock = forms.IntegerField(min_value=0, label="Stock")

class ClientesForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    email = forms.EmailField(label="Email")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    direccion = forms.CharField(max_length=200, required=False, label="Dirección")  

class VentaForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Clientes.objects.all(), label="Cliente")
    fecha = forms.DateTimeField(
        label="Fecha",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
    total = forms.DecimalField(max_digits=10, decimal_places=2, label="Total")

class DetalleVentaForm(forms.Form):
    venta = forms.ModelChoiceField(queryset=Venta.objects.all(), label="Venta")
    producto = forms.ModelChoiceField(queryset=Productos.objects.all(), label="Producto")
    cantidad = forms.IntegerField(min_value=1, label="Cantidad")
    forma_de_pago = forms.CharField(max_length=25, label="Forma de pago")

class MensajeContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    email = forms.EmailField(label="Email")
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")
    fecha_envio = forms.DateTimeField(label="Fecha de envío")

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=150, label="Nombre de usuario")
    password1 = forms.CharField(widget=PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}

# - Logear  un usuario

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


    