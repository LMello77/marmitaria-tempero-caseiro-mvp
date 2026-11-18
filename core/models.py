from django.db import models

class ItemCardapio(models.Model):
    nome_prato = models.CharField(max_length=120)
    descricao_acompanhamentos = models.TextField()
    preco_p = models.DecimalField(max_digits=6, decimal_places=2)
    preco_m = models.DecimalField(max_digits=6, decimal_places=2)
    preco_g = models.DecimalField(max_digits=6, decimal_places=2)
    data_cardapio = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        unique_together = ('nome_prato', 'data_cardapio')

    def __str__(self):
        return self.nome_prato


class Pedido(models.Model):
    TAMANHOS = [('P', 'Pequena'), ('M', 'Média'), ('G', 'Grande')]
    PAGAMENTOS = [('Pix', 'Pix'), ('Dinheiro', 'Dinheiro'), ('Cartao', 'Cartão'), ('Mensalista', 'Mensalista')]
    STATUS = [
        ('Recebido', 'Recebido'),
        ('Em Preparo', 'Em Preparo'),
        ('Saiu para Entrega', 'Saiu para Entrega'),
        ('Concluido', 'Concluído'),
    ]

    item = models.ForeignKey(ItemCardapio, on_delete=models.PROTECT)
    nome_cliente = models.CharField(max_length=100)
    telefone_contato = models.CharField(max_length=20)
    tamanho_marmita = models.CharField(max_length=1, choices=TAMANHOS)
    observacoes = models.CharField(max_length=250, blank=True)
    endereco_entrega = models.CharField(max_length=255)
    forma_pagamento = models.CharField(max_length=20, choices=PAGAMENTOS)
    valor_total = models.DecimalField(max_digits=7, decimal_places=2)
    status_pedido = models.CharField(max_length=25, choices=STATUS, default='Recebido')
    data_hora_pedido = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        precos = {'P': self.item.preco_p, 'M': self.item.preco_m, 'G': self.item.preco_g}
        return precos[self.tamanho_marmita]
