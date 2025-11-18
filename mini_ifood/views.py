from django.contrib.auth.models import Group, User
from rest_framework import generics, permissions, viewsets

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
    GroupSerializer,
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


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarrinhoList(generics.ListCreateAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


class CarrinhoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer


class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class EnderecoList(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class EnderecoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class EstabelecimentoList(generics.ListCreateAPIView):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer


class EstabelecimentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer


class FormaPagamentoList(generics.ListCreateAPIView):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer


class FormaPagamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer


class OfertaList(generics.ListCreateAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer


class OfertaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer


class PedidoList(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PratoList(generics.ListCreateAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer


class PratoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
