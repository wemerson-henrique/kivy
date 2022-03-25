import unittest
from exemplo1 import Soma, Dividir

class TestSoma(unittest.TestCase):
    
    def test_retornar_introducao(self):
        self.assertEqual(Soma(2, 3),5)
        self.assertEqual(Soma(-2, 3),1)
        self.assertEqual(Soma(2000, 3),2003)

    def test_tipo_de_parametro(self):
        self.assertRaises(TypeError,Soma,'2','2')
        self.assertRaises(TypeError,Soma,2,'2')
        self.assertRaises(TypeError,Soma,'2',2)
        self.assertRaises(TypeError,Soma,False,2)
        self.assertRaises(TypeError,Soma,1+2j,2)
        self.assertRaises(TypeError,Soma,2,True)
        self.assertRaises(TypeError,Soma,2,1+2j)
        self.assertRaises(TypeError,Soma,2.5,2)
        self.assertRaises(TypeError,Soma,2,2.5)

    def test_dvisao_por_zero(self):
        self.assertRaises(ZeroDivisionError,Dividir,2,0)

    # def test_pessoa(self):
    #     pessoa1 = Pessoa('Ana', 15)
    #     self.assertEqual(pessoa1.ApresentarSe(),print("Meu nome é {0} e tenho {1} anos".format('Ana',15)))