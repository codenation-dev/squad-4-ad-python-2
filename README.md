# Gestão de comissões Televendas

[Descrição do projeto](descricao.md)

### Equipe | Squad 4:

- [Fábio Matheus Mantelli](https://github.com/fabiomantelli)
- [Fillipe Calza](https://github.com/fcalza)
- [Julio Cezar Riffel](https://github.com/julioriffel)
- [Luan Fernando de Souza Ferreira](https://github.com/luanfsf)
- [Paulo Rogerio Kraemer](https://github.com/paulork)


### Requisitos

- [Python](https://www.python.org/downloads/) (3.7) 
- [Pipenv](https://pypi.org/project/pipenv/2018.11.26/) (2018.11.26)
- [git](https://git-scm.com/) (2) 

### Instalação

```
$ git clone git@github.com:codenation-dev/squad-4-ad-python-2.git
$ cd squad-4-ad-python-2

$ pip install pipenv

$ pipenv install
```

> Ao executar o comando `$ pipenv install`, um ambiente virtual será criado automaticamente, caso não haja um ambiente virtual já ativo.

Para verificar o caminho do ambiente virtual criado, execute `$ pipenv --venv`.

Para acessar o ambiente ativo, execute `$ pipenv shell`


### Execução

```
$ ./manage.py migrate
$ ./manage.py runserver [host]:[port]
```

- Using Docker & docker-compose
> requires [docker](link) and [docker-compose](link)
```
$ docker-compose build [web db]
$ docker-compose up [web db] [-d]
```

### Testes

```
$ ./manage.py test
```