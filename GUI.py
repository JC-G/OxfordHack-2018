import kivy
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.properties import StringProperty
from kivy.properties import BooleanProperty







Builder.load_string('''
<Menu>:
    BoxLayout:
        canvas.before: 
            Color: 
                rgb: 1, 1, 1 , 1
            Rectangle: 
                pos: self.pos 
                size: self.size 
        orientation: 'vertical'
        Image:
            size: 24, 24
            source: 'sad.png'
        Button:
            text: 'Start Game'
            font_size: 40
            background_color: 1, 0, 0 , 1
        Button:
            text: 'High Scores'
            font_size: 40
            background_color: 1, 0, 0 , 1
        Button:
            text: 'Settings'
            font_size: 40
            background_color: 1, 0, 0 , 1
        Button:
            text: 'Play Call Me Maybe'
            font_size: 40
            background_color: 1, 0, 0 , 1
''')


class Menu(GridLayout):

    def __init__(self, **kwargs):

        super(Menu, self).__init__(**kwargs)
        self.cols = 1


class MyApp(App):

    def build(self):
        return Menu()


if __name__ == '__main__':
    MyApp().run()
