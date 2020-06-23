from django.shortcuts import render ,redirect
from .models import Municipio ,Departamento
from .forms import MunicipioForm ,DepartamentoForm


# crud municipios
def listar_municipios(request):
    municipios = Municipio.objects.all()
    departamentos = Departamento.objects.all()
    return render(request,'municipios.html',{'municipios':municipios,'departamentos':departamentos})
	
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

#crud depto
def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request,'departamentos.html',{'departamentos':departamentos})
    
def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_departamentos')
    return render(request, 'departamento-guardar.html',{'form':form})

def actualizar_departamento(request,id):
    departamento = Departamento.objects.get(id=id)
    form = DepartamentoForm(request.POST or None, instance=departamento)
    
    if form.is_valid():
        form.save() 
        return redirect('listar_departamentos')
    
    return render(request, 'departamento-actualizar.html',{'form':form,'departamento':departamento})

def eliminar_departamento(request,id):
    departamento = Departamento.objects.get(id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('listar_departamentos')

    return render(request, 'departamento-eliminar.html',{'departamento':departamento}) 