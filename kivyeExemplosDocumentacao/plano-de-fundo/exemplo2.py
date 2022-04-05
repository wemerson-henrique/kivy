import os
import kivy
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout 

class Home(Widget):
    pass



class Exemplo2(App):
    def build(self):
        return Home()

if __name__=='__main__':
    Exemplo2().run()