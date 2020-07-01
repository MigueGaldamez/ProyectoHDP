from django.contrib import admin

from .models import Reporte
from departamentos.models import Departamento
from municipios.models import Municipio
from perfiles.models import Perfil


admin.site.register(Reporte)
admin.site.register(Municipio)
admin.site.register(Perfil)