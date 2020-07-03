from django.db import models
from perfiles.models import Perfil
    
# Create your models here.

class Doctor(models.Model):
    perfil = models.OneToOneField(Perfil, null=True,on_delete=models.CASCADE)
    especialidad =models.CharField(max_length=50)
    codigoDoctor = models.CharField(max_length=50)
    def __str__(self):
        return self.especialidad

    class Meta:
        db_table="doctor"
