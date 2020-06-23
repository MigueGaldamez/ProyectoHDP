
from django.shortcuts import render ,redirect
from .models import Departamento
from .forms import DepartamentoForm

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

