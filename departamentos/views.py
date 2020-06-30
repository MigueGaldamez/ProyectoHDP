from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Departamento
from .forms import DepartamentoForm

# Create your views here.

#crud depto
@login_required
def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request,'departamento/departamentos.html',{'departamentos':departamentos})

@login_required
def crear_departamento(request):
    form = DepartamentoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_departamentos')
    return render(request, 'departamento/departamento-guardar.html',{'form':form})

@login_required
def actualizar_departamento(request,id):
    departamento = Departamento.objects.get(id=id)
    form = DepartamentoForm(request.POST or None, instance=departamento)
    
    if form.is_valid():
        form.save() 
        return redirect('listar_departamentos')
    
    return render(request, 'departamento/departamento-actualizar.html',{'form':form,'departamento':departamento})

@login_required
def eliminar_departamento(request,id):
    departamento = Departamento.objects.get(id=id)
    if request.method == 'POST':
        departamento.delete()
        return redirect('listar_departamentos')

    return render(request, 'departamento/departamento-eliminar.html',{'departamento':departamento}) 


