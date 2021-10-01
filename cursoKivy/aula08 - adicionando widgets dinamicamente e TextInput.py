#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Tarefas(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ""

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Test08(App):
    def build(self):
        return Tarefas(["Oi","Hi","Olá","Hello","hey","Ei"])

Test08().run()