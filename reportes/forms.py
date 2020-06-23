import json
from django import forms
from .models import Reporte,Municipio,Departamento



class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields =['nombre']

class MunicipioForm(forms.ModelForm):
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = True)
	class Meta:
		model = Municipio
		fields =['nombre','departamento']

class ReporteForm(forms.ModelForm):

	municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), required = True)
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = True)
	class Meta:
		model = Reporte
		fields =['cantidadPruebas','cantidadPositivas','municipio','departamento']
	