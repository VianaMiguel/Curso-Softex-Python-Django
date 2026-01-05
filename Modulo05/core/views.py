from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Tarefa
from .serializers import (
    TarefaSerializer,
    CustomTokenObtainPairSerializer,
    UserRegistrationSerializer,
)
from .permissions import IsGerente  # Permissão customizada
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)


class ListaTarefasAPIView(APIView):
    """
    View para listar e criar tarefas.
    Endpoints:
    GET /api/tarefas/ - Lista todas as tarefas
    POST /api/tarefas/ - Cria uma nova tarefa
    """

    def get(self, request, format=None):
        user_id = request.query_params.get("user_id")
        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            tarefas = Tarefa.objects.all()

        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"[INFO]: Tarefa criada: {serializer.data['id']}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"[WARNING]: Validação falhou: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response(
                {"error": "[ERROR]: Violação de integridade no banco de dados."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
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

    def get(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        serializer = TarefaSerializer(tarefa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContagemTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        return Response(
            {"total": total, "concluidas": concluidas, "pendentes": pendentes},
            status=status.HTTP_200_OK,
        )


class DuplicarTarefaAPIView(APIView):
    """
    Endpoint para duplicar uma tarefa existente.
    POST /api/tarefas/<pk>/duplicar/
    """

    def post(self, request, pk, format=None):
        tarefa_original = get_object_or_404(Tarefa, pk=pk, deletada=False)
        tarefa_original.pk = None
        tarefa_original.concluida = False
        tarefa_original.data_conclusao = None
        tarefa_original.deletada = False
        tarefa_original.save()

        serializer = TarefaSerializer(tarefa_original)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MinhaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(f"Usuário autenticado: {request.user.username}")


class TarefaListCreateAPIView(generics.ListCreateAPIView):
    """Lista tarefas e permite a criação de novas tarefas. PROTEGIDA: Requer autenticação JWT."""

    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tarefa.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalhes de tarefa, atualização e exclusão.
    PROTEGIDA: Requer autenticação JWT.
    """

    serializer_class = TarefaSerializer

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)

    def get_permissions(self):
        """
        Define permissões dependendo do método HTTP.
        """
        if self.request.method == "DELETE":
            return [IsAuthenticated(), IsGerente()]
        return [IsAuthenticated()]


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"detail": "Logout realizado com sucesso."},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception:
            return Response(
                {"detail": "Token inválido."}, status=status.HTTP_400_BAD_REQUEST
            )


class CustomTokenObtainPairView(TokenObtainPairView):
    """View que usa o serializer customizado."""
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    Endpoint para cadastro de novos usuários.
    Acesso: Público (Qualquer um pode criar conta).
    """

    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
