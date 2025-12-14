from django.urls import path
from .views import ListaTarefasAPIView, DetalheTarefaAPIView, ContagemTarefasAPIView

# Namespace do app (útil para reverse())
app_name = "core"
urlpatterns = [
    # Coleção: /api/tarefas/ (POST, GET - Lista)
    # /api/tarefas/ → ListaTarefasAPIView
    path("tarefas/", ListaTarefasAPIView.as_view(), name="lista-tarefas"),
    # Recurso Individual: /api/tarefas/<pk>/ (GET, PUT, PATCH, DELETE)
    path("tarefas/<int:pk>/", DetalheTarefaAPIView.as_view(), name="detalhe-tarefa"),
    # Exercicio 2
    path(
        "tarefas/contagem/", ContagemTarefasAPIView.as_view(), name="contagem-tarefas"
    ),
]
