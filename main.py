import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout # wasd
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget # wasd
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.properties import StringProperty

import random

class HomeWindow(Screen):
    pass

class TimerWindow(Screen):
    scramble = StringProperty()

    def create_scramble(self):
        move_set = ["F", "F'", "F2", "F2'", "U", "U'", "U2", "U2'", 
        "D", "D'", "D2", "D2'", "U", "U'", "U2", "U2'", "L", "L'", "L2", "L2'"
        , "R", "R'", "R2", "R2'"]

        final_scramble = []
        
        line_broken = False

        for i in range(5):
            random.shuffle(move_set)
            final_scramble.extend((move_set[0], move_set[1], move_set[2],
            move_set[3], move_set[4], move_set[5]))

            if(len(final_scramble) >= 14 and line_broken == False):
                line_broken = True
                final_scramble.append("\n")

        print(*final_scramble)
        print(final_scramble)



class AlgsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


def randomise():
    pass

class MyApp(App): # <- Main Class
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()