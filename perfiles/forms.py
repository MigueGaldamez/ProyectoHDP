import json
from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from departamentos.models import Departamento
from municipios.models import Municipio
from reportes.models import Reporte

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

		if 'departamento' in self.data:
			try:
				departamento_id =int(self.data.get('departamento'))
				self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
				
			except(ValueError ,TypeError):
				pass 	
		
		elif self.instance.pk:
			self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('nombre')

