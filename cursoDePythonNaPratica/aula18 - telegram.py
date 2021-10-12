import telepot

# Não criei um bot no telegram ainda, dessa forma este codigo não funciona
# TODO: Criar bot no telegram e pegar chave

bot = telepot.Bot("Aqui vai minha chave do Telegram")

def recebendoMsg(msg):
    print(msg['text'])

bot.message_loop(recebendoMsg)

while True:
    pass