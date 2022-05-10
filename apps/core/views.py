from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.funcionarios.models import Funcionario


@login_required
def home(request):

    data = {}
    data['usuario'] = Funcionario.objects.last()
    #data['usuario'] = request.user
    return render(request, 'core/index.html', data)
