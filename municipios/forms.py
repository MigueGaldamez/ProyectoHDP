from django import forms
from .models import Municipio

class MunicipioForm(forms.ModelForm):
	class Meta:
		model = Municipio
		fields =['idDepartamento','nombreMunicipio']