from django.conf.urls import url
from . import views
from django.urls import include,path
from django.contrib.auth.views import LoginView,LogoutView

from .views import listar_reportes, crear_reporte, actualizar_reporte, eliminar_reporte

urlpatterns=[
	#links de seguidad	
	path('',listar_reportes,name='listar_reportes'),
	path('new',crear_reporte, name='crear_reporte'),
	path('update/<int:id>',actualizar_reporte, name='actualizar_reporte'),
	path('delete/<int:id>',eliminar_reporte,name='eliminar_reporte'),
	path('ajax/cargar-municipios', views.cargar_municipios, name='ajax_cargar_municipios'),
	
	
	
] 