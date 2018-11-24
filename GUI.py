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
        orientation: 'vertical'
        Button:
            text: 'Start Game'
            font_size: 40
        Button:
            text: 'High Scores'
            font_size: 40
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