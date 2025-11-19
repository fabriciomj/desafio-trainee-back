import re

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

NOME_PESSOA_PAT = re.compile(
    r"""
    ^(?!\s)                                                             # Não pode começar com espaço
    [A-ZÀ-ÂÈ-ÊÌ-ÎÒ-ÔÙ-Û][a-zà-ãç-êì-îò-õù-û]+                           # Um prenome
    ((\ (da|das|do|dos))?\ [A-ZÀ-ÂÈ-ÊÌ-ÎÒ-ÔÙ-Û][a-zà-ãç-êì-îò-õù-û]+)+  # Espaço mais sobrenome, com conjução opcional, 1+ vezes
    (?<!\s)$                                                            # Não pode terminar com espaço
    """,
    re.VERBOSE,
)


class MyUser(AbstractUser):
    class TipoUsuario(models.TextChoices):
        CLIENTE = "CL", "Cliente"
        ESTABELECIMENTO = "ES", "Estabelecimento"

    tipo = models.CharField(max_length=2, choices=TipoUsuario)


class Cliente(models.Model):
    TELEFONE_PAT = re.compile(
        r"""
    ^([14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])   # Possíveis DDDs do Brasil
    9[0-9]{8}$                                              # Um 9 seguido de 8 digitos
    """,
        re.VERBOSE,
    )

    nome = models.CharField(max_length=80, validators=[RegexValidator(NOME_PESSOA_PAT)])
    telefone = models.CharField(
        max_length=11, unique=True, validators=[RegexValidator(TELEFONE_PAT)]
    )
    endereco = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    formas_pagamento = models.ManyToManyField("FormaPagamento", blank=True)
    carrinho = models.OneToOneField("Carrinho", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Estabelecimento(models.Model):
    NOME_EMPRESA_PAT = re.compile(
        r"""
        ^(?!\s)     # Não pode começar com espaço
        \S+         # Palavra com qualquer char não espaço
        (\ \S+)*    # Um espaço seguido de uma palavra com qualquer char não espaço, 0+ vezes
        (?<!\s)$    # Não pode terminar com espaço
        """,
        re.VERBOSE,
    )

    nome = models.CharField(
        max_length=50, validators=[RegexValidator(NOME_EMPRESA_PAT)], blank=True
    )
    endereco = models.CharField(max_length=100)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class FormaPagamento(models.Model):
    numero_cartao = models.CharField(
        max_length=16, validators=[RegexValidator(r"^[0-9]{16}$")]
    )
    nome_titular = models.CharField(
        max_length=20, validators=[RegexValidator(NOME_PESSOA_PAT)]
    )

    def __str__(self):
        return self.numero_cartao

    def save(self, **kwargs):  # pyright: ignore[reportIncompatibleMethodOverride]
        self.nome_titular = self.nome_titular.capitalize()
        super().save(**kwargs)


class Prato(models.Model):
    nome = models.CharField(max_length=50)
    ingredientes = models.TextField()
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    ofertas = models.ManyToManyField("Oferta", blank=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Seu Carrinho - {self.estabelecimento.nome}"


class Oferta(models.Model):
    data = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prato.estabelecimento.nome} - {self.prato.nome} ({self.data})"


class Pedido(models.Model):
    class Status(models.TextChoices):
        RECEBIDO = "RE", "Pedido Recebido"
        PREPARANDO = "PR", "Pedido em Preparo"
        DELIVERY = "DL", "À Caminho"
        ENTREGUE = "EN", "Entregue"

    status = models.CharField(max_length=2, choices=Status, default=Status.RECEBIDO)
    data = models.DateField(auto_now_add=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    ofertas = models.ManyToManyField(Oferta)

    def __str__(self):
        return f"{self.cliente.nome} - {self.estabelecimento.nome} ({self.data})"
