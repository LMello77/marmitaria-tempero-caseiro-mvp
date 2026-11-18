from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import ItemCardapio, Pedido

def cardapio_publico(request):
    itens = ItemCardapio.objects.filter(ativo=True)
    return render(request, 'core/cardapio.html', {'itens': itens})

@require_POST
def criar_pedido(request, item_id):
    item = get_object_or_404(ItemCardapio, id=item_id, ativo=True)
    pedido = Pedido(
        item=item,
        nome_cliente=request.POST.get('nome_cliente', '').strip(),
        telefone_contato=request.POST.get('telefone_contato', '').strip(),
        tamanho_marmita=request.POST.get('tamanho_marmita', 'M'),
        observacoes=request.POST.get('observacoes', '').strip(),
        endereco_entrega=request.POST.get('endereco_entrega', '').strip(),
        forma_pagamento=request.POST.get('forma_pagamento', 'Pix'),
    )
    pedido.valor_total = pedido.calcular_total()
    pedido.save()
    return render(request, 'core/confirmacao.html', {'pedido': pedido})

@login_required
def painel_cozinha(request):
    pedidos = Pedido.objects.exclude(status_pedido='Concluido').order_by('data_hora_pedido')
    return render(request, 'core/cozinha.html', {'pedidos': pedidos})

@login_required
@require_POST
def avancar_status(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    fluxo = {'Recebido': 'Em Preparo', 'Em Preparo': 'Saiu para Entrega', 'Saiu para Entrega': 'Concluido'}
    if pedido.status_pedido in fluxo:
        pedido.status_pedido = fluxo[pedido.status_pedido]
        pedido.save()
    return redirect('painel_cozinha')
