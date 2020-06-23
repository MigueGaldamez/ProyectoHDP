
from django.db import models

# Create your models here.
class Departamento(models.Model):
	nombreDepartamento = models.CharField(max_length=50)
	

	def __str__(self):
		return self.nombreDepartamento



