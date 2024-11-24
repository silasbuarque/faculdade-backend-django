from django.urls import path
from .views import TransacaoView, TransacoesPorMesView, TransacaoFilterView, ResumoTransacoesView, ExcluirTransacaoView, \
    AtualizarTransacaoView

urlpatterns = [
    path('transacoes/', TransacaoView.as_view(), name='criar_transacao'),
    path('transacoes/mes/', TransacoesPorMesView.as_view(), name='transacoes_por_mes'),
    path('transacoes/<int:usuario_id>/<int:mes>/<int:ano>/<str:tipo>/', TransacaoFilterView.as_view(), name='filtrar_transacoes'),
    path('transacoes/resumo/<int:usuario_id>/<int:mes>/<int:ano>/', ResumoTransacoesView.as_view(), name='resumo_transacoes'),
    path('transacoes/atualizar/<int:usuario_id>/<int:transacao_id>/', AtualizarTransacaoView.as_view(),
         name='atualizar_transacao'),
    path('transacoes/excluir/<int:usuario_id>/<int:transacao_id>/', ExcluirTransacaoView.as_view(),
         name='excluir_transacao'),

]
