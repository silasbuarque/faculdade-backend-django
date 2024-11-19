from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Usuario


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        senha = data.get('senha')

        # Autentica o usuário com email e senha
        user = authenticate(email=email, password=senha)

        if user is None:
            raise serializers.ValidationError("Credenciais inválidas.")

        return user

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)  # Para garantir que a senha seja apenas para escrita

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'email', 'senha']

    def create(self, validated_data):
        senha = validated_data.pop('senha')  # Remove a senha para tratá-la separadamente
        usuario = Usuario.objects.create(**validated_data)
        usuario.set_password(senha)  # Criptografa a senha
        usuario.save()  # Salva o usuário com a senha criptografada
        return usuario