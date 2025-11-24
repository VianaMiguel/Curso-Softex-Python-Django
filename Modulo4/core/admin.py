from django.contrib import admin
from .models import Tarefa # 1. Importe seu Model

# 1. Crie uma classe que herda de admin.ModelAdmin
# A convenção é usar o nome do Model + "Admin"
class TarefaAdmin(admin.ModelAdmin):
# 'list_display' é uma tupla com os nomes dos campos
# que queremos exibir como colunas na lista
    list_display = ('titulo', 'user', 'concluida', 'criada_em')

# Adiciona uma barra lateral de filtros
# O Django entende o tipo de campo e cria o filtro certo:
# - 'concluida': Filtro de "Sim/Não"
# - 'user': Filtro de lista (baseado em um ForeignKey)
# - 'criada_em': Filtro de data (Hoje, Últimos 7 dias, Este mês, etc.)
    list_filter = ('concluida', 'user', 'criada_em')
# Adiciona uma barra de busca
# 'titulo': Vai buscar no campo 'titulo'
# 'user__username': Este é avançado! Usamos o lookup '__'
# para dizer ao Django: "Busque também no campo 'username'
# do Model 'User' que está relacionado".
    search_fields = ('titulo', 'user__username')
# ----------------------------------------------------
# NOVAS CONFIGURAÇÕES (para o formulário de edição)
# ----------------------------------------------------
# 'fieldsets' permite agrupar os campos em seções
# A estrutura é: ( ('Nome da Seção', {'fields': ('campo1', 'campo2')}) , ... )
    fieldsets = (
('Informações Principais', {
'fields': ('user', 'titulo')
}),
('Status da Tarefa', {
'fields': ('concluida', 'criada_em')
}),
)
# 'readonly_fields' define campos que podem ser vistos, mas não editados
# Perfeito para campos automáticos como 'criada_em'
    readonly_fields = ('criada_em',)

# 2. Defina o método
# O 'obj' é a instância da Tarefa que está sendo exibida na linha
@admin.display(description='Email do Usuário') # Define o título da coluna
def get_user_email(self, obj):
    return obj.user.email



# Register your models here.

# 2. "Registre" seu Model no site de administração
admin.site.register(Tarefa, TarefaAdmin)

#Usuário : admin
#Endereço : admin@admin.com
#Senha: admin
