from django.db import models

# Create your models here.
class Itens(models.Model):
    nome_produto = models.CharField(max_length=20)
    codigo_produto = models.CharField(max_length=30)
    quantidade = models.IntegerField(blank=False, null=False)
    valor_unitario = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    estoque_minimo = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['nome_produto']

    def __str__(self):
        return self.nome_produto
