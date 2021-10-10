print("Ola, qual o seu nome?")
nome = input(">: ")

if "O meu nome eh " in nome:
    nome = nome[14:]
if "meu nome é " in nome:
    nome = nome[9:]

if nome == "Raimundo":
    print("Fala "+ nome +". Como você esta?")
if nome == "wemerson":
    print("Olá " + nome + "!")
else:
    print("Muito prazer "+ nome)

while True:
    resposta = input(">: ")
    if resposta == "tchau":
        break
    else:
        print("Digite outra coisa")

print("Tchau tchau!")