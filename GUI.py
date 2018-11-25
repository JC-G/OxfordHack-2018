from kivy.app import App
from kivy.lang import Builder
from MAIN import startGame
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string('''
<Menu>:
    orientation:'horizontal'
    FloatLayout:
        canvas.before: 
            Color: 
                rgb: 1, 1, 1 , 1
            Rectangle: 
                pos: self.pos 
                size: self.size
                source: 'DAACTUALBG.png'
    BoxLayout:
        size: min(root.size), min(root.size)
        size_hint: None, None
        pos_hint: {'center_x': 0.675, 'center_y': 0.525}
        orientation: 'vertical'
        Label:
        Button:
            text: 'Start Game'
            font_size: 40
            background_color: 1, 0, 0 , 1
            size_hint: .4, .4
            halign: 'center'
            valign: 'center'
            on_press: root.start()
        Button:
            text: 'High Scores'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.manager.current = 'highscores'
            size_hint: .4, .4
        Button:
            text: 'Settings'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.manager.current = 'settings'
            size_hint: .4, .4
        Button:
            text: 'Play Call Me Maybe'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.manager.current = 'credits'
            size_hint: .4, .4
        Button:
            text: 'Quit'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: app.stop()
            size_hint: .4, .4
        Label:
<Settings>:
    BoxLayout:
        canvas.before: 
            Color: 
                rgb: 1, 1, 1 , 1
            Rectangle: 
                pos: self.pos 
                size: self.size
                source: 'DAACTUALBG.png'
        orientation: 'vertical'
        Label:
        Button:
            text: 'Back to Main Menu'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .1
<HighScores>:
    BoxLayout:
        canvas.before: 
            Color: 
                rgb: 1, 1, 1 , 1
            Rectangle: 
                pos: self.pos 
                size: self.size
                source: 'DAACTUALBG.png'
        orientation: 'vertical'
        Label:
        Button:
            text: 'Back to Main Menu'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .1
<Credits>:
    BoxLayout:
        canvas.before: 
            Color: 
                rgb: 1, 1, 1 , 1
            Rectangle: 
                pos: self.pos 
                size: self.size
                source: 'DAACTUALBG.png'
        orientation: 'vertical' 
        Label:  
        Label:
            text:'                                      Credits to: Joseph Chambers-Graham, Gabriela van Bergen, Lyndon Hon Fan, Charalampos Kokkalis'
            shorten: True
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
        Label:
    BoxLayout:    
        Button:
            text: 'Back to Main Menu'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .1
''')


class Menu(Screen):
    def start(self):
        print("STarting")
        startGame()


class Settings(Screen):
    pass


class HighScores(Screen):
    pass


class Credits(Screen):
    pass


sm = ScreenManager()
sm.add_widget(Menu(name='menu'))
sm.add_widget(Settings(name='settings'))
sm.add_widget(HighScores(name='highscores'))
sm.add_widget(Credits(name='credits'))


class Menu(GridLayout):

    def __init__(self, **kwargs):

        super(Menu, self).__init__(**kwargs)
        self.cols = 3


class MyApp(App):

    def build(self):

        self.title = 'Disciples'
        return sm


if __name__ == '__main__':
    MyApp().run()
