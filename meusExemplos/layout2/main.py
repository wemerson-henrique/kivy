# codigo ganbiarra
from importlib.resources import open_text
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# codigo ganbiarra
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Home(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def PostMensage(self, texto):
        text1 = texto
        controle = 'controle'
        a = self.ids.input1.text
        self.ids.input1.text = ''
        self.ids.label1 = text1 + controle + a
        open_text(self,a)

    def on_text(elf,*args):
        self.PostMensage('oi')

class MyApp(App):
    def build(self):
        return Home()

MyApp().run()