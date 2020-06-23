from django.urls import path
from .views import listar_reportes, crear_reporte, actualizar_reporte, eliminar_reporte

urlpatterns=[
	path('',listar_reportes,name='listar_reportes'),
	path('new',crear_reporte, name='crear_reporte'),
	path('update/<int:id>',actualizar_reporte, name='actualizar_reporte'),
	path('delete/<int:id>',eliminar_reporte,name='eliminar_reporte'),
] 