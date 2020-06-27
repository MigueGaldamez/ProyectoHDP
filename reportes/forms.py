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

	class Meta:
		model = Reporte
		fields =['cantidadPruebas','cantidadPositivas','departamento','municipio']
	
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


