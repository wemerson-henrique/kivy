#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class Screen(Widget):
    def bonclick(self,**kwargs):
        super().__init__(**kwargs)
        a = self.ids.texto.text
        self.ids.texto.text = ''
        self.ids.L2.text = str(a)
        self.ids.L2.text = "clicado"

class Layout1(App):
    def build(self):
        return Screen()

if __name__=='__main__':
    Layout1().run()