class Chatbot():
    def __init__(self, nome): #primeira função a rodar
        self.nome = nome

    def fala(self):
        print("oi, meu nome é ",self.nome)

a = Chatbot("Eduardo")
a.fala()

b = Chatbot("Alfred")
b.fala()

print(b.nome)