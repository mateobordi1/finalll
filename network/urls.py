
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("modificar_categoria/<str:categoria>", views.modificar_categoria , name="modificar_categoria"),
    path("a_q/<int:id_user>", views.a_q , name="a_q" ),  
]
