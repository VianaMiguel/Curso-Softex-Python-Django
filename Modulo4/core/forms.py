# core/forms.py
from django import forms
from .models import Tarefa # Importe o Model
from projects.models import Project # Importe o Project
# Esta classe herda de 'ModelForm'
class TarefaForm(forms.ModelForm):
    # 1. Vamos sobrescrever o construtor do formulário
    def __init__(self, *args, **kwargs):
# 2. Capture o 'user' que será passado pela view
        user = kwargs.pop('user', None)
# 3. Chame o construtor original (pai)
        super(TarefaForm, self).__init__(*args, **kwargs)
# 4. A MÁGICA:
# Se o 'user' foi passado...
        if user:
# ...filtre o 'queryset' (a lista de opções) do campo 'project'
# para mostrar apenas os projetos onde o 'user' é o usuário logado.
            self.fields['project'].queryset = Project.objects.filter(user=user)
    
    
    # A "mágica" acontece aqui, na classe 'Meta'
    class Meta:
    # 1. Diga ao form qual Model ele deve usar
        model = Tarefa
    # 2. Diga quais campos do Model devem virar campos no form
    # Nós só queremos que o usuário defina o 'titulo'.
    # 'concluida' (default=False) e 'criada_em' (auto_now_add=True)
    # serão preenchidos automaticamente pelo Model.
        fields = ['titulo', 'concluida', 'project']