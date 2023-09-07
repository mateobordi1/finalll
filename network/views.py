import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import date , datetime
from django.core.paginator import Paginator
from django.template import loader



from .models import User , Categoria , Asistencia , Partido


@login_required(login_url='login')
def index(request):
    if request.method == "GET":

        if request.user.is_authenticated and request.user.logeado_como == "jugador":
  
            if request.user.categoria == None:
                año_actual = date.today().year
                # Extraer el año de la fecha de nacimiento
                año_nacimiento = request.user.fecha_nacimiento.year
                # Calcular la edad en función del año de nacimiento
                print(año_actual)
                print(año_nacimiento)
                edad = año_actual - año_nacimiento
                user = request.user
                print(edad)
                # Aplicar las reglas para determinar la categoría
                if edad == 18 or 17:
                    user.categoria = 'cuarta'
                if edad == 16:
                    user.categoria = 'quinta'
                if edad == 15:
                    user.categoria = 'sexta'
                if edad == 14:
                    user.categoria = 'septima'
                if edad == 13:
                    user.categoria = 'octava'
                if edad == 12:
                    user.categoria = 'novena'
                if edad == 11:
                    user.categoria = 'decima'
                if edad == 10:
                    user.categoria = 'undecima'
                if edad == 9:
                    user.categoria = 'doceaba'
                if edad <=  8:
                        user.categoria = 'cebollitas'
                user.save()

            return render(request, "network/index.html")
        
        elif request.user.is_authenticated and (request.user.logeado_como == "dt" or request.user.logeado_como == "pf"):
             
            if request.user.categoria == "0":
                categoria_asignada = False
            else:
                categoria_asignada = True
            categorias = request.user.categoria
            categoria_lista = categorias.split()
            print(categoria_lista)
            categoria = Categoria.objects.get(nombre=categoria_lista[0])
            print(categoria.id)
            jugadores = User.objects.filter(logeado_como="jugador", categoria=categoria_lista[0], categoria_estado=True ).order_by('posicion')

            return render(request, 'network/profeindex.html', {
                "jugadores": jugadores,
                "categoria_asignada": categoria_asignada,
                "categoria": categoria,
            })
        else:
            return HttpResponse("No estas logueado como algo que tenga vista disponible comonicate con el coordinador")


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
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
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
            user.first_name = first_name
            user.last_name = last_name
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

@login_required(login_url='login')
def modificar_categoria(request, categoria):
    if request.method == "GET":
        jugadores = User.objects.filter(logeado_como="jugador", categoria=categoria).order_by('posicion')
        return render(request , 'network/modificar_categoria.html', {
            "jugadores" : jugadores
        })

@login_required(login_url='login')    
def a_q(request, id_user):
    if request.method == "PUT":
        user = User.objects.get(pk=id_user)
        categoria = Categoria.objects.get(nombre=user.categoria)
        data = json.loads(request.body)
        user.categoria_estado = data["t_f"]
        categoria.usuarios_en_categoria.add(user)
        categoria.save()
        user.save()
        response_data = {
            "categoria_estado": user.categoria_estado
        }
        
        return JsonResponse(response_data, status=200)

@login_required(login_url='login')
def asistencia(request, categoria ):
    jugadores = User.objects.filter(logeado_como="jugador", categoria=categoria, categoria_estado=True)
    if request.method == "GET":
        fecha_actual = datetime.now()
        editar_asistencia =   Asistencia.objects.filter(fecha=fecha_actual, categoria=categoria).exists()
        if editar_asistencia == False:
            return render(request, 'network/asistencia.html', {
                "mensaje":"Solo podra tomar asistencia una vez por dia asegurese de no cometer errores",
                "jugadores" : jugadores,
                "categoria" :categoria,
                "fecha": fecha_actual.strftime("%d/%m/%Y")
            })
        else:
            return HttpResponse( "ya se tomo asistencia , por lo que no se puede llevar a cabo esta accion")
            
    if request.method == "POST":
        for jugador in jugadores:
                asistencia = Asistencia()
                asistencia.jugador = jugador
                asistencia.tomada_por = request.user
                asistencia.estado= request.POST.get('estado_'+str(jugador.id))
                asistencia.comentarios= request.POST.get('comentario_' +str(jugador.id))
                asistencia.categoria = jugador.categoria
                asistencia.save()

        return HttpResponseRedirect(reverse('index'))

@login_required(login_url='login')       
def jugador(request , user_id ):
    jugador =  User.objects.get(pk= user_id)
    asistencias = Asistencia.objects.filter(jugador=jugador)
    return render(request, 'network/jugador.html',{
        "jugador": jugador,
        "asistencias": asistencias
    })

@login_required(login_url='login')
def convocatoria(request, categoria_id):
    if request.method == "GET":
        try:
            convocatoria = Partido.objects.get(categoria=categoria_id, partido_finalizado=False)
            # Realiza acciones con 'convocatoria' si existe
        except Partido.DoesNotExist:
            # Acciones a realizar si no se encuentra una convocatoria
            convocatoria = None
        categoria_datos = Categoria.objects.get(pk=categoria_id)
        return render(request, 'network/convocatoria.html', {
            "convocatoria" : convocatoria , 
            "categoria": categoria_datos , 
            "mensaje": "primero completa estos datos y guardalos para poder añadir los convocados"
        })
    if request.method == "POST":
        categoria = Categoria.objects.get(id=categoria_id)
        rival = request.POST['rival']
        condicion = request.POST['condicion']
        hora_citado = request.POST['hora_citado']
        hora_partido = request.POST['hora_partido']
        try:
            partido = Partido.objects.get(categoria=categoria_id, partido_finalizado=False)
        except Partido.DoesNotExist:
            partido = Partido(
                categoria=categoria,
                rival=rival,
                condicion=condicion,
                hora_citacion=hora_citado,
                hora_comienzo=hora_partido,
                partido_finalizado=False 
            )
            partido.save()
            return HttpResponseRedirect(reverse('index')) 
        partido.rival=rival
        partido.condicion=condicion
        partido.hora_citacion=hora_citado
        partido.hora_comienzo=hora_partido
        partido.save()
        return HttpResponseRedirect(reverse('index'))

    if request.method == "PUT":

        convocatoria = Partido.objects.get(categoria=categoria_id, partido_finalizado=False)
        print(convocatoria.usuarios)
        data = json.loads(request.body)
        user = User.objects.get(pk=data["id_user"])
        print(data)
        if data["c_d"] == True:
            estado = True
            user.convocado_estado = data["c_d"]
            convocatoria.usuarios.add(user)
        else:
            estado = False
            user.convocado_estado = data["c_d"]
            convocatoria.usuarios.remove(user)
        user.save()
        convocatoria.save()

        response_data = {
            "usuario_convocado": estado
        }
        
        return JsonResponse(response_data, status=200)
    
