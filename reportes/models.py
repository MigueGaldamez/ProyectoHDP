from django.db import models

class Departamento(models.Model):
	nombre = models.CharField(max_length=50)	
	def __str__(self):
		return self.nombre
	class Meta:
		db_table="departamento"
    
class Municipio(models.Model):
	departamento =  models.ForeignKey(Departamento,on_delete=models.CASCADE) 
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre
	class Meta:
		db_table="municipio"


class Reporte(models.Model):
	cantidadPruebas = models.IntegerField()
	cantidadPositivas = models.IntegerField()
	municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE) 

	class Meta:
		db_table="reporte"



