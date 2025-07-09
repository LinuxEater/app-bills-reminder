from datetime import timedelta
from django.db import models

class Conta(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    pago = models.BooleanField(default=False)

    # Novos campos:
    recorrente = models.BooleanField(default=False)
    intervalo_meses = models.PositiveIntegerField(default=1, blank=True, null=True)  # Quantos meses depois
    ultima_geracao = models.DateField(blank=True, null=True)  # Para controle interno

    def __str__(self):
        return self.titulo
    
