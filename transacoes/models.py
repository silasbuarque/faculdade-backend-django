from django.db import models
from usuarios.models import Usuario

class Transacao(models.Model):

    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    data = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='transacoes')

    def __str__(self):
        return f'{self.tipo.capitalize()} - {self.descricao}'