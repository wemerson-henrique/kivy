import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

Builder.load_file('view\exemplo1.kv')

class MyWidget(Screen):
    pass

class MyFirstWidget(BoxLayout):
    txt_inpt = ObjectProperty(None) # LEMBRE-SE: usar ObjectProperty é considerado uma boa pratica

    def check_status(self, btn):
        pass
        print('button state is: {state}'.format(state=btn.state))
        print('text input text is: {txt}'.format(txt=self.txt_inpt))

    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!" # alternative syntax

class Exemplo1(App):
    def build(self):
        return MyFirstWidget()

if __name__=='__main__':
    Exemplo1().run()