print("Ola, qual o seu nome?")
nome = input(">: ")

if "O meu nome eh " in nome:
    nome = nome[14:]
if "meu nome é " in nome:
    nome = nome[9:]

conhecidos = ["Raimundo","wemerson"]
for i in conhecidos:
    if nome == conhecidos:
        print("Eaew "+ nome +". Como você esta?")
    else:
        print("Muito prazer "+ nome)

while True:
    resposta = input(">: ")
    if resposta == "tchau":
        break
    else:
        print("Digite outra coisa")

print("Tchau tchau!")