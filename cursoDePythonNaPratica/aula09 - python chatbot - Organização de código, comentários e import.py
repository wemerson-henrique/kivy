#from aula09funcoes import resposta, pegaNome, respondeNome
from aula09funcoes import *
print("Ola, qual o seu nome?")
nome = pegaNome(resposta())
resp = respondeNome(nome)
print(resp)

while True:
    resp = resposta()
    if resp == "tchau":
        break
    else:
        print("Digite outra coisa")

print("Tchau tchau!")