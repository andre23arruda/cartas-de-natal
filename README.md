<h1 align="center">
    API para Cartas de Natal
</h1>

<p align="center">
 <img src="https://img.shields.io/static/v1?label=PRs&message=welcome&color=7159c1&labelColor=000000" alt="PRs welcome!" />

  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=7159c1&labelColor=000000">
</p>

<p align="center">
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>
  <a href="#-dificuldades">Dificuldades</a>
</p>

## :rocket: Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [djangorestframework-jwt](https://pypi.org/project/djangorestframework-jwt/)

## 💻 Projeto

- Desenvolver um CRUD de envio e leitura de cartinhas de Natal para o Papai Noel e
disponibilizá-lo como uma REST API.
- Hospedado em Heroku: <a href="https://andre23arruda-zappts.herokuapp.com/swagger/">Clique aqui</a>
- Criação de testes de unidade juntamente com o desenvolvimento da aplicação
- Utilização de autenticação JWT para acesso aos endpoints
![Swagger doc](/images/swagger_1.png?raw=true)


## Testes
### Para rodar os testes localmente:

- Tenha o Python instalado em sua máquina
- Renomeie o arquivo env_example.py para env.py
- e rode no terminal:
```sh
    python -m venv venv
    . venv/Scripts/activate
    pip install -r requirements.txt
    python manage.py tests
```
![Testes](/images/testes_1.png?raw=true)


## Dificuldades

- Primeira vez utilizando JWT em testes de unidade
