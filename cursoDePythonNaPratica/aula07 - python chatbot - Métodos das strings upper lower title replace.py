print("Ola, qual o seu nome?")
nome = input(">: ")
nome = nome.lower()
nome = nome.replace("é","eh") #vai subistituir "é" por "eh"

if "o meu nome eh " in nome:
    nome = nome[14:]
nome = nome.title() #funções .upper() | .lower() | .title()

conhecidos = ["Raimundo","Wemerson"]

if nome in conhecidos:
    frase = "Eaew "
else:
    frase = "muito prazer "
print(frase+nome)

while True:
    resposta = input(">: ")
    if resposta == "tchau":
        break
    else:
        print("Digite outra coisa")

print("Tchau tchau!")