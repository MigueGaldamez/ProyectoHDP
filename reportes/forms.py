import json
from django import forms
from .models import Reporte,Municipio,Departamento
from django.forms import ModelForm, Textarea, IntegerField
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
		widgets = {
            'cantidadPruebas': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidadPositivas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
	def __init__(self, *args , **kwargs):
		super().__init__(*args , **kwargs)
		self.fields['municipio'].queryset = Municipio.objects.none()
		self.fields['municipio'].empty_label="Seleccione"
		self.fields['departamento'].empty_label="Seleccione"
		self.fields['municipio'].widget.attrs.update({'class': 'form-control'})
		self.fields['departamento'].widget.attrs.update({'class': 'form-control'})
		if 'departamento' in self.data:
			try:
				departamento_id =int(self.data.get('departamento'))
				self.fields['municipio'].queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
			except(ValueError ,TypeError):
				pass 	
		
		elif self.instance.pk:
			self.fields['municipio'].queryset = self.instance.departamento.municipio_set.order_by('nombre')




