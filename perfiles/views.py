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

from django.db.models import Sum



# Create your views here.

#VIEWS DE SEGURIDAD
def indexView(request):
	
    casos_count=Reporte.objects.all().filter(estado=1).aggregate(Sum('cantidadPositivas'))
    pruebas_count=Reporte.objects.all().filter(estado=1).aggregate(Sum('cantidadPruebas'))
    return render(request,'index.html',{'casos_count':casos_count,'pruebas_count':pruebas_count})

@login_required
def dashboardView(request):
	reportes = Reporte.objects.all().filter(estado=0)
	reportes_count = Reporte.objects.all().filter(estado=0).count()
	perfiles = User.objects.all().filter(is_active=0)
	return render(request, 'dashboard.html',{'reportes':reportes,'reportes_count':reportes_count , 'perfiles':perfiles})

def registerView(request):
	if request.method == "POST":
		form = UCFWithEmail(request.POST)
		perfil_form = PerfilForm(request.POST)
	
		
		if form.is_valid() and perfil_form.is_valid():
			user = form.save(commit=False)
			user.is_active=0
			user.save()
			perfil = perfil_form.save(commit=False)
		
			perfil.user = user
			perfil.save()
			#username = form.cleaned_data.get('username')
			#password = form.cleaned_data.get('password1')
			#user = authenticate(username=username,password=password)
			#login(request,user)
			return redirect('login_url')
	else:
		form = UCFWithEmail()
		perfil_form = PerfilForm()

	return render(request , 'registration/register.html',{'form':form,'perfil_form':perfil_form})
	
def cargar_municipios(request):
    departamento_id = request.GET.get('departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
    return render(request, 'perfiles/municipios-listar.html', {'municipios': municipios})
