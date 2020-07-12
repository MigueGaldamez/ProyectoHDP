import django_filters

from reportes.models import Reporte
from municipios.models import Municipio
from departamentos.models import Departamento
from perfiles.models import Perfil
from django.contrib.auth.models import User
from django import forms 
from .models import Doctor

from django.db.models import Q 
class DoctorFilter(django_filters.FilterSet):
    perfil__nombre_c = django_filters.CharFilter(method='nombre_custom')
    perfil__apellido_c = django_filters.CharFilter(method='apellido_custom')
    perfil__complemento_c = django_filters.CharFilter(method='complemento_custom')
    class Meta:
        
        model = Doctor
       
        fields =['perfil__nombre_c','perfil__apellido_c','perfil__municipio','perfil__complemento_c','perfil__departamento','perfil__user__is_active']

    def nombre_custom(self, queryset, name, value):
        return Doctor.objects.filter(
            Q(perfil__nombre__icontains=value) )

    def apellido_custom(self, queryset, name, value):
        return Doctor.objects.filter(
            Q(perfil__apellido__icontains=value) )

    def complemento_custom(self, queryset, name, value):
        return Doctor.objects.filter(
            Q(perfil__complemento__icontains=value) )
    
    
            
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(DoctorFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['perfil__departamento'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
      
        self.filters['perfil__departamento'].field.empty_label="Seleccione"
        self.filters['perfil__municipio'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
        self.filters['perfil__nombre_c'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
        self.filters['perfil__apellido_c'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
        self.filters['perfil__complemento_c'].field.widget.attrs.update({'class': 'form-control form-control-sm','placeholder':'direccion'})
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