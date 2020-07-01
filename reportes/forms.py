import json
from django import forms 
from .models import Reporte
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from departamentos.models import Departamento
from municipios.models import Municipio
from perfiles.models import Perfil

#chepe
from django.forms import ModelForm, Textarea, IntegerField
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ReporteForm(forms.ModelForm):
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = False)
	#municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), required = False)
	departamento.empty_label="Seleccione"
	requerido = "Ingrese un Dato: "
	departamento.widget.attrs.update({'class': 'form-control'})
	
	cantidadPruebas = forms.IntegerField(min_value=0,error_messages={'required': requerido +"Pruebas realizadas",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	cantidadPositivas = forms.IntegerField(min_value=0,error_messages={'required': requerido+"Positivas",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	sospechosos = forms.IntegerField(min_value=0,error_messages={'required': requerido+"Sospechosos",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	fechaTomada = forms.DateField(error_messages={'required': requerido+"Fecha Tomada"},widget=forms.NumberInput(attrs={'class': 'form-control','type':'date'}))
	cantFemenino = forms.IntegerField(min_value=0,error_messages={'required': requerido+"Femnenino",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	cantMasculino = forms.IntegerField(min_value=0,error_messages={'required': requerido+"Masculino",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	edadCero = forms.IntegerField(min_value=0,error_messages={'required': requerido+"0-9",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	edadDiez = forms.IntegerField(min_value=0,error_messages={'required': requerido+"10-19",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	edadVeinte =  forms.IntegerField(min_value=0,error_messages={'required': requerido+"20-39",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	edadCuarenta = forms.IntegerField(min_value=0,error_messages={'required': requerido+"40-59",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	edadSesenta = forms.IntegerField(min_value=0,error_messages={'required': requerido+"60-79",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	edadOchenta = forms.IntegerField(min_value=0,error_messages={'required': requerido+"Mayores de 80",'min_value':'Ingrese # Positivo'},widget=forms.NumberInput(attrs={'class': 'form-control'}))
	complemento = forms.CharField(error_messages={'required': requerido+"Complemento de direccion"},widget=forms.TextInput(attrs={'class': 'form-control'}))
	estado = forms.IntegerField(required=False)
	class Meta:
		model = Reporte
		fields =['cantidadPruebas','cantidadPositivas','sospechosos','fechaTomada','cantFemenino','cantMasculino','edadCero','edadDiez','edadVeinte','edadCuarenta','edadSesenta','edadOchenta','municipio','complemento','departamento']
	
	def __init__(self, *args , **kwargs):
		super().__init__(*args , **kwargs)
		self.fields['municipio'].queryset = Municipio.objects.none()
		self.fields['municipio'].empty_label="Seleccione"
		self.fields['municipio'].widget.attrs.update({'class': 'form-control'})
		self.fields['municipio'].error_messages.update({'required': 'Llena el campo',})
		if 'departamento' in self.data:
			try:

				departamento_id =int(self.data.get('departamento'))
				self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
			
			except(ValueError ,TypeError):
				pass 	
		
		elif self.instance.pk:
			self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('nombre')
	def clean_cantidadPositivas(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		cantidadPruebas = self.cleaned_data.get('cantidadPruebas')
		if cantidadPositivas > cantidadPruebas :
			raise ValidationError(_('%(value)s No puede ser mayor a Cantidad de pruebas realizadas'),params={'value': cantidadPositivas},)
		return cantidadPositivas
	def clean_sospechosos(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		cantidadPruebas = self.cleaned_data.get('cantidadPruebas')
		sospechosos  = self.cleaned_data.get('sospechosos')
		diferencia =  cantidadPruebas-cantidadPositivas
		if sospechosos > cantidadPruebas :
			raise ValidationError(_('%(value)s No puede ser mayor a Cantidad de pruebas realizadas'),params={'value': sospechosos},)
		elif sospechosos > diferencia :
			raise ValidationError(_('%(value)s No puede ser mayor [pruebas-positivos]'),params={'value': sospechosos},)
		return sospechosos

	def clean_cantMasculino(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		cantMasculino = self.cleaned_data.get('cantMasculino')
		cantFemenino = self.cleaned_data.get('cantFemenino')
		sumadas = cantMasculino+cantFemenino
		if cantMasculino > cantidadPositivas :
			raise ValidationError(_('%(value)s No puede ser mayor a pruebas positivas'),params={'value': cantMasculino},)
		elif sumadas > cantidadPositivas :
			raise ValidationError(_('%(value)s La cant. femnenino y masculino No puede ser mayor a pruebas positivas'),params={'value': sumadas},)
		return cantMasculino

	def clean_cantFemenino(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		cantFemenino = self.cleaned_data.get('cantFemenino')
		if cantFemenino > cantidadPositivas :
			raise ValidationError(_('%(value)s No puede ser mayor a pruebas positivas'),params={'value':cantFemenino},)
		return cantFemenino
""" Work in Progress xddd 
	def clean_edadCero(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadCero= self.cleaned_data.get('edadCero')
		return edadCero

	def clean_edadDiez(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadDiez= self.cleaned_data.get('edadDiez')
		return edadDiez

	def clean_edadVeinte(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadVeinte= self.cleaned_data.get('edadVeinte')
		return edadVeinte

	def clean_edadCuarenta(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadCuarenta= self.cleaned_data.get('edadCuarenta')
		return edadCuarenta

	def clean_edadSesenta(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadSesenta= self.cleaned_data.get('edadSesenta')
		return edadSesenta

	def clean_edadOchenta(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadOchenta= self.cleaned_data.get('edadOchenta')
		return edadOchenta
     """