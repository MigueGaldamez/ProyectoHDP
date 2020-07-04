from django.shortcuts import render ,redirect
from .models import Perfil
from .forms import PerfilForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UCFWithEmail
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
#imports
from departamentos.forms import DepartamentoForm
from departamentos.models import Departamento
from municipios.models import Municipio
from municipios.forms import  MunicipioForm
from reportes.models import Reporte
from reportes.forms import ReporteForm
from doctores.forms import DoctorForm
from doctores.models import Doctor

from django.http import JsonResponse

from django.db.models import Sum


def get_data(request,*args,**kwargs):
	data ={
		"sales":100,
		"customers":10,
	}
	return JsonResponse()

# Create your views here.

#VIEWS DE SEGURIDAD
def perfilView(request):
	perfil = 0
	doctor = 0
	if request.user.is_authenticated:
		perfil = Perfil.objects.get(user_id=request.user.id)
		if perfil.tipoUsuario == 0:
			doctor = Doctor.objects.get(perfil_id=perfil.id)	

	return render(request,'perfiles/perfil.html',{'perfil':perfil,'doctor':doctor})

def indexView(request):	
    casos_count=Reporte.objects.all().filter(estado=1).aggregate(Sum('cantidadPositivas'))
    pruebas_count=Reporte.objects.all().filter(estado=1).aggregate(Sum('cantidadPruebas'))
    return render(request,'index.html',{'casos_count':casos_count,'pruebas_count':pruebas_count})

@login_required
def dashboardView(request):
	reportes = Reporte.objects.all().filter(estado=0)
	reportes_count = Reporte.objects.all().filter(estado=0).count()
	perfiles = User.objects.only().filter(is_active=0)
	perfiles_count =  User.objects.only().filter(is_active=0).count()
	all_reports = Reporte.objects.all().count()
	all_docs = Perfil.objects.all().filter(tipoUsuario=0).count()
	
	if request.user.is_authenticated:
		logi = Perfil.objects.get(user_id=request.user.id)	
	
	return render(request, 'dashboard.html',{'reportes':reportes,'reportes_count':reportes_count , 'perfiles':perfiles , 'logi':logi ,'perfiles_count':perfiles_count , 'all_reports':all_reports,'all_docs':all_docs})

def registerView(request):
	if request.method == "POST":
		form = UCFWithEmail(request.POST)
		perfil_form = PerfilForm(request.POST)
		doctor_form = DoctorForm(request.POST)
	
		
		if form.is_valid() and perfil_form.is_valid() and doctor_form.is_valid():
			user = form.save(commit=False)
			user.is_active=0
			user.save()
			perfil = perfil_form.save(commit=False)
		
			perfil.user = user
			perfil.tipoUsuario = 0
			perfil.save()

			doctor = doctor_form.save(commit=False)
			doctor.perfil = perfil
			doctor.save()

			#username = form.cleaned_data.get('username')
			#password = form.cleaned_data.get('password1')
			#user = authenticate(username=username,password=password)
			#login(request,user)
			return redirect('login')
	else:
		form = UCFWithEmail()
		perfil_form = PerfilForm()
		doctor_form = DoctorForm()

	return render(request , 'registration/register.html',{'form':form,'perfil_form':perfil_form , 'doctor_form':doctor_form})
	
def cargar_municipios(request):
    departamento_id = request.GET.get('departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
    return render(request, 'perfiles/municipios-listar.html', {'municipios': municipios})



def registerAdminView(request):
	if request.method == "POST":
		form = UCFWithEmail(request.POST)
		perfil_form = PerfilForm(request.POST)
		
		
		if form.is_valid() and perfil_form.is_valid() and doctor_form.is_valid():
			user = form.save(commit=False)
			user.is_active = 0
			user.save()
			perfil = perfil_form.save(commit=False)
		
			perfil.user = user
			perfil.tipoUsuario = 1
			perfil.save()

			return redirect('login')
	else:
		form = UCFWithEmail()
		perfil_form = PerfilForm()
	

	return render(request , 'registration/register.html',{'form':form,'perfil_form':perfil_form , 'doctor_form':doctor_form})