import json
from django import forms
from .models import Municipio
from departamentos.models import Departamento


class MunicipioForm(forms.ModelForm):
	departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), required = True)
	class Meta:
		model = Municipio
		fields =['nombre','departamento']

