from django.db.models import Sum
from .models import Pedido

def consolidar_fechamento_diario(data_consulta):
    pedidos_concluidos = Pedido.objects.filter(
        data_hora_pedido__date=data_consulta,
        status_pedido='Concluido'
    )
    totais_por_pagamento = (
        pedidos_concluidos
        .values('forma_pagamento')
        .annotate(subtotal=Sum('valor_total'))
    )
    mensalistas = pedidos_concluidos.filter(forma_pagamento='Mensalista')
    return {
        'totais': list(totais_por_pagamento),
        'mensalistas': mensalistas,
    }
