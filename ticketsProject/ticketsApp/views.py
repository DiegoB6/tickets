from django.shortcuts import render, redirect

from ticketsApp.models import *
from ticketsApp.forms import *

from . import forms

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

""" from .models import Usuario """
from .forms import SingUpForm
from .forms import CrearStuff

from django.db.models import Q
# Create your views here.


def mostrarTickets(request):
    ticket_id = request.GET.get('ticket_id')

    # Filtrar tickets según el ID proporcionado o traer todos si no hay filtro
    if ticket_id:
        # Filtrar por ID si se proporciona un ID específico
        tickets = Ticket.objects.filter(id=ticket_id)
    else:
        # Si no se proporciona un ID, mostrar todos los tickets
        tickets = Ticket.objects.all()
    data = {'tickets': tickets,
            'titulo': 'Lista de personas'
    }
    return render (request, 'ticketsApp/mostrarTickets.html', data)


def opcionesEjecutivo(request):
    Tickets = Ticket.objects.all()
    data = {'tickets': Tickets,
            'titulo': 'Lista de personas'
    }
    return render (request, 'ticketsApp/opcionesEjecutivo.html', data)



def crear_ticket(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        ticket_form = TicketForm(request.POST)
        
        if usuario_form.is_valid() and ticket_form.is_valid():
            usuario = usuario_form.save()  # Guardar el usuario
            ticket = ticket_form.save(commit=False)
            ticket.usuario = usuario  # Asignar el usuario al ticket
            ticket.save()  # Guardar el ticket
            return redirect('mostrarTickets')
    else:
        usuario_form = UsuarioForm()
        ticket_form = TicketForm()
    
    return render(request, 'ticketsApp/registroTickets.html', {
        'usuario_form': usuario_form,
        'ticket_form': ticket_form,
        'titulo': 'Crear ticket'
    })



def crear_ticket_con_usuario(request):
    if request.method == 'POST':
        formV2 = TicketConUsuarioForm(request.POST)
        if formV2.is_valid():
            formV2.save()
            return redirect('mostrarTickets')
    else:
        formV2 = TicketConUsuarioForm()
        usuarios = Usuario.objects.all()  # Todos los usuarios para JS

    return render(request, 'ticketsApp/registroTicketConUsuario.html', {
        'form': formV2,
        'usuarios': usuarios,
        'titulo': 'Crear ticket'
    })




""" def editarTicket(request, id):
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
    return render(request, 'ticketsApp/registroTickets.html', data) """



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



def opcionesJefe(request):
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
    return render (request, 'ticketsApp/opcionesJefe.html', data)




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

            if user.is_superuser:
                return redirect('home')
            elif user.is_staff:
                return redirect('homeJefe')
            else:
                return redirect('homeEjecutivo')

        else:
            messages.success(request, ("Hubo un error, intentelo de nuevo"))
            return redirect('login')
        
    else:

            return render(request, 'registration/login.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, ("Cerro sesion correctamente"))
    return redirect('login_user')




""" def signUp(request):
    usuario = Usuario
    form = SingUpForm
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else: print(form.errors)

    return render(request, 'registration/registrar.html', {'form':form}) """



def registrarStaff(request):
    if request.method == 'POST':
        form = CrearStuff(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')  # Redirige a una página después de crear el usuario
    else:
        
        form = CrearStuff()
        print(form.errors)
    return render(request, 'registration/registrarStaff.html', {'form': form})


def registrarEjecutivo(request):
    if request.method == 'POST':
        form = CrearEjecutivo(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Esto encripta la contraseña
            user.save()
            return redirect('login_user') 
    else:
        form = CrearEjecutivo()
    return render(request, 'registration/registrarEjecutivo.html', {'form': form})


from django.shortcuts import render, get_object_or_404



from django.http import JsonResponse
from .models import Usuario

def usuario_data(request, rut):
    usuario = get_object_or_404(Usuario, rut=rut)
    data = {
        "telefono": usuario.telefono,
        "correo": usuario.correo,
        "nombre": usuario.nombre,
    }
    return JsonResponse(data)



def editarTicket(request, id):
    # Obtener el ticket por ID y el usuario asociado
    ticket = get_object_or_404(Ticket, id=id)
    usuario = ticket.usuario  # Suponiendo que `Ticket` tiene una relación con `Usuario`
    
    # Cargar ambos formularios con los datos actuales
    ticket_form = TicketForm(instance=ticket)
    usuario_form = UsuarioForm(instance=usuario)

    if request.method == 'POST':
        # Rellenar los formularios con los datos del POST
        ticket_form = TicketForm(request.POST, instance=ticket)
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        
        # Validar y guardar ambos formularios
        if ticket_form.is_valid() and usuario_form.is_valid():
            ticket_form.save()
            usuario_form.save()
            print("El form es válido y se ha guardado.")
            return HttpResponseRedirect(reverse('mostrarTickets'))
        else:
            print("Hay errores: ", ticket_form.errors, usuario_form.errors)

    # Enviar ambos formularios al template
    data = {
        'ticket_form': ticket_form,
        'usuario_form': usuario_form,
        'titulo': 'Editar Ticket'
    }
    return render(request, 'ticketsApp/registroTickets.html', data)



def registroTEjecutivo(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        ticket_form = TicketForm(request.POST)
        
        if usuario_form.is_valid() and ticket_form.is_valid():
            usuario = usuario_form.save()  # Guardar el usuario
            ticket = ticket_form.save(commit=False)
            ticket.usuario = usuario  # Asignar el usuario al ticket
            ticket.save()  # Guardar el ticket
            return redirect('mostrarTickets')
    else:
        usuario_form = UsuarioForm()
        ticket_form = TicketForm()
    
    return render(request, 'ticketsApp/registroTEjecutivo.html', {
        'usuario_form': usuario_form,
        'ticket_form': ticket_form,
        'titulo': 'Crear ticket'
    })


def registroTUsuarioEjecutivo(request):
    if request.method == 'POST':
        formV2 = TicketConUsuarioForm(request.POST)
        if formV2.is_valid():
            formV2.save()
            return redirect('mostrarTickets')
    else:
        formV2 = TicketConUsuarioForm()
        usuarios = Usuario.objects.all()  # Todos los usuarios para JS

    return render(request, 'ticketsApp/registroTUsuarioEjecutivo.html', {
        'form': formV2,
        'usuarios': usuarios,
        'titulo': 'Crear ticket'
    })
