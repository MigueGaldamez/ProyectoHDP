import django_filters

from reportes.models import Reporte
from municipios.models import Municipio
from departamentos.models import Departamento
from perfiles.models import Perfil
from django.contrib.auth.models import User
from django import forms 
from doctores.models import Doctor

from django.db.models import Q 
class DoctorFilter(django_filters.FilterSet):
    perfil__nombre_c = django_filters.CharFilter(method='nombre_custom')
    perfil__apellido_c = django_filters.CharFilter(method='apellido_custom')
    correo_c = django_filters.CharFilter(method='correo_custom')
    nombre_usuario_c = django_filters.CharFilter(method='nombre_usuario_custom')
   
    class Meta:
        
        model = Doctor
       
        fields =['perfil__nombre_c','perfil__apellido_c','perfil__user__is_active' ,'correo_c','nombre_usuario_c']

    def nombre_custom(self, queryset, name, value):
        return Doctor.objects.filter(
            Q(perfil__nombre__icontains=value) )

    def apellido_custom(self, queryset, name, value):
        return Doctor.objects.filter(
            Q(perfil__apellido__icontains=value) )
    
    def correo_custom(self, queryset, name, value):
        return Doctor.objects.filter(
            Q(perfil__user__email__icontains=value) )
    
    def nombre_usuario_custom(self, queryset, name, value):
        return Doctor.objects.filter(
            Q(perfil__user__username__icontains=value) )
    

   
            
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(DoctorFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)

        self.filters['correo_c'].field.widget.attrs.update({'class': 'form-control form-control-sm' , 'placeholder':'Correo'})
        self.filters['nombre_usuario_c'].field.widget.attrs.update({'class': 'form-control form-control-sm' ,'placeholder':'Nombre usuario'})
        
        self.filters['perfil__nombre_c'].field.widget.attrs.update({'class': 'form-control form-control-sm' , 'placeholder':'Nombres'})
        self.filters['perfil__apellido_c'].field.widget.attrs.update({'class': 'form-control form-control-sm' ,'placeholder':'Apellidos'})
        self.filters['perfil__user__is_active'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
