from django.urls import path
from .views import (
    #ListaTarefasAPIView,
    DetalheTarefaAPIView,
    ContagemTarefasAPIView,
    DuplicarTarefaAPIView,
    TarefaListCreateAPIView,  
    TarefaRetrieveUpdateDestroyAPIView,
    RegisterView,
    TarefaEstatisticasAPIView, #exercicio 2 da apostila 6
)

# Namespace do app (útil para reverse())
app_name = "core"
""" urlpatterns = [
    # Coleção: /api/tarefas/ (POST, GET - Lista)
    # /api/tarefas/ → ListaTarefasAPIView
    path("tarefas/", ListaTarefasAPIView.as_view(), name="lista-tarefas"),
    # Recurso Individual: /api/tarefas/<pk>/ (GET, PUT, PATCH, DELETE)
    path("tarefas/<int:pk>/", DetalheTarefaAPIView.as_view(), name="detalhe-tarefa"),
    # Exercicio 2
    path(
        "tarefas/contagem/", ContagemTarefasAPIView.as_view(), name="contagem-tarefas"
    ),
    # Exercicio 2 Apostila 3
    path(
        "tarefas/<int:pk>/duplicar/",
        DuplicarTarefaAPIView.as_view(),
        name="duplicar-tarefa",
    ),
    path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefas-list'), 
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), 
        name='tarefas-detail'),
    path("tarefas/estatisticas/", TarefaEstatisticasAPIView.as_view(), name="tarefas-estatisticas"),
    # Nova rota de registro 
    path('register/', RegisterView.as_view(), name='register'), 
]
""""" 

urlpatterns = [ path("tarefas/", TarefaListCreateAPIView.as_view(), name="tarefas-list"), 
               path("tarefas/<int:pk>/", TarefaRetrieveUpdateDestroyAPIView.as_view(), name="tarefas-detail"),
               path("tarefas/contagem/", ContagemTarefasAPIView.as_view(), name="contagem-tarefas"),
               path("tarefas/<int:pk>/duplicar/", DuplicarTarefaAPIView.as_view(), name="duplicar-tarefa"),
               path("tarefas/estatisticas/", TarefaEstatisticasAPIView.as_view(), name="tarefas-estatisticas"),
               path("register/", RegisterView.as_view(), name="register"), ]