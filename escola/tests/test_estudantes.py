from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from escola.models import Estudante


class EstudanteAPITests(APITestCase):

    def setUp(self):
        self.url = reverse('Estudantes-list')  # Ajuste se necessário
        self.estudante_data = {
            'nome': 'Maria Silva',
            'email': 'maria@example.com',
            'cpf': '12345678901',
            'data_nascimento': '2000-01-01',
            'celular': '11987654321'
        }

    def test_create_estudante(self):
        response = self.client.post(self.url, self.estudante_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estudante.objects.count(), 1)
        self.assertEqual(Estudante.objects.get().nome, 'Maria Silva')

    def test_get_estudante(self):
        estudante = Estudante.objects.create(**self.estudante_data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], estudante.nome)

    def test_update_estudante(self):
        estudante = Estudante.objects.create(**self.estudante_data)
        update_data = {'nome': 'Maria Oliveira'}
        response = self.client.patch(reverse('estudante-detail', args=[estudante.id]), update_data, format='json')
        estudante.refresh_from_db()
        self.assertEqual(estudante.nome, 'Maria Oliveira')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_estudante(self):
        estudante = Estudante.objects.create(**self.estudante_data)
        response = self.client.delete(reverse('estudante-detail', args=[estudante.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Estudante.objects.count(), 0)

    def test_invalid_cpf(self):
        invalid_data = self.estudante_data.copy()
        invalid_data['cpf'] = '123'  # CPF inválido
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



