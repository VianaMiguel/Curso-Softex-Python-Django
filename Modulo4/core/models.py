from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.

# Cada classe aqui é "traduzida" para uma tabela no banco de dados
class Tarefa(models.Model):
    
    
 # 'on_delete=models.CASCADE' diz ao banco:
 # "Se o usuário for deletado, delete todas as tarefas dele também."
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 2. ADICIONE A NOVA RELAÇÃO
# Cada Tarefa agora DEVE estar ligada a um Projeto.
# 'related_name' é uma boa prática para consultas inversas.
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tarefas')
# Um campo de texto curto, com máximo de 200 caracteres
    titulo = models.CharField(max_length=200)
# Um campo booleano (verdadeiro/falso), que por padrão é Falso
    concluida = models.BooleanField(default=False)
# Um campo de data e hora.
# auto_now_add=True: Salva a data e hora EXATAMENTE quando o objeto é criado
    criada_em = models.DateTimeField(auto_now_add=True)
    
# Este é um "método mágico" do Python.
# Ele diz ao Django como "chamar" um objeto Tarefa.
# Em vez de "Tarefa object (1)", ele mostrará o título da tarefa.
# Isso é EXTREMAMENTE útil no painel de administração.
def __str__(self):
    return self.titulo