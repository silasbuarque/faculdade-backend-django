# serializers.py
from rest_framework import serializers

from usuarios.models import Usuario
from .models import Transacao

class TransacaoSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), required=False)

    class Meta:
        model = Transacao
        fields = ['id', 'valor', 'descricao', 'tipo', 'data', 'usuario']  # Ajuste os campos conforme necessário