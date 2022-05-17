import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp

# class Home(MDApp):
#     pass

class MyApp(MDApp):
    

    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # self.wel = ObjectProperty()
        return Builder.load_file('exemplo1.kv')
    
    def logar(self):
        self.root.ids.welcome_label.text = f'Sup { self.root.ids.user.text}!'
        # self.wel.text = "logado!"
    
    def limpar(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

if __name__=='__main__':
    MyApp().run()