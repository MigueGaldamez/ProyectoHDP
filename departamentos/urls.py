from django.conf.urls import url
from . import views
from django.urls import include,path
from django.contrib.auth.views import LoginView,LogoutView
from .views import listar_departamentos,crear_departamento,actualizar_departamento, eliminar_departamento

urlpatterns=[
	#links de seguidad
	
	path('',listar_departamentos,name='listar_departamentos'),
	path('new',crear_departamento, name='crear_departamento'),
	path('update/<int:id>',actualizar_departamento, name='actualizar_departamento'),
	path('delete/<int:id>',eliminar_departamento,name='eliminar_departamento'),
] 