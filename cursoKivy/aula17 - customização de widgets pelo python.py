#Eventos da tela e Eventos de teclado
#codigo ganbiarra
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
#codigo ganbiarra
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window #importa biblioteca para criar atalhos de botão/teclado
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Botao(ButtonBehavior,Label):
    def __init__(self,**kwargs):
        super(Botao, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self,*args):
        self.atualizar()

    def atualizar(self,*args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(0.1,0.5,0.7,1))
            Ellipse(size=(self.height,self.height), pos=self.pos)
            Ellipse(size=(self.height,self.height), pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height), pos=(self.x+self.height/2.0,self.y))

class Tarefas(Screen):
    def __init__(self,tarefas=[],**kwargs):
        super(Tarefas, self).__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
    #esta class redas os Eventos de Screen, Buscar sobre

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,window,key,*args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True
            #print(key) #mostra o codigo da tecla

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))
        self.ids.texto.text = ""

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super(Tarefa, self).__init__(**kwargs)
        self.ids.label.text = text

class Test17(App):
    def build(self):
        return Gerenciador()

Test17().run()