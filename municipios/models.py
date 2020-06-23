from django.db import models

# Create your models here.

class Departamento(models.Model):
	nombreDepartamento = models.CharField(max_length=50)	
	def __str__(self):
		return self.nombreDepartamento
	class Meta:
		db_table="departamentos"
    
class Municipio(models.Model):
	idDepartamento = models.IntegerField()
	nombreMunicipio = models.CharField(max_length=50)	
	def __str__(self):
		return self.nombreMunicipio
	class Meta:
		db_table="municipios"






