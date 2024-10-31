from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status



class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
        self.url = reverse('Estudantes-list')


    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um user com as credenciais corretas"""
        usuario = authenticate(username = 'admin',password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
    
    def test_autenticacao_user_com_username_incorreto(self):
        """Teste que verifica a autenticação com username incorreto"""
        usuario = authenticate(username = 'admn2',password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
    
    def test_autenticacao_user_com_password_incorreto(self):
        """Teste que verifica a autenticação com password incorreto"""
        password = authenticate(username = 'admin',password='adminnnnnnn')
        self.assertFalse((password is not None) and password.is_authenticated)

    def test_get_request(self):
        self.client.force_authenticate(user=self.usuario)
        response = self.client.get(reverse('Estudantes-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

