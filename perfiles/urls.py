from django.conf.urls import url
from . import views
from django.urls import include,path
from django.contrib.auth.views import LoginView,LogoutView
from perfiles.forms import UserLoginForm
from django.contrib.auth import views as auth_views
from .views import perfilView,editar_perfil




urlpatterns=[
	#links de seguidad
	#path('',ClubChartView.as_view(),name="home")
	path('',views.indexView,name="home"),
	path('dashboard/',views.dashboardView,name="dashboard"),
	path('login/',LoginView.as_view( template_name="registration/login.html",authentication_form=UserLoginForm),name="login"),
	path('register/',views.registerView, name="register_url"),
	path('logout/',LogoutView.as_view(next_page='/login/') , name ="logout"),
	path('ajax/cargar-municipios', views.cargar_municipios, name='ajax_cargar_municipios'),
	path('perfil/',views.perfilView , name ="perfilview"),#ver perfil
	path('perfil/editar/',views.editar_perfil , name ="editar_perfil"),#editar perfil
 
    path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_change_done'),
	path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
	path('password_reset/done/' , auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

    path('dashboard/permisos/update/<int:id>', views.verDoctorPermiso , name ="actualizar_permisos"),
	path('dashboard/permisos/', views.permisosView , name ="permisos"),
	path('fechas_resumen', views.fechas_resumen , name ="fechas_resumen"),
	path('fechas_resumen_muni/<int:id>', views.fechas_resumen_muni , name ="fechas_resumen_muni"),
	path('departamentos_resumen', views.departamentos_resumen , name ="departamentos_resumen"),
	path('genero_resumen', views.genero_resumen , name ="genero_resumen"),
	path('edades_resumen', views.edades_resumen , name ="edades_resumen"),
	path('edades_resumen_muni/<int:id>', views.edades_resumen_muni , name ="edades_resumen_muni"),
	path('dep1_resumen/<int:id>', views.dep1_resumen , name ="dep1_resumen"),
	
	
	
] 