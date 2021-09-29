# #1 - Python Kivy - criando uma interface gráfica
#Feito por weemerson henrique 13/09/2021

#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra

from kivy.app import App
from kivy.uix.button import Button #importa botão com nome botão
from kivy.uix.boxlayout import BoxLayout #importa BoxLayout com nome BoxLayout
from kivy.uix.label import Label #BoxLayout

class TestApp (App):
    def build(self):
        box = BoxLayout(orientation='vertical') #cria um layout arzendo na variavel box
        #"orientation='vertical'" serve para deixar o orientação no setingo vertical
        button1 = Button(text='Meu botão 1') #cria botao
        label1 = Label(text='Texto 1') #cria label para mostrar texto
        box.add_widget(button1) #adiciona button1 ao layout box
        box.add_widget(label1) #adiciona label1 ao layout box

        box2 = BoxLayout() #cria um segundo layout chamado box2
        button2 = Button(text='Botão 2') #cria botão
        label2 = Label(text='Texto 2') #cria label
        box2.add_widget(button2) #adiciona button2 ao layout box2
        box2.add_widget(label2) #adiciona label2 ao layout box2

        box.add_widget(box2) #adiciona o layout box ao layout box

        return box

TestApp().run()