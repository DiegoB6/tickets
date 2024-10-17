from django import forms 

from ticketsApp.models import *

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Usuario

class TicketsForm(forms.Form):

    telefono = forms.CharField(label='Telefono', max_length=15)
    correo = forms.CharField(label='Correo',max_length=50)
    nombre = forms.CharField(label='Nombre',max_length=50)
    rut = forms.CharField(label='Rut',max_length=20)
    detalle = forms.CharField(label='Detalle',max_length=100)
    observacion = forms.CharField(label='Observacion',max_length=100)
    servicio = forms.ModelChoiceField(queryset=Servicio.objects.all())
    trabajador = forms.ModelChoiceField(queryset=Trabajador.objects.all())
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.all())
    criticidad = forms.ModelChoiceField(queryset=Criticidad.objects.all())
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())
    area = forms.ModelChoiceField(queryset=Area.objects.all())


class TicketsForm(forms.ModelForm):

    telefono = forms.CharField(label='Telefono', max_length=15)
    correo = forms.CharField(label='Correo',max_length=50)
    nombre = forms.CharField(label='Nombre',max_length=50)
    rut = forms.CharField(label='Rut',max_length=20)
    detalle = forms.CharField(label='Detalle',max_length=100)
    observacion = forms.CharField(label='Observacion',max_length=100)
    servicio = forms.ModelChoiceField(queryset=Servicio.objects.all())
    trabajador = forms.ModelChoiceField(queryset=Trabajador.objects.all())
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.all())
    criticidad = forms.ModelChoiceField(queryset=Criticidad.objects.all())
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())
    area = forms.ModelChoiceField(queryset=Area.objects.all())

    class Meta:
        model = Ticket
        fields= '__all__'





class AreasForms(forms.Form):
    area = forms.CharField(label='Area', max_length=25)


class AreasForms(forms.ModelForm):
    area = forms.CharField(label='Area', max_length=25)

    class Meta:
        model = Area
        fields= '__all__'



class CriticidadesForms(forms.Form):
    criticidad = forms.CharField(label='Criticidad', max_length=25)


class CriticidadesForms(forms.ModelForm):
    criticidad = forms.CharField(label='Criticidad', max_length=25)
    class Meta:
        model = Criticidad
        fields= '__all__'



class EstadosForms(forms.Form):
    estado = forms.CharField(label='Estado', max_length=25)


class EstadosForms(forms.ModelForm):
    estado = forms.CharField(label='Estado', max_length=25)
    class Meta:
        model = Estado
        fields= '__all__'



class ServiciosForms(forms.Form):
    servicio = forms.CharField(label='Servicio', max_length=25)


class ServiciosForms(forms.ModelForm):
    servicio = forms.CharField(label='Servicio', max_length=25)
    class Meta:
        model = Servicio
        fields= '__all__'



class TiposForms(forms.Form):
    tipo = forms.CharField(label='Tipo', max_length=25)


class TiposForms(forms.ModelForm):
    tipo = forms.CharField(label='Tipo', max_length=25)
    class Meta:
        model = Tipo
        fields= '__all__'



class SingUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')