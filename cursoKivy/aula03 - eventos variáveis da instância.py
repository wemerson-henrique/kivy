#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botão 1',font_size=30,on_release=self.incrementar)
        #",on_release=self.incrementar" cria uma função que ao soltar o botão clicado chama a função "incrementar"
        #",font_size=30" define fonte tamanho 30
        self.label = Label(text='1',font_size=30)
        #"self.label" cria variavel da instancia
        # ",font_size=30" define fonte tamanho 30
        box.add_widget(button)
        box.add_widget(self.label)

        return box

    def incrementar(self,button):
        button.text = "Soltei"
        #vai mudar o valor do texto do botão
        self.label.text = str(int(self.label.text)+1)
        #"int()" converte para numero
        #"str()" converte para string

Test().run()