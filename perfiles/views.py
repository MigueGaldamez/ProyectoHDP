from django.shortcuts import render ,redirect
from .models import Perfil
from .forms import PerfilForm,PerfilForm_editar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UCFWithEmail ,UCFWithEmail_editar
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
#django messages
from django.contrib import messages
#json
import json
from django.http import JsonResponse

#imports
from departamentos.forms import DepartamentoForm
from departamentos.models import Departamento
from municipios.models import Municipio
from municipios.forms import  MunicipioForm
from reportes.models import Reporte
from reportes.forms import ReporteForm
from doctores.forms import DoctorForm
from doctores.models import Doctor

from django.views.generic import TemplateView
from django.db.models import Sum,Count
from collections import OrderedDict as SortedDict

def editarDoctor(request,id):

	doctor = Doctor.objects.get(id=id)
	perfil = Perfil.objects.get(id=doctor.perfil_id)
	user = User.objects.get(id=perfil.user_id)
	form = DoctorForm(request.POST or None, instance=doctor)
	form_perfil = PerfilForm_editar(request.POST or None, instance=perfil)
	form_user = UCFWithEmail_editar(request.POST or None , instance=user)
    
	if form.is_valid() and form_perfil.is_valid() and form_user.is_valid():

		doctor = form.save(commit=False)
		doctor.save()
		perfil = form_perfil.save(commit=False)
		perfil.save()
		user = form_user.save(commit=False)
		user.save()
	
		return redirect('listar_doctores')
    
	return render(request, 'doctor/doctor-actualizar.html',{'form':form,'doctor':doctor ,'form_perfil':form_perfil ,'user':user , 'form_user':form_user})
	

def  genero_resumen(request):
	porGenero = Reporte.objects.filter(estado=1,eliminado=0)
	finalrep ={}
	femenino = 0 
	masculino = 0
	for item in porGenero:		
		femenino += item.cantFemenino
		masculino += item.cantMasculino

	finalrep["Femenino"]=femenino
	finalrep["Masculino"]=masculino

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'genero_resumen':finalrep},safe=False)

def edades_resumen(request):
	porEdad = Reporte.objects.filter(estado=1,eliminado=0)
	finalrep ={}
	edad1 = 0 
	edad2 = 0
	edad3 = 0
	edad4 = 0
	edad5 = 0
	edad6 = 0
	for item in porEdad:		
		edad1 += item.edadCero
		edad2 += item.edadDiez
		edad3 += item.edadVeinte
		edad4 += item.edadCuarenta
		edad5 += item.edadSesenta
		edad6 += item.edadOchenta

	finalrep["De 0 a 9 anios"]=edad1
	finalrep["De 10 a 19 anios"]=edad2
	finalrep["De 20 a 39 anios"]=edad3
	finalrep["De 40 a 59 anios"]=edad4
	finalrep["De 60 a 79 anios"]=edad5
	finalrep["Mayores de 80"]=edad6
	


	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	
	finalrep = listsort(finalrep) 
	return JsonResponse({'edad_resumen':finalrep},safe=False)	

def fechas_resumen(request):
	porFecha = Reporte.objects.filter(estado=1, eliminado=0).order_by('fechaTomada')
	finalrep ={}
	finalrep2 ={}
				
	def get_fecha(reporte):
		return reporte.fechaTomada
	
	fechas_list = list(sorted(set(map(get_fecha,porFecha))))

	def get_positivas_amount(fecha):
		amount = 0
		filtered_by_fecha = porFecha.filter(fechaTomada=fecha)
		for item in filtered_by_fecha:
			amount += item.cantidadPositivas
		return amount

	def get_pruebas_amount(fecha):
		amount = 0
		filtered_by_fecha = porFecha.filter(fechaTomada=fecha)
		for item in filtered_by_fecha:
			amount += item.cantidadPruebas
		return amount

	for x in porFecha:
		for y in fechas_list:
			finalrep[str(y)]=get_positivas_amount(y)
			finalrep2[str(y)]=get_pruebas_amount(y)

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
			
	finalrep = listsort(finalrep)
	finalrep2 = listsort(finalrep2)
			
	return JsonResponse({'positivas_resumen':finalrep,'pruebas_resumen':finalrep2 ,'fechas_list':fechas_list},safe=False)


def  departamentos_resumen(request):
	porDepartamento = Reporte.objects.filter(estado=1,eliminado=0)
	finalrep ={}

	def get_departamento(reporte):
		return reporte.departamento
	
	departamento_list = list(set(map(get_departamento,porDepartamento)))
	

	def get_departamento_amount(departamento):
		amount = 0
		filtered_by_departamento = porDepartamento.filter(departamento=departamento)
		for item in filtered_by_departamento:
			amount += item.cantidadPositivas
		return amount

	
	for x in porDepartamento:
		for y in departamento_list:
			finalrep[str(y)]=get_departamento_amount(y)

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	finalrep = listsort(finalrep)
			
	return JsonResponse({'departamento_resumen':finalrep},safe=False)
#comeinza
def dep1_resumen(request ,id):

	porDepartamento = Reporte.objects.filter(estado=1,eliminado=0, departamento=id)
	finalrep ={}

	def get_departamento(reporte):
		return reporte.municipio
	
	departamento_list = list(set(map(get_departamento,porDepartamento)))

	def get_departamento_amount(departamento):
		amount = 0
		filtered_by_departamento = porDepartamento.filter(municipio=departamento)
		for item in filtered_by_departamento:
			amount += item.cantidadPositivas
		return amount

	
	for x in porDepartamento:
		for y in departamento_list:
			finalrep[str(y)]=get_departamento_amount(y)

	def listsort(value):
		if isinstance(value,dict):
			new_dict = SortedDict()
			key_list = value.keys()
			key_list=sorted(key_list)
			for key in key_list:
				new_dict[key] = value[key]
			return new_dict
	finalrep = listsort(finalrep)
			
	return JsonResponse({'dep1_resumen':finalrep},safe=False)
	


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
    porDepartamento = Reporte.objects.values('departamento__nombre').filter(estado=1).annotate(total=Sum('cantidadPositivas'))
    porMuniDep1 = Reporte.objects.values('municipio__nombre').filter(estado=1 ,departamento=1).annotate(total=Sum('cantidadPositivas'))
    casos_count=Reporte.objects.all().filter(estado=1).aggregate(Sum('cantidadPositivas'))
    pruebas_count=Reporte.objects.all().filter(estado=1).aggregate(Sum('cantidadPruebas'))
   
    return render(request,'index.html',{'casos_count':casos_count,'pruebas_count':pruebas_count  ,'porDepartamento': porDepartamento,'porMuniDep1':porMuniDep1})

@login_required
def dashboardView(request):
	reportes = Reporte.objects.all().filter(estado=0)
	reportes_count = Reporte.objects.all().filter(estado=0,eliminado=0).count()
	perfiles = User.objects.only().filter(is_active=0)
	perfiles_count =  User.objects.only().filter(is_active=0).count()
	all_reports = Reporte.objects.all().count()
	all_docs = Perfil.objects.all().filter(tipoUsuario=0).count()
	reportes_zona=0
	
	if request.user.is_authenticated:
		logi = Perfil.objects.get(user_id=request.user.id)
		if logi.tipoUsuario == 0:
			reportes_zona = Reporte.objects.all().filter(municipio=logi.municipio).count()

	return render(request, 'dashboard.html',{'reportes':reportes,'reportes_count':reportes_count , 'perfiles':perfiles , 'logi':logi ,'perfiles_count':perfiles_count , 'all_reports':all_reports,'all_docs':all_docs,'reportes_zona':reportes_zona})

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
			messages.success(request, 'Cuenta creada con exito,espere a que sea activada!')
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