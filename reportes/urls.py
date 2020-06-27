from django.conf.urls import url
from . import views
from django.urls import include,path
from .views import listar_reportes, crear_reporte, actualizar_reporte, eliminar_reporte,listar_municipios, crear_municipio,actualizar_municipio, eliminar_municipio,listar_departamentos,crear_departamento,actualizar_departamento, eliminar_departamento

urlpatterns=[
	path('',listar_reportes,name='listar_reportes'),
	path('new',crear_reporte, name='crear_reporte'),
	path('update/<int:id>',actualizar_reporte, name='actualizar_reporte'),
	path('delete/<int:id>',eliminar_reporte,name='eliminar_reporte'),
	path('ajax/cargar-municipios', views.cargar_municipios, name='ajax_cargar_municipios'),

	path('municipios/',listar_municipios,name='listar_municipios'),
	path('municipios/new',crear_municipio, name='crear_municipio'),
	path('municipios/update/<int:id>',actualizar_municipio, name='actualizar_municipio'),
	path('municipios/delete/<int:id>',eliminar_municipio,name='eliminar_municipio'),
	
	path('departamentos/',listar_departamentos,name='listar_departamentos'),
	path('departamentos/new',crear_departamento, name='crear_departamento'),
	path('departamentos/update/<int:id>',actualizar_departamento, name='actualizar_departamento'),
	path('departamentos/delete/<int:id>',eliminar_departamento,name='eliminar_departamento'),
] 