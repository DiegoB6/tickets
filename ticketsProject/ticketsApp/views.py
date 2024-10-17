from django.shortcuts import render, redirect

from ticketsApp.models import *
from ticketsApp.forms import *

from . import forms

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import Usuario
from .forms import SingUpForm
# Create your views here.


def mostrarTickets(request):
    Tickets = Ticket.objects.all()
    data = {'tickets': Tickets,
            'titulo': 'Lista de personas'
    }
    return render (request, 'ticketsApp/mostrarTickets.html', data)


def crearTicket(request):
    form = forms.TicketsForm()

    if request.method == 'POST':
        form = forms.TicketsForm(request.POST)
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse('mostrarTickets') )

    data = {'form': form,
            'titulo': 'Crear ticket'
            }
    return render(request, 'ticketsApp/registroTickets.html', data)


def editarTicket(request, id):
    ticket = Ticket.objects.get(id = id)
    form = TicketsForm(instance=ticket)
    if (request.method == 'POST'):
        form = TicketsForm(request.POST, instance=ticket)
        if form.is_valid():
            print("El form es valido")
            form.save()
            return HttpResponseRedirect(reverse('mostrarTickets') )
        else:
            print("Hay errores: ", form.errors)

    data = {'form': form,
            'titulo': 'Editar ticket'
            }
    return render(request, 'ticketsApp/registroTickets.html', data)



def eliminarTicket(request,id):
    ticket = Ticket.objects.get(id = id)
    ticket.delete()
    return HttpResponseRedirect(reverse('mostrarTickets') )






def mostrarOpciones(request):
    areas = Area.objects.all()
    criticidades = Criticidad.objects.all()
    estados = Estado.objects.all()
    servicios = Servicio.objects.all()
    tipos = Tipo.objects.all()
    data = {
            'areas': areas,
            'criticidades': criticidades,
            'estados': estados,
            'servicios': servicios,
            'tipos': tipos,
            'titulo': 'Opciones del ticket'
    }
    return render (request, 'ticketsApp/mostrarOpciones.html', data)




def crearAreas(request):
    formarea = forms.AreasForms()

    if request.method == 'POST':
        formarea = forms.AreasForms(request.POST)
        if formarea.is_valid():
            print("El formulario es valido")
            formarea.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )

    data = {'formarea': formarea,
            'titulo': 'Crear Area'
            }
    return render(request, 'ticketsApp/registroAreas.html', data)


def editarAreas(request, id):
    area = Area.objects.get(id = id)
    formarea = AreasForms(instance=area)
    if (request.method == 'POST'):
        formarea = AreasForms(request.POST, instance=area)
        if formarea.is_valid():
            print("El form es valido")
            formarea.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )
        else:
            print("Hay errores: ", formarea.errors)

    data = {'formarea': formarea,
            'titulo': 'Editar Area'
            }
    return render(request, 'ticketsApp/registroAreas.html', data)


def eliminarAreas(request,id):
    area = Area.objects.get(id = id)
    area.delete()
    return HttpResponseRedirect(reverse('mostrarOpciones') )




def crearCriticidades(request):
    formcriticidad = forms.CriticidadesForms()

    if request.method == 'POST':
        formcriticidad = forms.CriticidadesForms(request.POST)
        if formcriticidad.is_valid():
            print("El formulario es valido")
            formcriticidad.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )

    data = {'formcriticidad': formcriticidad,
            'titulo': 'Crear Criticidad'
            }
    return render(request, 'ticketsApp/registroCriticidades.html', data)


def editarCriticidades(request, id):
    criticidad = Criticidad.objects.get(id = id)
    formcriticidad = CriticidadesForms(instance=criticidad)
    if (request.method == 'POST'):
        formcriticidad = CriticidadesForms(request.POST, instance=criticidad)
        if formcriticidad.is_valid():
            print("El form es valido")
            formcriticidad.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )
        else:
            print("Hay errores: ", formcriticidad.errors)

    data = {'formcriticidad': formcriticidad,
            'titulo': 'Editar Criticidad'
            }
    return render(request, 'ticketsApp/registroCriticidades.html', data)



def eliminarCriticidades(request,id):
    criticidad = Criticidad.objects.get(id = id)
    criticidad.delete()
    return HttpResponseRedirect(reverse('mostrarOpciones') )




def crearEstados(request):
    formestado = forms.EstadosForms()

    if request.method == 'POST':
        formestado = forms.EstadosForms(request.POST)
        if formestado.is_valid():
            print("El formulario es valido")
            formestado.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )

    data = {'formestado': formestado,
            'titulo': 'Crear Estado'
            }
    return render(request, 'ticketsApp/registroEstados.html', data)


def editarEstados(request, id):
    estado = Estado.objects.get(id = id)
    formestado = EstadosForms(instance=estado)
    if (request.method == 'POST'):
        formestado = EstadosForms(request.POST, instance=estado)
        if formestado.is_valid():
            print("El form es valido")
            formestado.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )
        else:
            print("Hay errores: ", formestado.errors)

    data = {'formestado': formestado,
            'titulo': 'Editar Estado'
            }
    return render(request, 'ticketsApp/registroEstados.html', data)



def eliminarEstados(request,id):
    estado = Estado.objects.get(id = id)
    estado.delete()
    return HttpResponseRedirect(reverse('mostrarOpciones') )




def crearServicios(request):
    formservicio = forms.ServiciosForms()

    if request.method == 'POST':
        formservicio = forms.ServiciosForms(request.POST)
        if formservicio.is_valid():
            print("El formulario es valido")
            formservicio.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )

    data = {'formservicio': formservicio,
            'titulo': 'Crear Servicio'
            }
    return render(request, 'ticketsApp/registroServicios.html', data)


def editarServicios(request, id):
    servicio = Servicio.objects.get(id = id)
    formservicio = ServiciosForms(instance=servicio)
    if (request.method == 'POST'):
        formservicio = ServiciosForms(request.POST, instance=servicio)
        if formservicio.is_valid():
            print("El form es valido")
            formservicio.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )
        else:
            print("Hay errores: ", formservicio.errors)

    data = {'formservicio': formservicio,
            'titulo': 'Editar Servicio'
            }
    return render(request, 'ticketsApp/registroServicios.html', data)



def eliminarServicios(request,id):
    servicio = Servicio.objects.get(id = id)
    servicio.delete()
    return HttpResponseRedirect(reverse('mostrarOpciones') )




def crearTipos(request):
    formtipo = forms.TiposForms()

    if request.method == 'POST':
        formtipo = forms.TiposForms(request.POST)
        if formtipo.is_valid():
            print("El formulario es valido")
            formtipo.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )

    data = {'formtipo': formtipo,
            'titulo': 'Crear Tipo'
            }
    return render(request, 'ticketsApp/registroTipos.html', data)


def editarTipos(request, id):
    tipo = Tipo.objects.get(id = id)
    formtipo = TiposForms(instance=tipo)
    if (request.method == 'POST'):
        formtipo = TiposForms(request.POST, instance=tipo)
        if formtipo.is_valid():
            print("El form es valido")
            formtipo.save()
            return HttpResponseRedirect(reverse('mostrarOpciones') )
        else:
            print("Hay errores: ", formtipo.errors)

    data = {'formtipo': formtipo,
            'titulo': 'Editar Tipo'
            }
    return render(request, 'ticketsApp/registroTipos.html', data)



def eliminarTipos(request,id):
    tipo = Tipo.objects.get(id = id)
    tipo.delete()
    return HttpResponseRedirect(reverse('mostrarOpciones') )



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.success(request, ("Hubo un error, intentelo de nuevo"))
            return redirect('login')
        
    else:

            return render(request, 'registration/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("Cerro sesion correctamente"))
    return redirect('login_user')




def signUp(request):
    usuario = Usuario
    form = SingUpForm
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else: print(form.errors)

    return render(request, 'registration/registrar.html', {'form':form})


