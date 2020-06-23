from django.urls import path
from .views import listar_municipios, crear_municipio,actualizar_municipio, eliminar_municipio,listar_departamentos,crear_departamento,actualizar_departamento, eliminar_departamento

urlpatterns=[
	path('municipios/',listar_municipios,name='listar_municipios'),
	path('municipios/new',crear_municipio, name='crear_municipio'),
	path('municipios/update/<int:id>',actualizar_municipio, name='actualizar_municipio'),
	path('municipios/delete/<int:id>',eliminar_municipio,name='eliminar_municipio'),
	
	path('',listar_departamentos,name='listar_departamentos'),
	path('new',crear_departamento, name='crear_departamento'),
	path('update/<int:id>',actualizar_departamento, name='actualizar_departamento'),
	path('delete/<int:id>',eliminar_departamento,name='eliminar_departamento'),
] 