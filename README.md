# Desafio Trainee EJECT API Mini iFood

## Sobre o projeto

Uma API REST simulando uma Mini iFood.

## Instalação e Execução
1. No seu terminal, clone o repositório.
    ```
    git clone https://github.com/fabriciomj/desafio-trainee-back.git
    ``` 
2. Acesse a pasta criada com o comando `cd`.
    ```
    cd desafio-trainee-back
    ``` 
3. Sincronize as dependências de projetos com o `uv`:
    ```
    uv sync
    ```
4. Realize as migrações do projeto.
    ```
    uv run .\manage.py migrate
    ```
5. Crie um super usuário para ter permissões de administrador na API.
    ```
    uv run .\manage.py createsuperuser
    ```
6. Execute esse comando para rodar o projeto.
    ```
    uv run .\manage.py runserver
    ``` 
7. Acesse no seu navegador a seguinte url:
    ```
    http://127.0.0.1:8000/
    ```

## Instruções de uso da API


## Documentação da API
É possível acessar a documentação da API para visualizar todos os endpoints disponíveis na API. Com o servidor funcionando, acesse:
```
127.0.0.1:8000/swagger
```

## Dependências
Para garantir que o projeto funcione corretamente, certifique-se de possuir o gerenciador de pacotes [`uv`](https://github.com/astral-sh/uv). 
- Python 3.14  
- Django 5.2.7  
- Django REST framework 3.16.1
- Git
- uv 0.9.1