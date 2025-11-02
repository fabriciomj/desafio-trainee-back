import re

from django.core.validators import RegexValidator
from django.db import models


class Cliente(models.Model):
    NOME_PAT = re.compile(
        r"""
        ^(?!\s)                                                             # Não pode começar com espaço
        [A-ZÀ-ÂÈ-ÊÌ-ÎÒ-ÔÙ-Û][a-zà-ãç-êì-îò-õù-û]+                           # Um prenome
        ((\ (da|das|do|dos))?\ [A-ZÀ-ÂÈ-ÊÌ-ÎÒ-ÔÙ-Û][a-zà-ãç-êì-îò-õù-û]+)+  # Espaço mais sobrenome, com conjução opcional, 1+ vezes
        (?<!\s)$                                                            # Não pode terminar com espaço
        """,
        re.VERBOSE,
    )
    nome = models.CharField(
        max_length=80,
        validators=[RegexValidator(NOME_PAT)],
    )

    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=30)

    TELEFONE_PAT = re.compile(
        r"""
        ^([14689][1-9]|2[12478]|3[1234578]|5[1345]|7[134579])   # Possíveis DDDs do Brasil
        9[0-9]{8}$                                              # Um 9 seguido de 8 digitos
        """,
        re.VERBOSE,
    )
    telefone = models.CharField(
        max_length=11,
        unique=True,
        validators=[RegexValidator(TELEFONE_PAT)],
    )


class Estabelecimento(models.Model):
    cnpj = models.CharField(
        max_length=14,
        validators=[RegexValidator(r"^[0-9]{14}$")],
        unique=True,
    )

    NOME_PAT = re.compile(
        r"""
        ^(?!\s)     # Não pode começar com espaço
        \S+         # Palavra com qualquer char não espaço
        (\ \S+)*    # Um espaço seguido de uma palavra com qualquer char não espaço, 0+ vezes
        (?<!\s)$    # Não pode terminar com espaço
        """,
        re.VERBOSE,
    )
    razao_social = models.CharField(
        max_length=50,
        validators=[RegexValidator(NOME_PAT)],
        unique=True,
    )
    nome_fantasia = models.CharField(
        max_length=50,
        validators=[RegexValidator(NOME_PAT)],
        blank=True,
    )
