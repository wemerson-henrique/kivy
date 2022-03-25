from time import time
from tkinter import Label
from kivy.app import App
from os.path import dirname, join
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra

print('Holle world');
class MyApp(App):
    def build(self):
        return Label(text='Hello World')

if __name__=='__main__':
    MyApp().run()