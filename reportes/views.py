from django.shortcuts import render ,redirect
from .models import Reporte, Municipio, Departamento
from .forms import ReporteForm, MunicipioForm, DepartamentoForm


def cargar_municipios(request):
    departamento_id = request.GET.get('departamento')
    municipios = Municipio.objects.filter(departamento_id=departamento_id).order_by('nombre')
    return render(request, 'reportes/municipios-listar.html', {'municipios': municipios})

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

#crud depto
def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request,'departamento/departamentos.html',{'departamentos':departamentos})
    
def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_departamentos')
    return render(request, 'departamento/departamento-guardar.html',{'form':form})

def actualizar_departamento(request,id):
    departamento = Departamento.objects.get(id=id)
    form = DepartamentoForm(request.POST or None, instance=departamento)
    
    if form.is_valid():
        form.save() 
        return redirect('listar_departamentos')
    
    return render(request, 'departamento/departamento-actualizar.html',{'form':form,'departamento':departamento})

def eliminar_departamento(request,id):
    departamento = Departamento.objects.get(id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('listar_departamentos')

    return render(request, 'departamento/departamento-eliminar.html',{'departamento':departamento}) 

#crud reporte
def listar_reportes(request):
	reportes = Reporte.objects.all()
	return render(request,'reportes/reportes.html',{'reportes':reportes})
	
def crear_reporte(request):
	departamentos = Departamento.objects.all()
	municipios = Municipio.objects.all()
	form = ReporteForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('listar_reportes')
	return render(request,'reportes/reporte-guardar.html',{'form':form,'municipios':municipios,'departamentos':departamentos})
<<<<<<< HEAD
=======

>>>>>>> e1f832654f62ec2a1441cfe36314973d6e9f00d5

def actualizar_reporte(request,id):
	reporte = Reporte.objects.get(id=id)
	form = ReporteForm(request.POST or None, instance=reporte)
	
	if form.is_valid():
		form.save()
		return redirect('listar_reportes')
	
	return render(request, 'reportes/reporte-actualizar.html',{'form':form,'reporte':reporte})

def eliminar_reporte(request,id):
	reporte = Reporte.objects.get(id=id)
	if request.method == 'POST':
		reporte.delete()
		return redirect('listar_reportes')

	return render(request, 'reportes/reporte-eliminar.html',{'reporte':reporte})