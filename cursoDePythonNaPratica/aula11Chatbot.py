class Chatbot():
    def __init__(self, nome): #primeira função a rodar
        self.nome = nome
        self.conhecidos = ["Will","João","Wemerson"]
        self.historico = []

    def escuta(self):
        # Capturando a resposta do usuario e preprocessando-a
        frase = input(">: ")
        frase = frase.lower()
        frase = frase.replace("é", "eh")  # vai subistituir "é" por "eh"
        return frase

    def pensa(self, frase):
        if frase == "oi":
            return "Olá, qual o seu:nome?"
        if self.historico[-1] == "Olá, qual o seu:nome?": # Pega o primeiro elemento do vetor de traz para frente
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        return "Não entendi"

    def pegaNome(self, nome):
        if "o meu nome eh " in nome:
            nome = nome[14:]
        nome = nome.title()  # funções .upper() | .lower() | .title()
        return nome

    def respondeNome(self, nome):
        conhecidos = ["Raimundo", "Wemerson"]
        if nome in self.conhecidos:
            frase = "Eaew "
        else:
            frase = "muito prazer "
        return frase + nome

    def fala(self, frase):
        print(frase)
        self.historico.append(frase)

