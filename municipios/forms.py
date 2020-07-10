import json
from django import forms
from .models import Municipio
from departamentos.models import Departamento


class MunicipioForm(forms.ModelForm):
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = True)
	departamento.empty_label="Seleccione"
	departamento.widget.attrs.update({'class': 'form-control'})
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nombre Municipio','class': 'form-control'}))
	class Meta:
		model = Municipio
		fields =['nombre','departamento']

