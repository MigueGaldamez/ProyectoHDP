from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from departamentos.models import Departamento
from municipios.models import Municipio
    
# Create your models here.

class Perfil(models.Model):
	departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE) 
	municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE) 
	nombre =models.CharField(max_length=50)
	user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
	tipoUsuario =  models.IntegerField()
	eliminado=models.IntegerField()
	apellido =models.CharField(max_length=50)
	complemento = models.CharField(max_length=50)
	telefono = models.CharField(max_length=8,unique=True)
	DUI = models.CharField(max_length=9,unique=True)
	fechaNacimiento = models.DateField()
	def __str__(self):
		return self.nombre
	class Meta:
		db_table="perfil"

