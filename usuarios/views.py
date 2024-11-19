from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import LoginSerializer
from .serializers import UsuarioSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data  # Isso agora será o usuário autenticado
            return Response({
                "idUsuario": user.id,
                "mensagem": "Bem-vindo"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CadastroUsuarioView(APIView):
    def post(self, request):
        # Verificar se o email já existe
        email = request.data.get('email')
        if Usuario.objects.filter(email=email).exists():
            return Response({
                'mensagem': 'Este email já está em uso!'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Criar o usuário a partir dos dados validados
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()

            # Criptografar a senha antes de salvar
            senha = request.data.get('senha')
            if senha:
                usuario.set_password(senha)  # Criptografa a senha

            usuario.save()  # Salva o usuário com a senha criptografada

            return Response({
                'idUsuario': usuario.id,  # Retorna o ID do usuário
                'mensagem': 'Usuário cadastrado com sucesso!'
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)