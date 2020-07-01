from django.conf.urls import url
from . import views
from django.urls import include,path
from django.contrib.auth.views import LoginView,LogoutView
from .views import listar_municipios, crear_municipio,actualizar_municipio, eliminar_municipio

urlpatterns=[
	#links de seguidad
	path('',listar_municipios,name='listar_municipios'),
	path('new',crear_municipio, name='crear_municipio'),
	path('update/<int:id>',actualizar_municipio, name='actualizar_municipio'),
	path('delete/<int:id>',eliminar_municipio,name='eliminar_municipio'),
	
] 