from django.shortcuts import render ,redirect,get_object_or_404
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
from django.contrib import messages
from django.http import Http404
# Create your views here.
from .filters import ReporteFilter
from django.core.paginator import Paginator



def cargar_municipios(request):
    departamento_id = request.GET.get('departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
    return render(request, 'reportes/municipios-listar.html', {'municipios': municipios})

#crud reporte
@login_required
def listar_reportes(request):
	context ={}
	if request.method == 'GET' and 'eliminado' in request.GET:
		filtered_reportes = ReporteFilter(
			request.GET,
			queryset = Reporte.objects.all().order_by('-fechaTomada')
		)
	else:
		filtered_reportes = ReporteFilter(
			request.GET,
			queryset = Reporte.objects.all().order_by('-fechaTomada').filter(eliminado=0)
		)


	context['filtered_reportes']=filtered_reportes
	
	paginated_filtered_reportes = Paginator(filtered_reportes.qs,8)
	page_number = request.GET.get('page')
	reporte_page_obj = paginated_filtered_reportes.get_page(page_number)

	context['reporte_page_obj']=reporte_page_obj
	reportes = Reporte.objects.exclude(eliminado=1).order_by('-fechaTomada')
	#return render(request,'reportes/reportes.html',{'reportes':reportes})
	return render(request,'reportes/reportes.html',context=context)
	

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
		messages.success(request, 'El Reporte se ha creado Exitosamente!')
		return redirect('listar_reportes')
	return render(request,'reportes/reporte-guardar.html',{'form':form,'municipios':municipios,'departamentos':departamentos})

@login_required
def actualizar_reporte(request,id):
	try:
		reporte = 0
		if request.user.is_authenticated:
			reporte = Reporte.objects.get(id=id)
		else:
			reporte = Reporte.objects.exclude(eliminado=1).get(id=id)

		
		departamentos = Departamento.objects.all()
		municipios = Municipio.objects.all()
		form = ReporteForm(request.POST or None, instance=reporte)
		if request.method == 'POST' and "Eliminar" in request.POST: #Inicia la parte para "eliminar" un reporte
			obj = form.save(commit=False)
			if not request.user.is_authenticated:
				obj.estado = 0

			obj.save()
			Reporte.objects.filter(id=id).update(eliminado=1)#filtramos que el registro sea por id y que le actulice el estado a  0
			messages.info(request, 'El Reporte ha sido eliminado Exitosamente!')
			return redirect('listar_reportes')#termina el  codigo para eliminar un reporte
		if form.is_valid():
			obj = form.save(commit=False)
			if not request.user.is_authenticated:
					obj.estado = 0
			
			obj.save()
			messages.success(request, 'El  reporte ha sido actualizado Exitosamente!')
			return redirect('listar_reportes')
		return render(request, 'reportes/reporte-actualizar.html',{'form':form,'reporte':reporte,'municipios':municipios,'departamentos':departamentos})
	except Reporte.DoesNotExist:
		messages.error(request, 'El reporte no existe')
		return redirect('listar_reportes')

