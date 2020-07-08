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
import datetime

class ReporteForm(forms.ModelForm):
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = False)
	#municipio = forms.ModelChoiceField()
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
	eliminado = forms.IntegerField(required=False)
	fechaEditado=  forms.DateField(required=False,widget=forms.NumberInput(attrs={'class': 'form-control','type':'date'}))
	class Meta:
		model = Reporte
		fields =['estado','cantidadPruebas','cantidadPositivas','sospechosos','fechaTomada','fechaEditado','cantFemenino','cantMasculino','edadCero','edadDiez','edadVeinte','edadCuarenta','edadSesenta','edadOchenta','municipio','complemento','departamento','eliminado']
	
	def __init__(self, *args , **kwargs):
		super().__init__(*args , **kwargs)
		self.fields['municipio'].queryset = Municipio.objects.none()
		self.fields['municipio'].empty_label="Seleccione"
		self.fields['municipio'].widget.attrs.update({'class': 'form-control'})
		self.fields['municipio'].error_messages.update({'required': 'Llena el campo','invalid_choice':'Seleccione un Elemento ',})
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
		try:
			if cantidadPositivas > cantidadPruebas :
				raise ValidationError(_('%(value)s No puede ser mayor a Cantidad de pruebas realizadas'),params={'value': cantidadPositivas},)
		except(ValueError ,TypeError):
			pass
		return cantidadPositivas
	def clean_sospechosos(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		cantidadPruebas = self.cleaned_data.get('cantidadPruebas')
		sospechosos  = self.cleaned_data.get('sospechosos')
		try:
			diferencia =  cantidadPruebas-cantidadPositivas
			if sospechosos > cantidadPruebas :
				raise ValidationError(_('%(value)s No puede ser mayor a Cantidad de pruebas realizadas'),params={'value': sospechosos},)
			elif sospechosos > diferencia :
				raise ValidationError(_('%(value)s No puede ser mayor a: pruebas-positivos '),params={'value': sospechosos},)
		except(ValueError ,TypeError):
			pass 
		return sospechosos

	def clean_cantMasculino(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		cantMasculino = self.cleaned_data.get('cantMasculino')
		cantFemenino = self.cleaned_data.get('cantFemenino')
		try:
			sumadas = cantMasculino+cantFemenino
			if cantMasculino > cantidadPositivas :
				raise ValidationError(_('%(value)s No puede ser mayor a pruebas positivas'),params={'value': cantMasculino},)
			elif sumadas > cantidadPositivas :
				raise ValidationError(_('%(value)s La cant. femnenino y masculino No puede ser mayor a pruebas positivas'),params={'value': sumadas},)
			elif sumadas < cantidadPositivas :
				raise ValidationError(_('%(value)s La cant. femnenino y masculino No puede ser menor a pruebas positivas'),params={'value': sumadas},)
		except(ValueError ,TypeError):
			pass 
		return cantMasculino

	def clean_cantFemenino(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		cantFemenino = self.cleaned_data.get('cantFemenino')
		try:
			if cantFemenino > cantidadPositivas :
				raise ValidationError(_('%(value)s No puede ser mayor a pruebas positivas'),params={'value':cantFemenino},)
		except(ValueError ,TypeError):
			pass 
		return cantFemenino

	def clean_edadCero(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadCero= self.cleaned_data.get('edadCero')
		try:
			if edadCero >cantidadPositivas:
				raise ValidationError(_('%(value)s [0-9 años] No puede ser mayor a pruebas positivas'),params={'value':edadCero},)
		except(ValueError ,TypeError):
			pass
		return edadCero

	def clean_edadDiez(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadDiez= self.cleaned_data.get('edadDiez')
		try:
			if edadDiez > cantidadPositivas:
				raise ValidationError(_('%(value)s [10-19 años] No puede ser mayor a pruebas positivas'),params={'value':edadDiez},)
		except(ValueError ,TypeError):
			pass
		return edadDiez

	def clean_edadVeinte(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadVeinte= self.cleaned_data.get('edadVeinte')
		try:
			if edadVeinte >cantidadPositivas:
				raise ValidationError(_('%(value)s [20-39 años] No puede ser mayor a pruebas positivas'),params={'value':edadVeinte},)
		except(ValueError ,TypeError):
			pass
		return edadVeinte

	def clean_edadCuarenta(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadCuarenta= self.cleaned_data.get('edadCuarenta')
		try:
			if edadCuarenta >cantidadPositivas:
				raise ValidationError(_('%(value)s [40-59 años] No puede ser mayor a pruebas positivas'),params={'value':edadCuarenta},)
		except(ValueError ,TypeError):
			pass
		return edadCuarenta

	def clean_edadSesenta(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadSesenta= self.cleaned_data.get('edadSesenta')
		try:
			if edadSesenta >cantidadPositivas:
				raise ValidationError(_('%(value)s [60-79 años] No puede ser mayor a pruebas positivas'),params={'value':edadSesenta},)
		except(ValueError ,TypeError):
			pass
		return edadSesenta

	def clean_edadOchenta(self):
		cantidadPositivas = self.cleaned_data.get('cantidadPositivas')
		edadCero= self.cleaned_data.get('edadCero')
		edadDiez= self.cleaned_data.get('edadDiez')
		edadVeinte= self.cleaned_data.get('edadVeinte')
		edadCuarenta= self.cleaned_data.get('edadCuarenta')
		edadSesenta= self.cleaned_data.get('edadSesenta')
		edadOchenta= self.cleaned_data.get('edadOchenta')
		try:
			total = edadCero+edadDiez+edadVeinte+edadCuarenta+edadSesenta+edadOchenta
			if edadOchenta >cantidadPositivas:
				raise ValidationError(_('%(value)s [ >80 años] No puede ser mayor a pruebas positivas'),params={'value':edadOchenta},)
			
			elif total > cantidadPositivas:
				raise ValidationError(_('%(value)s La suma de todas las edades NO puede ser mayor a pruebas positivas'),params={'value':total},)
			elif total < cantidadPositivas:
				raise ValidationError(_('%(value)s Error en la suma de todas  las pruebas positias por grupo etario'),params={'value':total},)
		except(ValueError ,TypeError):
			pass
		return edadOchenta
	def clean_fechaTomada(self):
		fechaTomada= self.cleaned_data.get('fechaTomada')
		try:
			if fechaTomada> datetime.date.today():
				raise ValidationError(_('%(value)s Fecha invalida'),params={'value':fechaTomada},)
		except(ValueError,TypeError):
			pass
		return fechaTomada
	def clean_fechaEditado(self):
		fechaEditado=self.cleaned_data.get('fechaEditado')
		fechaEditado=datetime.date.today()
		return fechaEditado
	def clean_eliminado(self):
		eliminado=self.cleaned_data.get('eliminado')
		eliminado=0
		return eliminado