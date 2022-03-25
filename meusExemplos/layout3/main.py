# codigo ganbiarra
from distutils.command.build import build
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# codigo ganbiarra
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class Home(Screen):
    pass

class MyApp(App):
    def build(self):
        return Home()

MyApp().run()