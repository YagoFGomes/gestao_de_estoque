from django.db import models
from apps.cadastro_produtos.models import Itens

class Cliente(models.Model):
    nome = models.CharField(max_length=20, blank=False, null=False)
    sobrenome = models.CharField(max_length=50, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    endereco = models.CharField(max_length=50)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Itens, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField(blank=False, null=False)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)