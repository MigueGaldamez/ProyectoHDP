from django import forms
from .models import Municipio,Departamento

class MunicipioForm(forms.ModelForm):
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), initial=0)
	class Meta:
		model = Municipio
		fields =['idDepartamento','nombreMunicipio','departamento']

class DepartamentoForm(forms.ModelForm):
	class Meta:
		model = Departamento
		fields =['nombreDepartamento']