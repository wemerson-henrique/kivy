def resposta():
    # Capturando a resposta do usuario e preprocessando-a
    resp = input(">: ")
    resp = resp.lower()
    resp = resp.replace("é", "eh")  # vai subistituir "é" por "eh"
    return resp

def pegaNome(nome):
    if "o meu nome eh " in nome:
        nome = nome[14:]
    nome = nome.title()  # funções .upper() | .lower() | .title()
    return nome

def respondeNome(nome):
    conhecidos = ["Raimundo", "Wemerson"]
    if nome in conhecidos:
        frase = "Eaew "
    else:
        frase = "muito prazer "
    return frase + nome