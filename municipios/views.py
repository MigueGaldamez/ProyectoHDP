from django.shortcuts import render ,redirect
from .models import Municipio
from .forms import  MunicipioForm
from django.contrib.auth.decorators import login_required
from departamentos.forms import DepartamentoForm
from departamentos.models import Departamento

# Create your views here.

# crud municipios
def listar_municipios(request):
    municipios = Municipio.objects.all()
    departamentos = Departamento.objects.all()
    return render(request,'municipio/municipios.html',{'municipios':municipios,'departamentos':departamentos})
				#
	
def crear_municipio(request):
	form = MunicipioForm(request.POST or None)
	
	if form.is_valid():
		form.save()
		return redirect('listar_municipios')
	return render(request, 'municipio/municipio-guardar.html',{'form':form})

def actualizar_municipio(request,id):
	municipio = Municipio.objects.get(id=id)
	form = MunicipioForm(request.POST or None, instance=municipio)
	
	if form.is_valid():
		form.save()
		return redirect('listar_municipios')
	
	return render(request, 'municipio/municipio-actualizar.html',{'form':form,'municipio':municipio})

def eliminar_municipio(request,id):
	municipio = Municipio.objects.get(id=id)
	if request.method == 'POST':
		municipio.delete()
		return redirect('listar_municipios')

	return render(request, 'municipio/municipio-eliminar.html',{'municipio':municipio})

