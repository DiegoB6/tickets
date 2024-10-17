"""
URL configuration for ticketsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from ticketsApp.views import *

from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('', login_user, name='login_user'),
    path('admin/', admin.site.urls),
    path('cuentas/', include("django.contrib.auth.urls")),
    path('home/', TemplateView.as_view(template_name="home.html"), name="home"),

    path('logout_user', logout_user, name='logout'),

    path('signUp/', signUp, name='signUp'),

    
    path('mostrarTickets/', mostrarTickets, name='mostrarTickets'),
    path('registroTickets/', crearTicket, name="registroTickets"),
    path('editarTicket/<int:id>', editarTicket, name='editarTicket'),
    path('eliminarTicket/<int:id>', eliminarTicket, name='eliminarTicket'),

    path('mostrarOpciones/', mostrarOpciones, name='mostrarOpciones'),

    path('registroAreas/', crearAreas, name="registroAreas"),
    path('editarAreas/<int:id>', editarAreas, name='editarAreas'),
    path('eliminarAreas/<int:id>', eliminarAreas, name='eliminarAreas'),

    path('registroCriticidades/', crearCriticidades, name="registroCriticidades"),
    path('editarCriticidades/<int:id>', editarCriticidades, name='editarCriticidades'),
    path('eliminarCriticidades/<int:id>', eliminarCriticidades, name='eliminarCriticidades'),

    path('registroEstados/', crearEstados, name="registroEstados"),
    path('editarEstados/<int:id>', editarEstados, name='editarEstados'),
    path('eliminarEstados/<int:id>', eliminarEstados, name='eliminarEstados'),

    path('registroServicios/', crearServicios, name="registroServicios"),
    path('editarServicios/<int:id>', editarServicios, name='editarServicios'),
    path('eliminarServicios/<int:id>', eliminarServicios, name='eliminarServicios'),

    path('registroTipos/', crearTipos, name="registroTipos"),
    path('editarTipos/<int:id>', editarTipos, name='editarTipos'),
    path('eliminarTipos/<int:id>', eliminarTipos, name='eliminarTipos'),
    
]
