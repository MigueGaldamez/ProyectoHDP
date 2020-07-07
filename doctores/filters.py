import django_filters

from .models import Reporte
from municipios.models import Municipio
from departamentos.models import Departamento
from django import forms 

class DoctorFilter(django_filters.FilterSet):
   
    class Meta:
        fechaEditado = django_filters.DateFilter()
        model = Reporte
        fields =['fechaTomada','fechaEditado','municipio','complemento','departamento','eliminado']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(ReporteFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['eliminado'].field.widget.attrs.update({'class': 'form-control form-control-sm, d-none'})
        self.filters['departamento'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
      
        self.filters['departamento'].field.empty_label="Seleccione"
        self.filters['municipio'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
        self.filters['complemento'].field.widget.attrs.update({'class': 'form-control form-control-sm','placeholder':'direccion'})
        self.filters['municipio'].field.queryset = Municipio.objects.none()
        self.filters['municipio'].field.empty_label="Seleccione"
        self.filters['fechaEditado'].field.widget.attrs.update({'class': 'form-control form-control-sm' ,'type':'date'})
        

        if 'departamento' in self.data:
            try:

                departamento_id =int(self.data.get('departamento'))
                self.filters['municipio'].field.queryset = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
			
            except(ValueError ,TypeError):
                pass 	
		
        #elif self.field.instance.pk:
            #self.filter['municipio'].field.queryset = self.field.instance.departamento.municipio_set.order_by('nombre')