import unittest
from ..model.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_multiplicacao(self):
        self.assertEqual(Calculadora().Multiplicacao(2,2),4)
        # self.assertEqual(Calculadora().Multiplicacao(3,1),3)
        # self.assertEqual(Calculadora().Multiplicacao(0,5),0)
        # self.assertEqual(Calculadora().Multiplicacao(-1,1),-1)
        # self.assertEqual(Calculadora().Multiplicacao(2,-1),-2)

if __name__=='__main__':
    unittest.main()