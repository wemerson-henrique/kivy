import sys
sys.path.append(r"C:\Users\WEMERSON\Documents\GitHub\kivy\meusExemplos\calculadora")

import unittest
from model.calculadora import Calculadora


cal = Calculadora()

class TestCalculadoraSubtracao(unittest.TestCase):
    def testCasoDeSucesso(self):
        self.assertEqual(cal.subtracao(10,5),5)