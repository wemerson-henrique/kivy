# #1 - Python Kivy - criando uma interface gráfica
#Feito por weemerson henrique 13/09/2021

#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra

from kivy.app import App
from kivy.uix.button import Button

class PrimeiroApp (App):
    def build(self):
        return Button(text = "Olá Mundo")

PrimeiroApp().run()