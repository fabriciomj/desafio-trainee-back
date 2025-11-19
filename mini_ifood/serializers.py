from rest_framework import serializers

from mini_ifood.models import (
    Carrinho,
    Cliente,
    Estabelecimento,
    FormaPagamento,
    Oferta,
    Pedido,
    Prato,
)


class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ["ofertas", "estabelecimento"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["nome", "telefone", "endereco", "formas_pagamento", "carrinho"]


class EstabelecimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ["url", "nome", "endereco"]


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = ["numero_cartao", "nome_titular"]


class OfertaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oferta
        fields = ["url", "data", "valor", "quantidade", "prato"]


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["status", "estabelecimento", "cliente", "ofertas"]


class PratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prato
        fields = ["url", "nome", "ingredientes", "estabelecimento"]
