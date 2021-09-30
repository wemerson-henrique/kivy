#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa,font_size=30,size_hint_y=None,height=200))
class Test06 (App):
    def build(self):
        return Tarefas(["Oi","Hi","Olá","Hello","hey","Ei"])
Test06().run()
