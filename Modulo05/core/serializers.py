from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from .models import Tarefa
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User 





class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para o Model Tarefa.
    Responsabilidades:
    1. Converter Tarefa → JSON (serialização)
    2. Converter JSON → Tarefa (desserialização)
    3. Validar dados de entrada
    """
    """
    Serializer para Tarefa com segurança.
    O campo 'user' é exibido (read-only) mas NÃO aceito na entrada."""
    # 1. Mostra o username do usuário em vez do ID (read-only na saída)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Tarefa
        fields = [
            "id",
            "user",
            "titulo",
            "descricao",
            "concluida",
            "prioridade",
            "prazo",
            "criada_em",
            "data_conclusao",
            "deletada",
        ]
        # Campos gerados automaticamente (não aceitos na entrada)
        read_only_fields = ["id", 'user', "criada_em"]

    # Exercico 1 Apostila 3
    def create(self, validated_data):
        # Se criar já concluída, preenche data_conclusao
        concluida = validated_data.get("concluida", False)
        if concluida:
            validated_data["data_conclusao"] = timezone.now()
        return super().create(validated_data)

    # Exercico 1 Apostila 3
    def update(self, instance, validated_data):
        concluida = validated_data.get("concluida", instance.concluida)

        # Se marcar como concluída e ainda não tem data, preenche automaticamente
        if concluida and not instance.data_conclusao:
            instance.data_conclusao = timezone.now()

        # Se desmarcar concluída, limpa a data
        if not concluida:
            instance.data_conclusao = None

        return super().update(instance, validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer customizado para incluir campos extras no JWT."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adicionar campos customizados ao payload
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        return token
class CustomTokenObtainPairView(TokenObtainPairView):
    """View que usa o serializer customizado."""

    serializer_class = CustomTokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer): 
    # Definimos 'write_only=True' para que a senha seja aceita no cadastro (POST), # mas NUNCA seja devolvida na resposta (Response JSON). 
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'} ) 
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password'] 
        
        def create(self, validated_data):
            """ Intercepta a criação para usar o 'create_user' e hashear a senha. """ 
            # Extrai a senha dos dados validados 
            password = validated_data.pop('password') 
            user = User.objects.create_user( 
                username=username, 
                email=email, 
                password=password 
            )
        # 2. Lógica de Atribuição de Cargo (Role) 
            try: 
                # Busca o grupo 'Comum' 
                grupo_comum = Group.objects.get(name='Comum') 
                # Adiciona o usuário ao grupo 
                user.groups.add(grupo_comum) 
            except Group.DoesNotExist: 
                # Fallback: Se o grupo não existir, o usuário é criado sem grupo. 
                # Em produção, deveríamos logar um erro aqui. 
                pass 
                
            return user 