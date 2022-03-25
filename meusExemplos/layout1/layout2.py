# codigo ganbiarra
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# codigo ganbiarra
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Screen1(Screen):
    def F_Escrever(self):
        self.ids.L1.text = 'ciclado'

class Layout2(App):
    def build(self):
        return Screen1()

Layout2().run()