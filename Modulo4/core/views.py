from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Uma 'view' é uma função que recebe um 'request' e retorna uma 'response'
def home(request):
# Vamos retornar a resposta HTTP mais simples: um texto HTML
#return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>") modo antigo

# 1. Crie seu dicionário de contexto
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS']
    }

    return render(request, 'home.html', context)

def saudacao(request):
    return HttpResponse("<input>Saudacao</input>")