from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from django.utils.timezone import now
from .models import Transacao
from .serializers import TransacaoSerializer
from usuarios.models import Usuario


class TransacaoView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        id_usuario = request.data.get('idUsuario')

        if not id_usuario:
            return Response({"error": "ID do usuário não fornecido."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario = Usuario.objects.get(id=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario=usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransacoesPorMesView(ListAPIView):
    serializer_class = TransacaoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        mes = self.request.query_params.get('mes', now().month)
        ano = self.request.query_params.get('ano', now().year)
        return Transacao.objects.filter(
            idUsuario=self.request.user,
            data__year=ano,
            data__month=mes
        )

class TransacaoFilterView(generics.ListAPIView):
    serializer_class = TransacaoSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        mes = self.kwargs['mes']
        ano = self.kwargs['ano']
        tipo = self.kwargs['tipo']  # 'receita' ou 'despesa'

        # Filtra as transações com base no usuário, mês, ano e tipo
        queryset = Transacao.objects.filter(
            usuario_id=usuario_id,
            tipo=tipo,
            data__month=mes,
            data__year=ano
        )
        return queryset

class ResumoTransacoesView(APIView):
    def get(self, request, usuario_id, mes, ano):
        # Filtra as receitas e despesas para o usuário e o mês/ano informados
        receitas = Transacao.objects.filter(
            usuario_id=usuario_id,
            tipo='receita',
            data__month=mes,
            data__year=ano
        ).aggregate(soma_receitas=Sum('valor'))  # Soma das receitas

        despesas = Transacao.objects.filter(
            usuario_id=usuario_id,
            tipo='despesa',
            data__month=mes,
            data__year=ano
        ).aggregate(soma_despesas=Sum('valor'))  # Soma das despesas

        # Se não houver receitas ou despesas, define 0 como padrão
        soma_receitas = receitas['soma_receitas'] or 0
        soma_despesas = despesas['soma_despesas'] or 0

        # Monta o dicionário de resposta
        resumo = {
            'receitas': soma_receitas,
            'despesas': soma_despesas,
            'competencia': f'{mes}/{ano}'
        }

        return Response(resumo)


class ExcluirTransacaoView(APIView):
    def delete(self, request, usuario_id, transacao_id):
        try:
            # Buscando a transação pelo ID e associando ao usuário
            transacao = Transacao.objects.get(id=transacao_id, usuario_id=usuario_id)
        except Transacao.DoesNotExist:
            return Response({"detail": "Transação não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Excluindo a transação
        transacao.delete()
        return Response({"detail": "Transação excluída com sucesso."}, status=status.HTTP_204_NO_CONTENT)


class AtualizarTransacaoView(APIView):
    def patch(self, request, usuario_id, transacao_id):
        try:
            # Buscando a transação pelo ID e associando ao usuário
            transacao = Transacao.objects.get(id=transacao_id, usuario_id=usuario_id)
        except Transacao.DoesNotExist:
            return Response({"detail": "Transação não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Atualizando os campos com os dados do request (parcial)
        serializer = TransacaoSerializer(transacao, data=request.data, partial=True)

        # Validando os dados
        if serializer.is_valid():
            # Salvando as mudanças na transação
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)