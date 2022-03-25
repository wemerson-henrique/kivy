from cProfile import run
from kivy.app import App
from kivy.uix.label import Label

class Home(Label):
    pass

class MyApp(App):
    def __init__(self):
        return Home()

if __name__=='__main__':
    MyApp().run()