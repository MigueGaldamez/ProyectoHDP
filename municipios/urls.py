from django.urls import path
from .views import listar_municipios, crear_municipio,actualizar_municipio, eliminar_municipio

urlpatterns=[
	path('',listar_municipios,name='listar_municipios'),
	path('new',crear_municipio, name='crear_municipio'),
	path('update/<int:id>',actualizar_municipio, name='actualizar_municipio'),
	path('delete/<int:id>',eliminar_municipio,name='eliminar_municipio'),
] 