'''
frase = "Um bom programador sempre estuda"
res1 = frase[0]
res2 = frase[7:18]
res3 = frase[19:]
res4 = frase[:7]
print("Frase Original: ",frase)
print(res1)
print(res2)
print(res3)
print(res4)
'''

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