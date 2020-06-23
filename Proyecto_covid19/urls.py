from django.contrib import admin  
from django.urls import path ,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [  
    path('reportes/',include('reportes.urls')), 
    path('admin/', admin.site.urls),  
  
]  

urlpatterns += staticfiles_urlpatterns()