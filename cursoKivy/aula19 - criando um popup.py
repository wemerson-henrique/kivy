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
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    def confirmacao(self,*args):
        box = BoxLayout(orientation='vertical',padding=10,spacing=10)
        botoes = BoxLayout(padding=10,spacing=10)
        pop = Popup(title="Deseja mesmo sair?", content=box, size_hint=(None, None),
                    size=(300, 180))
        sim = Botao(text="Sim",on_release=App.get_running_app().stop)
        nao = Botao(text="Não",on_release=pop.dismiss)
        botoes.add_widget(sim)
        botoes.add_widget(nao)
        atencao = Image(source='imagens/icone-atencao.png')
        box.add_widget(atencao)
        box.add_widget(botoes)
        pop.open()

class Botao(ButtonBehavior,Label):
    cor = ListProperty([0.1,0.5,0.7,1])
    cor2 = ListProperty([0.1,0.1,0.1,1])

    def __init__(self,**kwargs):
        super(Botao, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self,*args):
        self.atualizar()

    def on_cor(self,*args):
        self.atualizar()

    def on_press(self,*args):
        self.cor, self.cor2 = self.cor2, self.cor #troca os valores das variaveis

    def on_release(self,*args):
        self.cor, self.cor2 = self.cor2, self.cor #troca os valores das variaveis

    def atualizar(self,*args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
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

class Test19(App):
    def build(self):
        return Gerenciador()

Test19().run()