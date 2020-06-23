from django.contrib import admin

# Register your models here.
from .models import Municipio , Departamento

admin.site.register(Municipio)
admin.site.register(Departamento)