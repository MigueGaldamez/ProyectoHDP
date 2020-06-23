from django.shortcuts import render ,redirect
from .models import Municipio
from .forms import MunicipioForm

def listar_municipios(request):
	municipios = Municipio.objects.all()
	return render(request,'municipios.html',{'municipios':municipios})
	
def crear_municipio(request):
	form = MunicipioForm(request.POST or None)
	
	if form.is_valid():
		form.save()
		return redirect('listar_municipios')
	return render(request, 'municipio-guardar.html',{'form':form})

def actualizar_municipio(request,id):
	municipio = Municipio.objects.get(id=id)
	form = MunicipioForm(request.POST or None, instance=municipio)
	
	if form.is_valid():
		form.save()
		return redirect('listar_municipios')
	
	return render(request, 'municipio-actualizar.html',{'form':form,'municipio':municipio})

def eliminar_municipio(request,id):
	municipio = Municipio.objects.get(id=id)
	if request.method == 'POST':
		municipio.delete()
		return redirect('listar_municipios')

	return render(request, 'municipio-eliminar.html',{'municipio':municipio})