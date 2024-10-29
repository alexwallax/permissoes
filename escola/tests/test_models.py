from django.test import TestCase
from escola.models import Estudante

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
