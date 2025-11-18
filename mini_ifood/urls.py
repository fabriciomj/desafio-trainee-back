from django.urls import include, path
from rest_framework import routers

from mini_ifood import views

router = routers.DefaultRouter()

to_register = [
    (r"carrinhos", views.CarrinhoViewSet),
    (r"clientes", views.ClienteViewSet),
    (r"enderecos", views.EnderecoViewSet),
    (r"estabelecimentos", views.EstabelecimentoViewSet),
    (r"pagamentos", views.FormaPagamentoViewSet),
    (r"ofertas", views.OfertaViewSet),
    (r"pedidos", views.PedidoViewSet),
    (r"pratos", views.PratoViewSet),
]

for tup in to_register:
    router.register(tup[0], tup[1])

urlpatterns = [path("", include(router.urls))]
