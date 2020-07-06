import json
from django import forms
from .models import Doctor



class DoctorForm(forms.ModelForm):
	especialidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Especialidad','class': 'form-control'}))
	codigoDoctor = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Codigo Medico','class': 'form-control'}))
	institucionTrabajo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Institucion ','class': 'form-control'}))
	
	class Meta:
		model = Doctor
		fields =['especialidad','codigoDoctor','institucionTrabajo'] 

