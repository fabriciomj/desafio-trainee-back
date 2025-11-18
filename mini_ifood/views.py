from rest_framework import permissions, viewsets

from mini_ifood.models import (
    Carrinho,
    Cliente,
    Estabelecimento,
    FormaPagamento,
    Oferta,
    Pedido,
    Prato,
)
from mini_ifood.permissions import IsAuthenticatedReadOnly, IsOwner
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
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner | IsAuthenticatedReadOnly,
    ]


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner | IsAuthenticatedReadOnly,
    ]


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


class PratoViewSet(viewsets.ModelViewSet):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner | IsAuthenticatedReadOnly,
    ]
