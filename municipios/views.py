from django.shortcuts import render ,redirect
from .models import Municipio
from .forms import  MunicipioForm
from django.contrib.auth.decorators import login_required
from departamentos.forms import DepartamentoForm
from departamentos.models import Departamento

from django.contrib import messages


from .filters import MunicipioFilter
from django.core.paginator import Paginator
# Create your views here. 

# crud municipios
def listar_municipios(request):


	context ={}
	filtered_municipios = MunicipioFilter(
		request.GET,
		queryset = Municipio.objects.all().order_by('nombre')
	)
	context['filtered_municipios']= filtered_municipios
	
	paginated_filtered_muncipios = Paginator(filtered_municipios.qs,8)
	page_number_mun = request.GET.get('page')
	municipio_page_obj = paginated_filtered_muncipios.get_page(page_number_mun)

	context['municipio_page_obj']=municipio_page_obj
	
	return render(request,'municipio/municipios.html',context=context)
				
	
def crear_municipio(request):
	form = MunicipioForm(request.POST or None)
	
	if form.is_valid():
		form.save()
		messages.success(request, 'Municipio agregado con exito !')
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

