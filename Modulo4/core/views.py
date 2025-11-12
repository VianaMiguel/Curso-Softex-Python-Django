from django.shortcuts import render, redirect
from .models import Tarefa
from .forms import TarefaForm # 2. Importe nosso novo 'TarefaForm'

# Create your views here.

# Uma 'view' é uma função que recebe um 'request' e retorna uma 'response'
def home(request):
# 3. Lógica de POST: Se o formulário foi enviado
    if request.method == 'POST':
# Cria uma instância do form e preenche com os dados do POST
        form = TarefaForm(request.POST)
# 4. O Django valida os dados (max_length, etc.)
        if form.is_valid():
# 5. Salva o objeto no banco de dados!
            form.save()
# 6. Redireciona de volta para a 'home'
# Isso é o Padrão "Post-Redirect-Get" (PRG)
            return redirect('home')
# Se o form NÃO for válido, o código continua e
# o 'form' (com os erros) será enviado para o template
# 7. Lógica de GET: Se o usuário apenas visitou a página
    else:
        form = TarefaForm() # Cria um formulário vazio

# 2. Use o ORM para buscar os dados!
# Tarefa.objects.all() significa: "Pegue todas as linhas da tabela Tarefa"
    todas_as_tarefas = Tarefa.objects.all().order_by('-criada_em') # Ordena pelas mais novas
# Vamos retornar a resposta HTTP mais simples: um texto HTML
#return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>") modo antigo

# 1. Crie seu dicionário de contexto
    context = {
        'nome_usuario': 'Júnior',
        'tecnologias': ['Python', 'Django', 'HTML', 'CSS','Models', 'Admin'],
        'tarefas': todas_as_tarefas, # 4. Adicione as tarefas ao contexto
        'form': form, # 10. Envie o 'form' (vazio ou com erros) para o template
    }

    return render(request, 'home.html', context)
