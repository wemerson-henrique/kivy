# codigo ganbiarra
from importlib.resources import open_text
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
# codigo ganbiarra
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Home(BoxLayout):
    
    def onclick(self):
        a = self.PegaInput()
        self.MudarTextLabel(a)

    def PegaInput(self):
        texto = self.ids.input1.text
        self.ids.input1.text = ''
        return texto
    
    def MudarTextLabel(self,texto):
        self.ids.label1.text = texto
        return print(texto)
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # if the touch collides with our widget, let's grab it
            touch.grab(self)
            # and accept the touch.
            return True
    def on_touch_up(self, touch):
        # here, you don't check if the touch collides or things likethat.
        # you just need to check if it's a grabbed touch event
        if touch.grab_current is self:
            # ok, the current touch is dispatched for us.
            # do something interesting here
            print('Hello world!')
            # don't forget to ungrab ourself, or you might have sideeffects
            touch.ungrab(self)
            # and accept the last up
            return True

class MyApp(App):
    def build(self):
        return Home()

MyApp().run()