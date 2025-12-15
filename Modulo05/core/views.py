from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tarefa
from .serializers import TarefaSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView



class ListaTarefasAPIView(APIView):
    """
    View para listar todas as tarefas (GET).
    Endpoints:
    GET /api/tarefas/ - Lista todas as tarefas
    """


def get(self, request, format=None):
    """
    Retorna lista de todas as tarefas do banco.
    Returns:
    Response: JSON com lista de tarefas e status 200
    """
    user_id = request.query_params.get("user_id")  # Exercicio 3

    if user_id:
        tarefas = Tarefa.objects.filter(user_id=user_id)  # Exercicio 3
    else:
        tarefas = Tarefa.objects.all()  # Exercicio 3

    # 1. BUSCAR: ORM do Django busca todos os registros
    # tarefas = Tarefa.objects.all()
    # 2. SERIALIZAR: Converter objetos Python → JSON
    # many=True: indica que é uma lista de objetos

    serializer = TarefaSerializer(tarefas, many=True)
    # 3. RESPONDER: Retornar JSON com status HTTP
    return Response(serializer.data, status=status.HTTP_200_OK)


def post(self, request, format=None):
    """
    Cria uma nova tarefa.

    Args:
    request.data: JSON com dados da tarefa
    {
    "titulo": "string",
    "concluida": boolean (opcional, default=False)
    }

    Returns:
    201 Created: Tarefa criada com sucesso
    400 Bad Request: Dados inválidos
    """

    try:
        # 1. INSTANCIAR: Criar serializer com dados recebidos
        serializer = TarefaSerializer(data=request.data)
        # 2. VALIDAR: Checar se os dados são válidos
        if serializer.is_valid():
            # 3. SALVAR: Persistir no banco de dados
            serializer.save()
            logger.info(f"[INFO]: Tarefa criada: {serializer.data['id']}")
            # 4. RESPONDER: Retornar objeto criado + status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.warning(f"[WARNING]: Validação falhou: {serializer.errors}")
        # 5. ERRO: Retornar erros de validação + status 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except IntegrityError as e:
        # Erro de constraint no banco (ex: UNIQUE)
        return Response(
            {"error": "[ERROR]: Violação de integridade no banco de dados."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        # Erro inesperado
        logger.error(f"Erro ao criar tarefa: {str(e)}")
        return Response(
            {"error": "Erro interno do servidor."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


class DetalheTarefaAPIView(APIView):
    """
    View para operações em recurso individual.
    GET, PUT, PATCH, DELETE /api/tarefas/<pk>/
    """

    def get_object(self, pk):
        return get_object_or_404(Tarefa, pk=pk)

    # 4. GET (Buscar)
    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 5. PUT (Atualização Total)
    def put(self, request, pk, format=None):

        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 6. PATCH (Atualização Parcial)
    def patch(self, request, pk, format=None):

        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(
            tarefa, data=request.data, partial=True  # Permite omissão de campos
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 7. DELETE (Remoção)
    def delete(self, request, pk, format=None):

        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Exercicio 2


class ContagemTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        return Response(
            {"total": total, "concluidas": concluidas, "pendentes": pendentes},
            status=status.HTTP_200_OK,
        )


# Exercicio 2 Apostila 3
class DuplicarTarefaAPIView(APIView):
    """
    Endpoint para duplicar uma tarefa existente.
    POST /api/tarefas/<pk>/duplicar/
    """

    def post(self, request, pk, format=None):
        try:
            tarefa_original = get_object_or_404(Tarefa, pk=pk, deletada=False)
        except Tarefa.DoesNotExist:
            return Response(
                {"error": "Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND
            )

        # Cria uma cópia da tarefa
        tarefa_original.pk = None  # remove a chave primária para gerar nova
        tarefa_original.concluida = False  # duplicada começa como pendente
        tarefa_original.data_conclusao = None  # limpa data de conclusão
        tarefa_original.deletada = False  # não marcada como deletada
        tarefa_original.save()

        serializer = TarefaSerializer(tarefa_original)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class MinhaView(APIView):
# Adicionando a permissão
    permission_classes = [IsAuthenticated]
    def get(self, request):
# Se chegou aqui, request.user é SEMPRE um objeto User logado
        print(f"Usuário autenticado: {request.user.username}")

class TarefaListCreateAPIView(generics.ListCreateAPIView):
    """Lista tarefas e permite a criação de novas tarefas. PROTEGIDA: Requer autenticação JWT."""

    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]  # ← Proteção
    
    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

    # MÉTODO CHAVE: Injeta o usuário logado antes de salvar o objeto
    def perform_create(self, serializer):
        """Associa a tarefa ao usuário logado (request.user) automaticamente."""
        # request.user é garantido como autenticado pelo IsAuthenticated
        serializer.save(user=self.request.user)
# A URL deve apontar para esta view em core/urls.py
# path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefa-list-create'),

class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhes de tarefa, atualização e exclusão.
    PROTEGIDA: Requer autenticação JWT.
    """

    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]  # ← Proteção

# A URL deve apontar para esta view em core/urls.py
# path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefa-detail'),

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Adiciona o token à lista negra
            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT  # 205 = "reset content"
            )
        except Exception:
            # Captura exceções como token inválido ou já expirado
            return Response(
                {"detail": "Token inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )
class CustomTokenObtainPairView(TokenObtainPairView):
#View que usa o serializer customizado."""
    serializer_class = CustomTokenObtainPairSerializer