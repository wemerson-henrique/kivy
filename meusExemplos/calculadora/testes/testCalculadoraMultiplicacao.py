import sys
sys.path.append(r"C:\Users\WEMERSON\Documents\GitHub\kivy\meusExemplos\calculadora")

from model.calculadora import Calculadora
import unittest

cal = Calculadora()

class TestCalculadoraMultiplicacao(unittest.TestCase):

    def testMultiplicacao(self):
        self.assertEqual(cal.multiplicacao(2,2),4)
        self.assertEqual(cal.multiplicacao(1,1),1)
        self.assertEqual(cal.multiplicacao(100,100),10000)
        self.assertEqual(cal.multiplicacao(0,0),0)
        self.assertEqual(cal.multiplicacao(-3,2),-6)
        self.assertEqual(cal.multiplicacao(2.0,2.0),4.0)
        self.assertEqual(cal.multiplicacao(3.0,2),6.0)
        self.assertEqual(cal.multiplicacao(2,4.0),8.0)
    
    def testMultiplicacaoValoresDeEntrada(self):
        self.assertRaises(TypeError,cal.multiplicacao("2","2"))
        self.assertRaises(TypeError,cal.multiplicacao("2",6))
        self.assertRaises(TypeError,cal.multiplicacao(3,"5"))
        self.assertRaises(TypeError,cal.multiplicacao(2,True))
        self.assertRaises(TypeError,cal.multiplicacao(True,2))
        self.assertRaises(TypeError,cal.multiplicacao(2,False))
        self.assertRaises(TypeError,cal.multiplicacao(False,2))
        self.assertRaises(TypeError,cal.multiplicacao([1,2,3],[1,2,3]))
        self.assertRaises(TypeError,cal.multiplicacao((1,2,3),(1,2,3)))  

# if __name__=='__main__':
#     unittest.main()