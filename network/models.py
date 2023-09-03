from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    categoria = models.CharField(max_length=100, null=True , blank=True)
    categoria_estado = models.BooleanField(default=False)
    mail_verificado = models.BooleanField(default= False)
    fecha_nacimiento = models.DateField(max_length=100,null=True)
    telefono1 = models.IntegerField(blank=True, null=True)
    telefono2 = models.IntegerField( blank=True, null=True)
    lesiones = models.CharField(max_length=10000, blank=True)
    enfermedades = models.CharField(max_length=10000, blank=True)
    genero = models.CharField(max_length=100,null=True)
    posicion = models.CharField(max_length=100,null=True)
    trayectoria = models.CharField(max_length=10000, blank=True)
    dni = models.IntegerField(null=True, unique=True)
    logeado_como = models.CharField(default="jugador", max_length=100)

    def __str__(self):
        return f" id : {self.id} {self.username}" 

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
def calcular_categoria(fecha_nacimiento):
    # Obtener el año actual
    año_actual = date.today().year

    # Extraer el año de la fecha de nacimiento
    año_nacimiento = fecha_nacimiento.year

    # Calcular la edad en función del año de nacimiento
    edad = año_actual - año_nacimiento

    # Aplicar las reglas para determinar la categoría
    if 8 <= edad <= 17:
        categorias = {
            8: "cebollitas",
            9: "doceaba",
            10: "primerodecima",
            11: "decima",
            12: "novena",
            13: "octava",
            14: "septima",
            15: "sexta",
            16: "quinta",
            17: "cuarta",
        }
        return categorias[edad]
    else:
        return "Categoría no válida"