import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.lang import Builder
from kivymd.app import MDApp

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.primary_palette = "DeepPurple"
        # self.theme_cls.primary_palette = "Lime"
        # self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('my.kv')

if __name__=='__main__':
    MyApp().run()