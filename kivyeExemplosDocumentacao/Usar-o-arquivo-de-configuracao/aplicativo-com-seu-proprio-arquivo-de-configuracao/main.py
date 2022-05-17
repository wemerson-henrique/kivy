import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class Mywidget(Widget):
    pass

class Home(FloatLayout):
    pass

class MyApp(App):

    def build_config(self, config):
        config.setdefaults('section1',{
            'key1':'value1',
            'key2':'42'
        })

    def build(self):
        config = self.config
        return Label(text='key1 is %s and key2 is %d' % (
            config.get('section1', 'key1'),
            config.getint('section1', 'key2')))

if __name__=='__main__':
    MyApp().run()