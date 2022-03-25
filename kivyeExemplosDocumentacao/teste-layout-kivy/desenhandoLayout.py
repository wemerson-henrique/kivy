#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget (Widget):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__=='__main__':
    MyApp().run()
