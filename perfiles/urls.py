from django.conf.urls import url
from . import views
from django.urls import include,path
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns=[
	#links de seguidad
	path('',views.indexView,name="home"),
	path('dashboard/',views.dashboardView,name="dashboard"),
	path('login/',LoginView.as_view(),name="login_url"),
	path('register/',views.registerView, name="register_url"),
	path('logout/',LogoutView.as_view(next_page='/login/') , name ="logout"),
	path('ajax/cargar-municipios', views.cargar_municipios, name='ajax_cargar_municipios'),
	
] 