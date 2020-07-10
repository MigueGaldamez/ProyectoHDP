import json
from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from departamentos.models import Departamento
from municipios.models import Municipio
from reportes.models import Reporte
import datetime
from django.forms import ModelForm, Textarea, IntegerField
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuario','class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*******','class': 'form-control'}))


class UCFWithEmail(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuario','class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*******','class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*******','class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Correo Electronico','class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2","email"]

class UCFWithEmail_editar(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
   
    password1 = forms.CharField(required = False,widget=forms.PasswordInput(attrs={'placeholder':'*******','class': 'form-control'}))
    password2 = forms.CharField(required = False,widget=forms.PasswordInput(attrs={'placeholder':'*******','class': 'form-control'}))
    is_active = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Activo','class': 'form-control'}))

    class Meta:
        model = User
        fields = [ "password1", "password2","is_active"]

    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
       


class PerfilForm(forms.ModelForm):

	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = False)
	departamento.empty_label="Seleccione"
	departamento.widget.attrs.update({'class': 'form-control'})
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'nombre','class': 'form-control'}))
	tipoUsuario = forms.IntegerField(required=False)
	
	apellido =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellido','class': 'form-control'}))
	complemento = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Direccion','class': 'form-control'}))
	telefono =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefono','class': 'form-control'}))
	DUI = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'DUI','class': 'form-control'}))
	fechaNacimiento =forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))

	class Meta:
		model=Perfil
		fields =['departamento','municipio','nombre','apellido','complemento','telefono','DUI','fechaNacimiento']

	def __init__(self, *args , **kwargs):
		super().__init__(*args , **kwargs)
		self.fields['municipio'].queryset = Municipio.objects.none()
		self.fields['municipio'].empty_label="Seleccione"
		self.fields['municipio'].widget.attrs.update({'class': 'form-control'})
		self.fields['departamento'].queryset = Departamento.objects.order_by('nombre')
		if 'departamento' in self.data:
			try:
				departamento_id =int(self.data.get('departamento'))
				self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
				
			except(ValueError ,TypeError):
				pass 	
		
		elif self.instance.pk:
			self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('nombre')

class PerfilForm_editar(forms.ModelForm):
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = False)
	departamento.empty_label="Seleccione"
	departamento.widget.attrs.update({'class': 'form-control'})
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'nombre','class': 'form-control'}))
	tipoUsuario = forms.IntegerField(required=False)
	
	apellido =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apellido','class': 'form-control'}))
	complemento = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Direccion','class': 'form-control'}))
	telefono =forms.CharField(max_length=8,min_length=8, widget=forms.TextInput(attrs={'placeholder':'Telefono','class': 'form-control'}))
	DUI = forms.CharField(max_length=9,min_length=9,widget=forms.TextInput(attrs={'placeholder':'DUI','class': 'form-control'}))
	fechaNacimiento =forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))

	class Meta:
		model=Perfil
		fields =['departamento','municipio','nombre','apellido','complemento','telefono','DUI','fechaNacimiento']

	def __init__(self, *args , **kwargs):
		super().__init__(*args , **kwargs)
		self.fields['municipio'].queryset = Municipio.objects.none()
		self.fields['municipio'].empty_label="Seleccione"
		self.fields['municipio'].widget.attrs.update({'class': 'form-control'})
		self.fields['departamento'].queryset = Departamento.objects.order_by('nombre')
		#self.fields['DUI'].widget.attrs['disabled'] = True

		if 'departamento' in self.data:
			try:
				departamento_id =int(self.data.get('departamento'))
				self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
				
			except(ValueError ,TypeError):
				pass 	
		
		elif self.instance.pk:
			self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('nombre')
	def clean_telefono(self):
		telefono = self.cleaned_data.get('telefono')
		valor = False
		try:
			if telefono.isdigit():
				valor = False
			else:
				raise ValidationError(_('%(value)s ,No es un numero valido'),params={'value': telefono},)
			if telefono[0] != '6' and telefono[0] != '7' and telefono[0] != '2' :
				raise ValidationError(_('%(value)s ,No es un numero valido'),params={'value': telefono},)
		except(ValueError ,TypeError):
			pass 
		return telefono
	def clean_DUI(self):
		DUI = self.cleaned_data.get('DUI')
		try:
			if DUI.isdigit():
				valor = False
			else:
				raise ValidationError(_('%(value)s ,No es un DUI valido'),params={'value': DUI},)
			ultimo= DUI[8]
			contador=9
			suma=0
			valor = False
			for numero in DUI: #summador de los primeros 8 numeros del dui
				suma=suma+(int(numero)*contador)
				contador=contador-1
			suma=suma - (int(ultimo)*1)
			verificador = 10 - suma%10
			if verificador != 0 and verificador != int(ultimo):#verifica el verificador es el ultimo numero del dui o es 0
				raise ValidationError(_('%(value)s ,No es un DUI valido'),params={'value': DUI},)
		except(ValueError ,TypeError):
			pass
		return DUI
	def clean_fechaNacimiento(self):
		fechaNacimiento= self.cleaned_data.get('fechaNacimiento')
		try:
			hoy= datetime.date.today()
			"""primero restamos los años y luego restamos la comparación entre mes 
			y día actual y mes y día de nacimiento. Si la combianción mes/día de
			hoy es anterior a la combinación mes/día de nacimiento la comparación devuelve 1, si no devuelve 0."""
			edad = hoy.year - fechaNacimiento.year - ((hoy.month, hoy.day) < (fechaNacimiento.month, fechaNacimiento.day))
			if(edad<23):
				print(edad)
				raise ValidationError(_('%(value)s años, ¿ y eres  doctor?'),params={'value': edad},)
		except(ValueError ,TypeError):
			pass 
		return fechaNacimiento