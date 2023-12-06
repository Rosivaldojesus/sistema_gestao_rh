from django.db import models
from apps.empresas.models import Empresa
from django.urls import reverse

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('list_departamentos')
        

    def __str__(self) -> str:
        return self.nome
