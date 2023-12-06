from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario
from django.views.generic import ListView, UpdateView, CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("list_funcionarios")
    

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(
            username=funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1])
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)

    