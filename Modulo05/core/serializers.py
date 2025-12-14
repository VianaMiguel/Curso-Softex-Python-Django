from rest_framework import serializers
from .models import Tarefa


class TarefaSerializer(serializers.ModelSerializer):
    """
    Serializer para o Model Tarefa.
    Responsabilidades:
    1. Converter Tarefa → JSON (serialização)
    2. Converter JSON → Tarefa (desserialização)
    3. Validar dados de entrada
    """

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
        read_only_fields = ["id", "criada_em"]

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
