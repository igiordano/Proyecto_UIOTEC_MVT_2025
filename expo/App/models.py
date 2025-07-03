from django.db import models
from django.utils import timezone

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.telefono} {self.direccion}"
    
class Productos(models.Model):
    nombre_producto = models.CharField(max_length=30)
    marca_producto = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre_producto} {self.marca_producto} {self.descripcion} {self.stock}"
    
class Venta(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='ventas')
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.id}  {self.cliente}  {self.fecha}  {self.total}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    forma_de_pago = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.venta} {self.producto} {self.cantidad} {self.forma_de_pago}"

class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f'Mensaje de {self.nombre} - {self.email}'
