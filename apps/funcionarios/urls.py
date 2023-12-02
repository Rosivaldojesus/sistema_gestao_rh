from django.urls import path

from .views import FuncionariosList, FuncionariosEdit

urlpatterns = [

    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionario')
]
