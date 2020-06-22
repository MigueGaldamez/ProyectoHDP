from django.db import models

class Reporte(models.Model):
	cantPruebasRealizadas = models.IntegerField()
	cantPruebasPos = models.IntegerField()
	sospechosos = models.IntegerField()
	fechaRegistrado = models.DateTimeField()
	fechaTomado = models.DateTimeField()
	fechaEditado = models.DateTimeField()
	estado = models.IntegerField()
	cantFemenino = models.IntegerField()
	cantMasculino = models.IntegerField()
	edad0_9 = models.IntegerField()
	edad10_19 = models.IntegerField()
	edad20_39 = models.IntegerField()
	edad40_59 = models.IntegerField()
	edad60_79 = models.IntegerField()
	edad80 = models.IntegerField()
	comentario = models.CharField(max_length=200)

	def __str__(self):
		return self.comentario



