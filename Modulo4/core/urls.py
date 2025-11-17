# core/urls.py
from django.urls import path
from . import views # O '.' importa as 'views' do app atual
urlpatterns = [
# Quando a URL for a raiz (''), chame a função 'home' de 'views.py'
path('', views.home, name='home'),
# NOSSAS NOVAS URLs DINÂMICAS
# Ex: /tarefa/5/concluir/
# <int:pk> captura um inteiro da URL e o passa para a view como um argumento chamado 'pk'
path('tarefa/<int:pk>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
# Ex: /tarefa/5/deletar/
path('tarefa/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
]
