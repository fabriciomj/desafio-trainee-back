import re

from django.contrib.auth.models import User
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
TELEFONE_PAT = re.compile(
    r"""
    ^([14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])   # Possíveis DDDs do Brasil
    9[0-9]{8}$                                              # Um 9 seguido de 8 digitos
    """,
    re.VERBOSE,
)


class Cliente(User):
    nome = models.CharField(max_length=80, validators=[RegexValidator(NOME_PESSOA_PAT)])
    telefone = models.CharField(
        max_length=11, unique=True, validators=[RegexValidator(TELEFONE_PAT)]
    )
    formas_pagamento = models.ManyToManyField("FormaPagamento", blank=True)
    carrinho = models.OneToOneField("Carrinho", on_delete=models.PROTECT)
    enderecos = models.ManyToManyField("Endereco")


class Estabelecimento(User):
    cnpj = models.CharField(
        max_length=14, validators=[RegexValidator(r"^[0-9]{14}$")], unique=True
    )

    NOME_EMPRESA_PAT = re.compile(
        r"""
        ^(?!\s)     # Não pode começar com espaço
        \S+         # Palavra com qualquer char não espaço
        (\ \S+)*    # Um espaço seguido de uma palavra com qualquer char não espaço, 0+ vezes
        (?<!\s)$    # Não pode terminar com espaço
        """,
        re.VERBOSE,
    )
    razao_social = models.CharField(
        max_length=50, validators=[RegexValidator(NOME_EMPRESA_PAT)], unique=True
    )
    nome_fantasia = models.CharField(
        max_length=50, validators=[RegexValidator(NOME_EMPRESA_PAT)], blank=True
    )
    telefone = models.CharField(
        max_length=11, unique=True, validators=[RegexValidator(TELEFONE_PAT)]
    )
    endereco = models.OneToOneField("Endereco", on_delete=models.PROTECT)


class FormaPagamento(models.Model):
    numero_cartao = models.CharField(
        max_length=16, validators=[RegexValidator(r"^[0-9]{16}$")]
    )
    nome_titular = models.CharField(
        max_length=20, validators=[RegexValidator(NOME_PESSOA_PAT)]
    )

    def save(self, **kwargs):  # pyright: ignore[reportIncompatibleMethodOverride]
        self.nome_titular = self.nome_titular.capitalize()
        super().save(**kwargs)


class Prato(models.Model):
    nome = models.CharField(max_length=50)
    ingredientes = models.TextField()
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)


class Carrinho(models.Model):
    ofertas = models.ManyToManyField("Oferta", blank=True)


class Oferta(models.Model):
    data = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)


class Pedido(models.Model):
    class Status(models.TextChoices):
        PAGAMENTO = "PM", "Aguardando Pagamento"
        PAGO = "PG", "Pago"
        RECEBIDO = "RE", "Pedido Recebido"
        PREPARANDO = "PR", "Pedido em Preparo"
        DELIVERY = "DL", "À Caminho"
        ENTREGUE = "EN", "Entregue"

    status = models.CharField(max_length=2, choices=Status, default=Status.PAGAMENTO)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    ofertas = models.ManyToManyField(Oferta)


class Endereco(models.Model):
    class Estados(models.TextChoices):
        AC = "AC", "Acre"
        AL = "AL", "Alagoas"
        AP = "AP", "Amapá"
        AM = "AM", "Amazonas"
        BA = "BA", "Bahia"
        CE = "CE", "Ceará"
        DF = "DF", "Distrito Federal"
        ES = "ES", "Espirito Santo"
        GO = "GO", "Goiás"
        MA = "MA", "Maranhão"
        MT = "MT", "Mato Grosso"
        MS = "MS", "Mato Grosso do Sul"
        MG = "MG", "Minas Gerais"
        PA = "PA", "Pará"
        PB = "PB", "Paraíba"
        PR = "PR", "Paraná"
        PE = "PE", "Pernambuco"
        PI = "PI", "Piauí"
        RJ = "RJ", "Rio de Janeiro"
        RN = "RN", "Rio Grande do Norte"
        RS = "RS", "Rio Grande do Sul"
        RO = "RO", "Rondônia"
        RR = "RR", "Roraima"
        SC = "SC", "Santa Catarina"
        SP = "SP", "São Paulo"
        SE = "SE", "Sergipe"
        TO = "TO", "Tocantins"

    cep = models.CharField(max_length=8, validators=[RegexValidator(r"^[0-9]{8}$")])
    rua = models.CharField(max_length=80)
    numero = models.PositiveIntegerField()
    bairro = models.CharField(max_length=80)
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=2, choices=Estados)
    complemento = models.CharField(max_length=40)
