import unittest
from ..model.calculadora import Calculadora

class testCal(unittest.TestCase):
    def test_multiplicacao(self):
        self.assertEqual(Calculadora().Multiplicacao(2,2),4)
        # self.assertEqual()