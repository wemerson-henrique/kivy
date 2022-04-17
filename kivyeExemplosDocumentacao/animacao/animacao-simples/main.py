import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import ObjectProperty


class MeuQuadrado(Widget):
    pass

class Home(FloatLayout):
    quad = ObjectProperty()

    def AnimacaoSimples (self,widget):
        anim = Animation(x=100, y=100)
        anim.start(widget)
    
    def MultiplasPropriedadesETransicoes(self,widget):
        anim = Animation(x=50, size=(80, 80), t='linear')
        anim.start(widget)
    
    def AnimacaoSequencial(self,widget):
        anim = Animation(x=50) + Animation(size=(80, 80), t='in_quad', duration=2.)
        anim.start(widget)

    def AnimacaoParalela(self,widget):
        anim = Animation(pos=(80, 10))
        anim &= Animation(size=(800, 800), duration=2.)
        anim.start(widget)
    
    def RepetindoAnimacao(self,widget):
        anim = Animation(pos=(100, 10)) + Animation(size=(800, 800))
        anim.repeat = True
        anim.start(widget)
    
    def cancelarAnimacao(self,widget):
        # Animation.stop(widget)
        Animation.cancel_all(widget, 'x')

class MyApp(App):
    def build(self):
        return Home()

if __name__=='__main__':
    MyApp().run()