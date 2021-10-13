import telepot
from RobodeFala import Chatbot

# Não criei um bot no telegram ainda, dessa forma este codigo não funciona
# TODO: Criar bot no telegram e pegar chave

telegram = telepot.Bot("Aqui vai minha chave do Telegram")
bot = Chatbot("Hector")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    #chatID = msg["chat"]["id"] # Pega o id do telegram
    tipoMsg, tipoChat, chatID = telepot.glance(msg) # Pega o id do telegram
    telegram.sendMessage(chatID.resp)

telegram.message_loop(recebendoMsg)

while True:
    pass