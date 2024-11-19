from django.urls import path
from .views import CadastroUsuarioView, LoginView

urlpatterns = [
    path('cadastro/', CadastroUsuarioView.as_view(), name='cadastro_usuario'),
    path('login/', LoginView.as_view(), name='login'),
]
