from django.conf.urls import url
from . import views
from django.urls import include,path
from django.contrib.auth.views import LoginView,LogoutView
from .views import listar_doctores, crear_doctor,actualizar_doctor, eliminar_doctor

urlpatterns=[
	#links de seguidad
	path('',listar_doctores,name='listar_doctores'),
	path('new',crear_doctor, name='crear_doctor'),
	path('update/<int:id>',actualizar_doctor, name='actualizar_doctor'),
	path('delete/<int:id>',eliminar_doctor,name='eliminar_doctor'),
	
] 