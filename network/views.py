import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User , Categoria

@login_required(login_url='login')
def index(request):
    if request.method == "GET":

        if request.user.is_authenticated and request.user.logeado_como == "jugador":

            return render(request, "network/index.html")
        
        elif request.user.is_authenticated and request.user.logeado_como == "dt" or "pf":
            
            jugadores = User.objects.filter(logeado_como="jugador")
            cero ="0"
            if request.user.categoria == cero:
                categoria_asignada = False
            else:
                categoria_asignada = True
            categorias = request.user.categoria
            categoria_lista = categorias.split()

            print(categoria_lista)
            return render(request, 'network/profeindex.html', {
                "jugadores": jugadores,
                "categoria_asignada": categoria_asignada,
                "categoria_lista": categoria_lista
            })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })
        fecha_nacimiento = request.POST["fecha_nacimiento"]
        telefono1 = request.POST.get("telefono1")
        telefono2 = request.POST.get("telefono2")
        lesiones = request.POST["lesiones"]
        enfermedades = request.POST["enfermedades"]
        genero = request.POST["genero"]
        posicion = request.POST["posicion"]
        trayectoria = request.POST["trayectoria"]
        dni = request.POST.get("dni")  

        # Verificar si los campos numéricos están vacíos o no son válidos
        if telefono1:
            telefono1 = int(telefono1)
        if telefono2:
            telefono2 = int(telefono2)
        if dni:
            dni = int(dni)
        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.fecha_nacimiento = fecha_nacimiento
            user.telefono1 = telefono1
            user.telefono2 = telefono2
            user.lesiones = lesiones
            user.enfermedades = enfermedades
            user.genero = genero
            user.posicion = posicion
            user.trayectoria = trayectoria
            user.dni = dni
            print(user)
            user.save()
            
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def modificar_categoria(request, categoria):
    if request.method == "GET":
        jugadores = User.objects.filter(logeado_como="jugador")
        return render(request , 'network/modificar_categoria.html', {
            "jugadores" : jugadores
        })


