from django.shortcuts import render ,redirect
from .models import Reporte
from .forms import ReporteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from perfiles.forms import UCFWithEmail
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
#imports
from departamentos.forms import DepartamentoForm
from departamentos.models import Departamento
from municipios.models import Municipio
from municipios.forms import  MunicipioForm
from perfiles.models import Perfil
from perfiles.forms import PerfilForm


# Create your views here.

def cargar_municipios(request):
    departamento_id = request.GET.get('departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
    return render(request, 'reportes/municipios-listar.html', {'municipios': municipios})

#crud reporte
@login_required
def listar_reportes(request):
	reportes = Reporte.objects.all()
	return render(request,'reportes/reportes.html',{'reportes':reportes})
	
def crear_reporte(request):
	departamentos = Departamento.objects.all()
	municipios = Municipio.objects.all()
	form = ReporteForm(request.POST or None)

	if form.is_valid():
		obj = form.save(commit=False)
		
		if not request.user.is_authenticated:
        		obj.estado = 0
		else:
        		obj.estado = 1
		obj.save()
		
		return redirect('listar_reportes')
	return render(request,'reportes/reporte-guardar.html',{'form':form,'municipios':municipios,'departamentos':departamentos})

@login_required
def actualizar_reporte(request,id):
	reporte = Reporte.objects.get(id=id)
	departamentos = Departamento.objects.all()
	municipios = Municipio.objects.all()
	form = ReporteForm(request.POST or None, instance=reporte)
	if form.is_valid():
		obj = form.save(commit=False)
		if not request.user.is_authenticated:
        		obj.estado = 0
		else:
        		obj.estado = 1
		obj.save()
		return redirect('listar_reportes')
	return render(request, 'reportes/reporte-actualizar.html',{'form':form,'reporte':reporte,'municipios':municipios,'departamentos':departamentos})

@login_required
def eliminar_reporte(request,id):
	reporte = Reporte.objects.get(id=id)
	if request.method == 'POST':
		reporte.delete()
		return redirect('listar_reportes')

	return render(request, 'reportes/reporte-eliminar.html',{'reporte':reporte})


