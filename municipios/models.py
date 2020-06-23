from django.db import models

# Create your models here.
class Municipio(models.Model):
	idDepartamento = models.IntegerField()
	nombreMunicipio = models.CharField(max_length=50)
	

	def __str__(self):
		return self.nombreMunicipio




