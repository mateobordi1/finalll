from django.contrib.auth.models import AbstractUser
from django.db import models
from django.apps import apps


class User(AbstractUser):
    categoria = models.CharField(max_length=100, null=True , blank=True)
    categoria_estado = models.BooleanField(default=False)
    convocado_estado = models.BooleanField(default=False)
    mail_verificado = models.BooleanField(default= False)
    fecha_nacimiento = models.DateField(max_length=100,null=True)
    telefono1 = models.IntegerField(blank=True, null=True)
    telefono2 = models.IntegerField( blank=True, null=True)
    lesiones = models.CharField(max_length=10000, blank=True)
    enfermedades = models.CharField(max_length=10000, blank=True)
    genero = models.CharField(max_length=100,null=True)
    posicion = models.CharField(max_length=100,null=True, blank=True)
    trayectoria = models.CharField(max_length=10000, blank=True)
    dni = models.IntegerField(null=True, unique=True)
    logeado_como = models.CharField(default="jugador", max_length=100)

    def __str__(self):
        return f" id : {self.id} {self.username}" 
    

    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    usuarios_en_categoria = models.ManyToManyField(User, related_name="usuarios_en_categoria", blank=True)

    def __str__(self):
        return self.nombre
    
class Partido(models.Model):
    usuarios = models.ManyToManyField(User, related_name="usuarios_convocados", blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="partido_categoria")
    rival = models.CharField(max_length=50)
    condicion= models.CharField(max_length=50)
    hora_comienzo = models.DateTimeField()
    hora_citacion = models.DateTimeField()
    partido_finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"categoria {self.categoria} vs {self.rival} de {self.condicion}"

class Asistencia(models.Model):
    jugador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asistencias_jugador')
    tomada_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asistencias_tomadas_por')
    categoria = models.CharField(max_length=50, default='Default Category')
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20) 
    comentarios = models.TextField(blank=True)
    
    def __str__(self):
        return f"Asistencia de {self.jugador} el {self.fecha} estado:{self.estado}"
