from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=255)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.descricao
