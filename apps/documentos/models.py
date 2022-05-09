from django.db import models


class Documento(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descricao
