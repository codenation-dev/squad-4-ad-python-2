from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class BaseApiTest(APITestCase):
    """
    Teste de base, possuí dados básicos para o testes

    Usuário base:
    username: luan
    password: senha@123
    """

    fixtures = [
        'fixtures/api.yaml',
        'fixtures/users.yaml',
    ]

    user = User.objects.get(username='luan')
