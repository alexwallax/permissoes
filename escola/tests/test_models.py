from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User



from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from django.contrib.auth import authenticate



class ModelEstudanteTesteCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "teste do modelo estudante",
            email = "teste@gmail.com",
            cpf = "09225248075",
            data_nascimento = "2022-03-23",
            celular = "88 98888-4444"
        )

    def test_verifica_atributos_de_estudantes(self):
        ''' teste os atributos de um estudante quando ele é criado BD '''
        self.assertEqual(self.estudante.nome, "teste do modelo estudante")
        self.assertEqual(self.estudante.email, "teste@gmail.com")
        self.assertEqual(self.estudante.cpf, "09225248075")
        self.assertEqual(self.estudante.data_nascimento, "2022-03-23")
        self.assertEqual(self.estudante.celular, "88 98888-4444")

#-----------------------------------------------------------------------------

class ModelCursoTesteCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = "teste curso",
            descricao = "curso python",
            nivel = "B",
        )

    def test_verifica_atributos_de_curso(self):
        ''' teste os atributos de um curso quando ele é criado BD '''
        self.assertEqual(self.curso.codigo, "teste curso")
        self.assertEqual(self.curso.descricao, "curso python")
        self.assertEqual(self.curso.nivel, "B")

#------------------------------------------------------------------------------
