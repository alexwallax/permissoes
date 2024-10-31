
'''



'''


from django.test import TestCase
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursoSerializerTestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            'codigo': 'PYT101',
            'descricao': 'Curso de Python para iniciantes.',
            'nivel': 'B'  
        }
        
        self.invalid_data = {
            'codigo': 'P', 
            'descricao': '',  
            'nivel': 'X' 
        }

    def test_valid_serializer(self):
        serializer = CursoSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['codigo'], self.valid_data['codigo'])
        self.assertEqual(serializer.validated_data['descricao'], self.valid_data['descricao'])
        self.assertEqual(serializer.validated_data['nivel'], self.valid_data['nivel'])

    def test_invalid_serializer(self):
        serializer = CursoSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('codigo', serializer.errors)  
        self.assertIn('descricao', serializer.errors)  
        self.assertIn('nivel', serializer.errors)  
