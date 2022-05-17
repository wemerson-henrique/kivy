import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.base import EventLoop 

class Mywidget(Widget):
    pass

class Home(FloatLayout):
    pass

class MyApp(App):

    def build(self):
        self.title = 'Meu Primeiro App'
        # tite = 'Custom title'
        # EventLoop.window.title = 'New title'

        self.icon = 'myicon.png'
        return Home()

if __name__=='__main__':
    MyApp().run()