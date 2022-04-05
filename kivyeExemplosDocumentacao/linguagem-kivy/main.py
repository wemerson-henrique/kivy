import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('view/myapp.kv')

class MyWidget(Screen):
    pass


class MyApp(App):
    def build(self):
        return MyWidget()

if __name__== '__main__':
    MyApp().run()