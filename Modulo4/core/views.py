from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa

# Create your views here.

# Uma 'view' é uma função que recebe um 'request' e retorna uma 'response'
def home(request):
# 2. Use o ORM para buscar os dados!
# Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa"
    todas_as_tarefas = Tarefa.objects.all()
# Vamos retornar a resposta HTTP mais simples: um texto HTML
#return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>") modo antigo

# 1. Crie seu dicionário de contexto
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS','Models', 'Admin'],
        'tarefas': todas_as_tarefas # 4. Adicione as tarefas ao contexto
    }

    return render(request, 'home.html', context)

def saudacao(request):
    return HttpResponse("<input>Saudacao</input>")