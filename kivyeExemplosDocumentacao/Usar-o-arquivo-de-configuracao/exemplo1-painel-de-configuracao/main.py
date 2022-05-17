import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class Mywidget(Widget):
    pass

# class Home(FloatLayout):
#     pass

class MyApp(App):
    # use_kivy_settings = False
    # def open_settings(self, *largs):
    #     pass

    def build_config(self, config):
        config.setdefaults('section1', {
        'key1': 'value1',
        'key2': '42'
        })
    
    def build_settings(self, settings):
        def build_settings(self, settings):
            jsondata = '''
            
            [
                {   "type": "title",
                    "title": "Meu titulo da aplicaçao" },

                {   "type": "options",
                    "title": "My first key",
                    "desc": "Description of my first key",
                    "section": "section1",
                    "key": "key1",
                    "options": ["value1", "value2", "another value"] },
                
                {   "type": "numeric",
                    "title": "My second key",
                    "desc": "Description of my second key",
                    "section": "section1",
                    "key": "key2" }
            ]
    
            '''
            settings.add_json_panel('Test application',self.config, data=jsondata)
    
    def on_config_change(self, config, section, key, value):
        if config is self.config:
           token = (section, key)
        if token == ('section1', 'key1'):
            print('Our key1 has been changed to', value)
        elif token == ('section1', 'key2'):
            print('Our key2 has been changed to', value)


    def build(self):
        config = self.config
        return Label(text='key1 is %s and key2 is %d' % (config.get('section1', 'key1'),config.getint('section1', 'key2')))



if __name__=='__main__':
    MyApp().run()