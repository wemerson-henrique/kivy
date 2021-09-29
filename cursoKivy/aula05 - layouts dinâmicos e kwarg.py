#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Tarefas(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        #"**kwargs" keyword arguments letra = 'a', pode sercolocado qualquer nome
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))

class Test(App):
    def build(self):
        return Tarefas(["Fazer compras","Estudar","Trabalhar"],orientation='vertical')

Test().run()