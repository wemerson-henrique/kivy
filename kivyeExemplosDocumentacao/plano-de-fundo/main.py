import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class Home(Screen):
    pass

class MyApp(App):
    def build(self):
        return Home()

if __name__=='__main__':
    MyApp().run()