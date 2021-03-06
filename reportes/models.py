from django.db import models
from departamentos.models import Departamento
from municipios.models import Municipio
from perfiles.models import Perfil
    
class Reporte(models.Model):
	cantidadPruebas = models.IntegerField()
	cantidadPositivas = models.IntegerField()
	sospechosos= models.IntegerField()
	fechaTomada=  models.DateField()
	fechaEditado=  models.DateField()
	cantFemenino = models.IntegerField()
	cantMasculino = models.IntegerField()
	edadCero = models.IntegerField()
	edadDiez = models.IntegerField()
	edadVeinte = models.IntegerField()
	edadCuarenta = models.IntegerField()
	edadSesenta = models.IntegerField()
	edadOchenta = models.IntegerField()
	complemento = models.CharField(max_length=50)	
	departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE) 
	municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE) 
	estado = models.IntegerField()
	eliminado = models.IntegerField()
	perfil = models.ForeignKey(Perfil,on_delete = models.CASCADE)
	duiIngresado = models.CharField(max_length=9)
	class Meta:
		db_table="reporte"





