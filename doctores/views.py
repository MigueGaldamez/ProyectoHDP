from django.shortcuts import render , redirect
from .models import Doctor
from .forms import DoctorForm

from .filters import DoctorFilter
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from perfiles.models import Perfil 
from perfiles.forms import PerfilForm_editar,PerfilForm_ver
from perfiles.forms import UCFWithEmail ,UCFWithEmail_editar

from django.contrib import messages
def verDoctor(request, id): #Vist apara ver informacion de un doctor en especifico dentro de la tabla
    doctor= Doctor.objects.get(id=id)
    perfil= Perfil.objects.get(id=doctor.perfil_id)
    user = User.objects.get(id=perfil.user_id)
    form_perfil=PerfilForm_ver(request.POST or None,instance=perfil)
    form_user= UCFWithEmail_editar(request.POST or None , instance=user)
    
    if request.method == 'POST' and "Eliminar" in request.POST: #Inicia la parte para "eliminar" un reporte
        perfil.eliminado=1
        perfil.save()
        messages.info(request, 'El Doctor ha sido eliminado Exitosamente!')
        return redirect('listar_doctores')#termina el  codigo para eliminar un reporte
    if form_user.is_valid():
        perfil.save()
        user.save()
        return redirect('listar_doctores')
    return render(request, 'doctor/doctor-actualizar.html',{'doctor':doctor ,'form_perfil':form_perfil ,'usuario':user,'form_user':form_user })



def listar_doctores(request):
    #doctores = Doctor.objects.all().values('id','especialidad','codigoDoctor','perfil__nombre')
    context ={}
    filtered_doctores = DoctorFilter(
		request.GET,
		queryset = Doctor.objects.all().order_by('codigoDoctor')
	)
    context['filtered_doctores']=filtered_doctores
	
    paginated_filtered_doctores = Paginator(filtered_doctores.qs,8)
    page_number_doc = request.GET.get('page')
    doctor_page_obj = paginated_filtered_doctores.get_page(page_number_doc)

    context['doctor_page_obj']=doctor_page_obj
	

    return render(request,'doctor/doctores.html',context=context)
 
def crear_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        form_perfil = PerfilForm_editar(request.POST)
        form_user = UCFWithEmail(request.POST )
        
        if form.is_valid() and form_perfil.is_valid() and form_user.is_valid():

            user = form_user.save(commit=False)
            user.is_active = 1
            user.save()

            perfil = form_perfil.save(commit=False)
            perfil.user = user
            perfil.tipoUsuario = 0
            perfil.save()
        
            doctor = form.save(commit=False)
            doctor.perfil = perfil
            doctor.save()
            messages.success(request, 'Cuenta creada con exito !')
		
        
            return redirect('listar_doctores')
    else:
        form = DoctorForm()
        form_perfil = PerfilForm_editar()
        form_user = UCFWithEmail()
    
    return render(request, 'doctor/doctor-guardar.html',{'form':form ,'form_perfil':form_perfil , 'form_user':form_user})

			

def actualizar_doctor(request,id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    
    if form.is_valid():
        form.save() 
        return redirect('listar_doctores')
    
    return render(request, 'doctor/doctor-actualizar.html',{'form':form,'doctor':doctor})

def eliminar_doctor(request,id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('listar_doctores')

    return render(request, 'doctor/doctor-eliminar.html',{'doctor':doctor}) 




# Create your views here.
