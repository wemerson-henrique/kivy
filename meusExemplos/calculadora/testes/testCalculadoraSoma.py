import sys
sys.path.append(r"C:\Users\WEMERSON\Documents\GitHub\kivy\meusExemplos\calculadora")

import unittest
from model.calculadora import Calculadora 

cal =  Calculadora()


class TestCalculadoraSoma(unittest.TestCase):
    def testCasoDeSucesso(self):
        self.assertEqual(cal.soma(2,3),5)
        self.assertEqual(cal.soma(2,2),4)
        self.assertEqual(cal.soma(3,2),5)
        self.assertEqual(cal.soma(-7,-7),-14)
        self.assertEqual(cal.soma(2,-7),-5)
        self.assertEqual(cal.soma(-7,13),6)
        self.assertEqual(cal.soma(5.0,3.0),8.0)
        self.assertEqual(cal.soma(7.0,2),9)
    
    def testParaMetroDeEntrada(self):
        self.assertRaises(TypeError,cal.soma("2","3"))
        self.assertRaises(TypeError,cal.soma("2",3))
        self.assertRaises(TypeError,cal.soma(2,"3"))
        self.assertRaises(TypeError,cal.soma([1,2,3],[1,2,3]))
        self.assertRaises(TypeError,cal.soma(1,[1,2,3]))
        self.assertRaises(TypeError,cal.soma((1,2,3),(1,2,3)))
        self.assertRaises(TypeError,cal.soma((1,2,3),4))