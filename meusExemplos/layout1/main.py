#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class Home(Widget):
    pass

class MyApp(App):
    def build(self):
        return Home()

if __name__=='__main__':
    MyApp().run()