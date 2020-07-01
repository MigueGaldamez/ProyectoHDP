from django.db import models
from departamentos.models import Departamento

# Create your models here.
class Municipio(models.Model):
	departamento =  models.ForeignKey(Departamento,on_delete=models.CASCADE) 
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre
	class Meta:
		db_table="municipio"

