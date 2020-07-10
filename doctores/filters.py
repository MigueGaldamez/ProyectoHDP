import django_filters

from reportes.models import Reporte
from municipios.models import Municipio
from departamentos.models import Departamento
from perfiles.models import Perfil
from django.contrib.auth.models import User
from django import forms 
from .models import Doctor

class DoctorFilter(django_filters.FilterSet):
   
    class Meta:
       
        model = Doctor
        fields =['perfil__nombre','perfil__apellido','perfil__municipio','perfil__complemento','perfil__departamento','perfil__user__is_active']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(DoctorFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['perfil__departamento'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
      
        self.filters['perfil__departamento'].field.empty_label="Seleccione"
        self.filters['perfil__municipio'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
        self.filters['perfil__nombre'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
        self.filters['perfil__apellido'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
        self.filters['perfil__complemento'].field.widget.attrs.update({'class': 'form-control form-control-sm','placeholder':'direccion'})
        self.filters['perfil__municipio'].field.queryset = Municipio.objects.none()
        self.filters['perfil__municipio'].field.empty_label="Seleccione"
        self.filters['perfil__user__is_active'].field.widget.attrs.update({'class': 'form-control form-control-sm'})

        if 'perfil__departamento' in self.data:
            try:

                departamento_id =int(self.data.get('perfil__departamento'))
                self.filters['perfil__municipio'].field.queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
			
            except(ValueError ,TypeError):
                pass 	
		
        #elif self.field.instance.pk:
            #self.filter['municipio'].field.queryset = self.field.instance.departamento.municipio_set.order_by('nombre')