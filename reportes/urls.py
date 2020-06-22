from django.urls import path
from .views import listar_reportes, crear_reporte, update_reporte, delete_reporte

urlpatterns=[
	path('',listar_reportes,name='listar_reportes'),
	path('new',crear_reporte, name='crear_reporte'),
	path('update/<int:id>',update_reporte, name='update_reporte'),
	path('delete/<int:id>',delete_reporte,name='delete_reporte'),
] 