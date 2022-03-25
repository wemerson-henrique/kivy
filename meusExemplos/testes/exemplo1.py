

from __future__ import division
from ast import If
from tkinter.tix import Tree


def Soma(num1, num2):
    if(type(num1) not in [int]) or (type(num2) not in [int]):
        raise TypeError("num1 e num2 deven ser do tipo int")
    soma = num1+num2
    return soma

def Dividir(num1,num2):
    if(num2==0):
        raise ZeroDivisionError("num2 não pode ser zero")
    divisao = num1 / num2
    return division

# Soma(True,False)
#----------------------------------------------

# class Pessoa:
#     especie = "humana"

#     def __init__(self, nome , idade):
#         self.nome = nome
#         self.idade = idade
    
#     def ApresentarSe(self):
#         MyIntroducao = "Meu nome é {0} e tenho {1} anos".format(self.nome,self.idade)
#         return print(MyIntroducao)

# class Usuario(Pessoa):
#     def __init__(self, nome , idade, usuario, senha):
#         self.nome = nome
#         self.idade = idade
#         self.usuario = usuario
#         self.senha = senha
    
#     def Dados():
#         text = "Meu usuario é: {0} \n Minha senha é: {1}".format(self.usuario,self.senha)
#         return print(text)

# pessoa1 = Pessoa('Ana',16)
# pessoa1.ApresentarSe()
# print(pessoa1.especie)

# pessoa2 = Usuario('José', 34, 'jose1','123')
# pessoa2.ApresentarSe()
# pessoa2.Dados()