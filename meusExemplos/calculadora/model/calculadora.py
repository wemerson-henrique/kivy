#feito por wemerson henrique


class Calculadora:
    
    def multiplicacao(self, numero1, numero2):
        if (type(numero1) == int or type(numero1) == float) and (type(numero2) == int or type(numero2) == float):
            multiplicacao = numero1 * numero2
            return multiplicacao
        else:
            TypeError("As entradas devem ser do tipo int ou float")
    
    def soma(self,numero1,numero2):
        if (type(numero1) == int or type(numero1) == float) and (type(numero2)==int or type(numero2)==float):
            soma = numero1+numero2
            return soma
        else:
            TypeError("As entradas devem ser do tipo int ou float")
    
    def subtracao(self,numero1,numero2):
        subtracao = numero1 - numero2
        return subtracao