import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *

class MyWidget1(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 1, mode='rgb')
            # draw a line using the default color
            Line(points=(2, 4, 6, 8, 16, 32,64))
            # lets draw a semi-transparent red square
            Color(1, 0, 0, .5, mode='rgba')
            Rectangle(pos=self.pos, size=self.size)

class MyWidget2(Widget):
    def __init__(self, **kwargs):
        super(MyWidget2, self).__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect)
        self.bind(size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class MyWidget3(Widget):

    def __init__(self, **kwargs):
        super(MyWidget3, self).__init__(**kwargs)
        self.draw_my_stuff()
        self.bind(pos=self.draw_my_stuff)
        self.bind(size=self.draw_my_stuff)
        
    def draw_my_stuff(self):
        self.canvas.clear()
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size)

class MainApp(App):
    def build(self):
        return MyWidget2()

if __name__== '__main__':
    MainApp().run()