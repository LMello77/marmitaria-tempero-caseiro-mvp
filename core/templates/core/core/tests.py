from decimal import Decimal
from django.test import TestCase
from .models import ItemCardapio, Pedido

class PedidoSegurancaTestCase(TestCase):
    def setUp(self):
        self.item = ItemCardapio.objects.create(
            nome_prato='Virado à Paulista',
            descricao_acompanhamentos='Arroz, tutu, bisteca, ovo e couve',
            preco_p=Decimal('18.00'),
            preco_m=Decimal('22.00'),
            preco_g=Decimal('26.00'),
            ativo=True,
        )

    def test_calculo_automatico_tamanho_m(self):
        pedido = Pedido(item=self.item, tamanho_marmita='M')
        self.assertEqual(pedido.calcular_total(), Decimal('22.00'))

    def test_bloqueio_acesso_anonimo_painel_cozinha(self):
        response = self.client.get('/cozinha/')
        self.assertEqual(response.status_code, 302)
