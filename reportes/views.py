from django.shortcuts import render ,redirect
from .models import Reporte
from .forms import ReporteForm

def listar_reportes(request):
	reportes = Reporte.objects.all()
	return render(request,'reportes.html',{'reportes':reportes})
	
def crear_reporte(request):
	form = ReporteForm(request.POST or None)
	
	if form.is_valid():
		form.save()
		return redirect('listar_reportes')
	return render(request, 'reportes-form.html',{'form':form})

def update_reporte(request,id):
	reporte = Reporte.objects.get(id=id)
	form = ReporteForm(request.POST or None, instance=reporte)
	
	if form.is_valid():
		form.save()
		return redirect('listar_reportes')
	
	return render(request, 'reportes-form-act.html',{'form':form,'reporte':reporte})

def delete_reporte(request,id):
	reporte = Reporte.objects.get(id=id)
	if request.method == 'POST':
		reporte.delete()
		return redirect('listar_reportes')

	return render(request, 'prod-delete-confirm.html',{'reporte':reporte})