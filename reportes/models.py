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
class Direccion(models.model):
    complemento = models.CharField(max_length=50)
    municipio = models.ForeignKey(Departamento,on_delete=models.CASCADE)
	def __str__(self):
		return self.complemento
	class Meta:
		db_table="direccion"
class Reporte(models.Model):
	cantidadPruebas = models.IntegerField(null=False)
	cantidadPositivas = models.IntegerField(null=False)
	sospechosos= models.IntegerField(null=False)
	fechaTomada=  models.DateField(null=False)
	cantFemenino = models.IntegerField(null=False)
	cantMasculino = models.IntegerField(null=False)
	edadCero = models.IntegerField(null=False)
	edadDiez = models.IntegerField(null=False)
	edadVeinte = models.IntegerField(null=False)
	edadCuarenta = models.IntegerField(null=False)
	edadSesenta = models.IntegerField(null=False)
	edadOchenta = models.IntegerField(null=False)
	estado = models.IntegerField(default=1)
	departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE) 
	municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
	direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)
	class Meta:
		db_table="reporte"



