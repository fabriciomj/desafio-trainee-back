from rest_framework import viewsets

from mini_ifood.models import (
    Carrinho,
    Cliente,
    Estabelecimento,
    FormaPagamento,
    Oferta,
    Pedido,
    Prato,
)
from mini_ifood.serializers import (
    CarrinhoSerializer,
    ClienteSerializer,
    EstabelecimentoSerializer,
    FormaPagamentoSerializer,
    OfertaSerializer,
    PedidoSerializer,
    PratoSerializer,
)


class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer


class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PratoViewSet(viewsets.ModelViewSet):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
