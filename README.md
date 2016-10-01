# [Academic Job Board](https://github.com/academichero/jobs) ![Travis CI badge](https://travis-ci.org/academichero/jobs.svg?branch=master)

O Job Board é uma plataforma online que permite o encontro perfeito entre a
busca por vagas no mercado de trabalho e a busca por profissionais qualificados.

Feito com <3 usando [Python](https://www.python.org) e
[Django](https://www.djangoproject.com).

## Como instalar

Se você estiver utilizando uma distro baseada no Debian (ex.: Ubuntu), precisará
instalar alguns pacotes:

```
$ sudo apt-get install libncurses-dev g++ git-core
```

Usamos Python 3.5 e Django 1.9. Seu ambiente precisa atender esses requisitos.

<!--
TODO: Adicionar instruções de instalação do Python [e caso necessário do Django
também] à linha de comando abaixo. Instruções para OS X também conta? :-)
-->
```
$ sudo apt-get install python
```

Clone o projeto:

```
$ git clone https://github.com/academichero/jobs.git
```

Crie um ambiente virtual ([virtualenv](https://pypi.python.org/pypi/virtualenv))
para instalação das dependências:

```
$ cd jobs && python3 -m venv ambiente
$ source ambiente/bin/activate
$ pip install -r deploy/requirements-dev.txt
```

_Para mais informações sobre o virtualenv, acesse
[virtualenv.pypa.io](https://virtualenv.pypa.io/)._

Duplique o arquivo de configuração de exemplo `app/settings.sample.py`. Ele já
contém todas as configurações necessárias para você rodar a aplicação em
ambiente de desenvolvimento:

```
$ cp app/settings.sample.py app/settings.py
```

Crie o banco de dados:

```
python manage.py migrate
```

## Como executar

```
python manage.py runserver
```

Você deverá ver essa mensagem:

```
Performing system checks...

System check identified no issues (0 silenced).
Django version 1.9.7, using settings 'app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

A aplicação estará disponível em [localhost:8000](http://localhost:8000).

## Como contribuir

Usamos [GitHub Flow](https://guides.github.com/introduction/flow/):

1. Faça um fork do repositório
1. Faça suas alterações no seu repositório
1. Envie um pull request
