# codigo ganbiarra
import os
from turtle import onclick
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# codigo ganbiarra
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

class Screen1(Screen):
    def my_callback(dt):
        print ('#########################################################My callback is called !')
    Clock.schedule_once(my_callback, 1)

    


class relogio():
    def my_callback(dt):
        print ('My callback is called !')
    Clock.schedule_once(my_callback, 1)

class MyApp(App):
    def build(self):
        return Screen1()

MyApp().run()