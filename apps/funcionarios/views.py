from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario
from django.views.generic import ListView, UpdateView


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']