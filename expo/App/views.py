from django.shortcuts import render, redirect, get_object_or_404
from App.models import *
from .forms import ProductosForm, ClientesForm, VentaForm, DetalleVentaForm, UserRegistrationForm, LoginForm  
from django.contrib import messages
from django.contrib.auth import login, logout ,authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import admin
from django.core.paginator import Paginator
# Create your views here.

# Funciones para mostrar

def mostrar_index(request): 


    return render(request, 'App/index.html')


def mostrar_productos(request):
    producto = Productos.objects.all()
    context = {'producto': producto}
    return render(request, 'App/productos.html', context)


def mostrar_clientes(request):
    clientes = Clientes.objects.all()
    context = {'clientes': clientes}
    return render(request, 'App/clientes.html', context)

def mostrar_ventas(request):
    ventas = Venta.objects.all()
    context = {'ventas': ventas}
    return render(request, 'App/ventas.html', context)

def mostrar_detalle_venta(request):
    detalles = DetalleVenta.objects.all()
    context = {'detalles': detalles}
    return render(request, 'App/detalle_venta.html', context)

# Funciones para crear

def crear_producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            producto = Productos(
                nombre_producto=formulario_limpio['nombre_producto'],
                marca_producto=formulario_limpio['marca_producto'],
                descripcion=formulario_limpio['descripcion'],
                stock=formulario_limpio['stock']
            )
            producto.save()
            return redirect('productos')  # Cambia 'App/index.html' si tu template principal es otro
    else:
        form = ProductosForm()
    return render(request, 'App/crear_producto.html', {'form': form})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cliente = Clientes(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email'],
                telefono=data['telefono'],
                direccion=data['direccion']
            )
            cliente.save()
            return redirect('clientes')
    else:
        form = ClientesForm()
    return render(request, 'App/crear_cliente.html', {'form': form})

def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            venta = Venta(
                cliente=data['cliente'],
                fecha=data['fecha'],
                total=data['total']
            )
            venta.save()
            return redirect('ventas')
    else:
        form = VentaForm()
    return render(request, 'App/crear_venta.html', {'form': form})

def crear_detalle_venta(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            detalle = DetalleVenta(
                venta=data['venta'],
                producto=data['producto'],
                cantidad=data['cantidad'],
                forma_de_pago=data['forma_de_pago']
            )
            detalle.save()
            return redirect('detalle_venta')
    else:
        form = DetalleVentaForm()
    return render(request, 'App/crear_detalle_venta.html', {'form': form})

# Funciones para buscar

def buscar_marca_producto(request):
    if request.GET.get('marca_producto', False):
        marca_producto = request.GET['marca_producto']
        productos = Productos.objects.filter(marca_producto__icontains=marca_producto)
        return render(request, 'App/buscar_marca_producto.html', {'productos': productos})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/buscar_marca_producto.html', {'respuesta': respuesta})


def buscar_apellido_cliente(request):
    if request.GET.get('apellido', False):
        apellido = request.GET['apellido']
        clientes = Clientes.objects.filter(apellido__icontains=apellido)
        return render(request, 'App/buscar_apellido_cliente.html', {'clientes': clientes})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/buscar_apellido_cliente.html', {'respuesta': respuesta})


def buscar_cliente_venta(request):
    if request.GET.get('cliente', False):
        cliente = request.GET['cliente']
        ventas = Venta.objects.filter(cliente__nombre__icontains=cliente)
        return render(request, 'App/buscar_cliente_venta.html', {'ventas': ventas})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/buscar_cliente_venta.html', {'respuesta': respuesta})


def buscar_producto_detalle_venta(request):
    if request.GET.get('producto', False):
        producto = request.GET['producto']
        detalles = DetalleVenta.objects.filter(producto__nombre_producto__icontains=producto)
        return render(request, 'App/buscar_producto_detalle_venta.html', {'detalles': detalles})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/buscar_producto_detalle_venta.html', {'respuesta': respuesta})


# # Funciones para eliminar 
def eliminar_producto(request, producto_id):
    producto = Productos.objects.get(id=producto_id)
    producto.delete()
    return redirect('productos')

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)
    cliente.delete()
    return redirect('clientes')

def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    venta.delete()
    return redirect('ventas')

def eliminar_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, id=detalle_id)
    detalle.delete()
    return redirect('detalle_venta')

# Funciones para Actualizar
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id)
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            producto.nombre_producto = data['nombre_producto']
            producto.marca_producto = data['marca_producto']
            producto.descripcion = data['descripcion']
            producto.stock = data['stock']
            producto.save()
            return redirect('productos')
    else:
        form = ProductosForm(initial={
            'nombre_producto': producto.nombre_producto,
            'marca_producto': producto.marca_producto,
            'descripcion': producto.descripcion,
            'stock': producto.stock
        })
    return render(request, 'App/actualizar_producto.html', {'form': form, 'producto': producto})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cliente.nombre = data['nombre']
            cliente.apellido = data['apellido']
            cliente.email = data['email']
            cliente.telefono = data['telefono']
            cliente.direccion = data['direccion']
            cliente.save()
            return redirect('clientes')
    else:
        form = ClientesForm(initial={
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'email': cliente.email,
            'telefono': cliente.telefono,
            'direccion': cliente.direccion
        })
    return render(request, 'App/actualizar_cliente.html', {'form': form, 'cliente': cliente})

def actualizar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            venta.cliente = data['cliente']
            venta.fecha = data['fecha']
            venta.total = data['total']
            venta.save()
            return redirect('ventas')
    else:
        form = VentaForm(initial={
            'cliente': venta.cliente,
            'fecha': venta.fecha,
            'total': venta.total
        })
    return render(request, 'App/actualizar_venta.html', {'form': form, 'venta': venta})

def actualizar_detalle_venta(request, detalle_id):
    detalle = get_object_or_404(DetalleVenta, id=detalle_id)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            detalle.venta = data['venta']
            detalle.producto = data['producto']
            detalle.cantidad = data['cantidad']
            detalle.forma_de_pago = data['forma_de_pago']
            detalle.save()
            return redirect('detalle_venta')
    else:
        form = DetalleVentaForm(initial={
            'venta': detalle.venta,
            'producto': detalle.producto,
            'cantidad': detalle.cantidad,
            'forma_de_pago': detalle.forma_de_pago
        })
    return render(request, 'App/actualizar_detalle_venta.html', {'form': form, 'detalle': detalle})

# Funciones de registro y login
def registro_usuario(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el usuario sin asignarlo a una variable
            messages.success(request, '¡Registro exitoso! Bienvenido/a.')
            # Renderiza directamente el template de index después del registro exitoso
            return render(request, 'App/index.html')
    else:
        form = UserRegistrationForm()

    return render(request, 'App/registro.html', {'form': form})


def login_request(request):

    if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')

                user = authenticate(username=usuario, password=contra)

            
                if user is not None:
                        login(request, user)

                        return render(request,"App/index.html",  {"mensaje":f"Bienvenido {usuario}"} )
                else:

                        return render(request,"App/index.html", {"mensaje":"Error, datos incorrectos"} )

            else:

                    return render(request,"App/index.html" ,  {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"App/login.html", {'form':form} )


def logout_request(request):
    logout(request)
    return render(request, "App/index.html", {"mensaje": "Has cerrado sesión exitosamente."})

def privacy_policy(request):
    return render(request, "App/privacy_policy.html")

def terms_conditions(request):
    return render(request, "App/terms_conditions.html")

class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_envio')
    search_fields = ('nombre', 'email')

def listar_mensajes(request):
    mensajes = MensajeContacto.objects.all().order_by('-fecha_envio')
    paginator = Paginator(mensajes, 10)  # Mostrar 10 mensajes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'App/lista_mensajes.html', {'page_obj': page_obj} ) #{'mensajes': mensajes}


def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        asunto = request.POST.get('asunto')

        template = render_to_string('App/email-template.html',{
            'nombre': nombre,
            'email': email,
            'mensaje': mensaje,
            'asunto': asunto
        })
        emailSender = EmailMessage(
            asunto,
            template,
            settings.EMAIL_HOST_USER,
            ['ignaciogiordano03@gmail.com'], # Aca va el mail host que elegieron
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        if nombre and email and mensaje:
            # Guardar el mensaje en la base de datos
            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                mensaje=mensaje,
            )

            # Enviar confirmación al usuario
            send_mail(
                'Gracias por contactarnos ',
                f'Hola {nombre}, hemos recibido tu mensaje y te contactaremos pronto.',
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )

            messages.success(request, 'Mensaje enviado exitosamente.')
            return redirect('pagina_de_gracias')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')

    return render(request, 'App/contacto.html')


def pagina_de_gracias(request):
    return render(request, 'App/gracias.html')
