import json
from django import forms
from .models import Doctor
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class DoctorForm(forms.ModelForm):
	especialidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Especialidad','class': 'form-control'}))
	codigoDoctor = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Codigo Medico','class': 'form-control'}))
	institucionTrabajo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Institucion ','class': 'form-control'}))
	
	class Meta:
		model = Doctor
		fields =['especialidad','codigoDoctor','institucionTrabajo']
	def clean_codigoDoctor(self):
		codigoDoctor= self.cleaned_data.get('codigoDoctor')
		valor = False
		try:
			if codigoDoctor.isdigit():
				valor = False
			else: 
				raise ValidationError(_('%(value)s ,Ingrrese un numero valido'),params={'value': codigoDoctor},)
		except(ValueError,TypeError):
			pass
		return codigoDoctor

