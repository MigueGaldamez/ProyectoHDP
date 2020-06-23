from django.contrib import admin  
from django.urls import path ,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [  
    path('reportes/',include('reportes.urls')), 
    path('admin/', admin.site.urls),  
    path('municipios/',include('municipios.urls')), 
    path('departamentos/',include('departamentos.urls')),

    
]  

urlpatterns += staticfiles_urlpatterns()