import json
from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from departamentos.models import Departamento
from municipios.models import Municipio
from reportes.models import Reporte


class UCFWithEmail(UserCreationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Correo Electronico'}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2","email"]


class PerfilForm(forms.ModelForm):
	class Meta:
		model=Perfil
		fields =['departamento','municipio','nombre']

	def __init__(self, *args , **kwargs):
		super().__init__(*args , **kwargs)
		self.fields['municipio'].queryset = Municipio.objects.none()

		if 'departamento' in self.data:
			try:
				departamento_id =int(self.data.get('departamento'))
				self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
			except(ValueError ,TypeError):
				pass 	
		
		elif self.instance.pk:
			self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('nombre')

