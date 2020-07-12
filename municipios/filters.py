import django_filters
from .models import Municipio
from departamentos.models import Departamento

class MunicipioFilter(django_filters.FilterSet):
   
    class Meta:
       
        model = Municipio
        fields =['departamento']

    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(MunicipioFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['departamento'].field.widget.attrs.update({'class': 'form-control form-control-sm'})
      
        self.filters['departamento'].field.empty_label="Seleccione"
        


    