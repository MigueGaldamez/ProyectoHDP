from django.shortcuts import render , redirect
from .models import Doctor
from .forms import DoctorForm


def listar_doctores(request):
    #doctores = Doctor.objects.all().values('id','especialidad','codigoDoctor','perfil__nombre')
    doctores = Doctor.objects.select_related()
    return render(request,'doctor/doctores.html',{'doctores':doctores})

def crear_doctor(request):
    form =DoctorForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_doctores')
    return render(request, 'doctor/doctor-guardar.html',{'form':form})

def actualizar_doctor(request,id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    
    if form.is_valid():
        form.save() 
        return redirect('listar_doctoress')
    
    return render(request, 'doctor/doctor-actualizar.html',{'form':form,'doctor':doctor})

def eliminar_doctor(request,id):
    doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('listar_doctores')

    return render(request, 'doctor/doctor-eliminar.html',{'doctor':doctor}) 




# Create your views here.
