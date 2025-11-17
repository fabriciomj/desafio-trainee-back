from django.contrib.auth.models import Group, User
from rest_framework import serializers

from fabricio.mini_ifood.models import (
    Carrinho,
    Cliente,
    Endereco,
    Estabelecimento,
    FormaPagamento,
    Oferta,
    Pedido,
    Prato,
)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ["ofertas"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["nome", "telefone", "formas_pagamento", "carrinho", "enderecos"]


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ["cep", "rua", "numero", "bairro", "cidade", "estado", "complemento"]


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ["cnpj", "razao_social", "nome_fantasia", "telefone", "endereco"]


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = ["numero_cartao", "nome_titular"]


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = ["data", "valor", "quantidade", "prato"]


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ["status", "estabelecimento", "cliente", "ofertas"]


class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prato
        fields = ["nome", "ingredientes", "estabelecimento"]
