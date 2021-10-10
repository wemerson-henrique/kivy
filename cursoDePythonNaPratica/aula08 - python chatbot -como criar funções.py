def resposta():
    resp = input(">: ")
    resp = resp.lower()
    resp = resp.replace("é", "eh")  # vai subistituir "é" por "eh"
    return resp
print("Ola, qual o seu nome?")
nome = resposta()

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
    resp = resposta()
    if resp == "tchau":
        break
    else:
        print("Digite outra coisa")

print("Tchau tchau!")