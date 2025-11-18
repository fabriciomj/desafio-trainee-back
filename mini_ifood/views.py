from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from mini_ifood.models import (
    Carrinho,
    Cliente,
    Endereco,
    Estabelecimento,
    FormaPagamento,
    Oferta,
    Pedido,
    Prato,
)
from mini_ifood.serializers import (
    CarrinhoSerializer,
    ClienteSerializer,
    EnderecoSerializer,
    EstabelecimentoSerializer,
    FormaPagamentoSerializer,
    OfertaSerializer,
    PedidoSerializer,
    PratoSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


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
