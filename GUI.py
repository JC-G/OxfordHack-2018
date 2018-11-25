from kivy.app import App
from kivy.lang import Builder
from MAIN import startGame
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import MAIN

wasd = 0

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
        pos_hint: {'center_x': 0.7, 'center_y': 0.525}
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
            text: 'Credits'
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
            text: 'Enable/Disable WASD'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.changecontrols()
            valign: "center"
            halign: "center"
            size_hint: .3, .1
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
            text: root.highs()
            shorten: False
            text_size: self.width, self.height * 4
            halign: 'center'
            valign: 'center'
            height: self.texture_size[1]
            font_size: 40
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
            text: """Created by:\\n Joseph Chambers-Graham \\n Gabriela van Bergen \\n Lyndon Fan \\n Charalampos Kokkalis \\n\\n Credits to: \\nOmar Ayman for creating the Emotion Recognition Program\\nGustavo Maciel for the procedural generation of the track\\n\\nApologies for not playing Call Me Maybe."""
            shorten: False
            text_size: self.width, self.height * 4
            halign: 'center'
            valign: 'center'
            height: self.texture_size[1]
            font_size: 40
        Button:
            text: 'Back to Main Menu'
            font_size: 40
            background_color: 1, 0, 0 , 1
            on_press: root.manager.current = 'menu'
            size_hint: .3, .1
''')


class Menu(Screen):

    def start(self):
        global wasd
        print("Starting")
        startGame(not(bool(wasd)))

class Settings(Screen):
    def changecontrols(self):
        global wasd
        wasd = 1 - wasd
        print("WASD controls are now " + ("On" if wasd else "Off"))
        return None


class HighScores(Screen):

    def highs(self):
        names = []
        scores = []
        with open('highscores.txt') as json_file:
            data = json.load(json_file)
            for p in data['players']:
                names.append(p["name"])
                scores.append(p["score"])

            best = []
            for i in range(min(len(scores),5)):
                ind = scores.index(max(scores))
                best.append([names[ind],scores[ind]])
                names.pop(ind)
                scores.pop(ind)

        returnText = 'Highscores\n'
        for j in best:
            returnText = returnText + str(best.index(j) + 1) + '.' + j[0] + ' ' + str(j[1]) + '\n'

        return returnText

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
    MAIN.name = input("Enter your Name")
    MyApp().run()
