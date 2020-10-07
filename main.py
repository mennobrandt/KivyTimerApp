import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout # wasd
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget # wasd
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
import random


class HomeWindow(Screen):
    pass


class ScramblePopup(FloatLayout):
    scramble = StringProperty()
    def create_scramble(self):
        move_set = ["F", "F'", "F2", "F2'", "U", "U'", "U2", "U2'", 
        "D", "D'", "D2", "D2'", "U", "U'", "U2", "U2'", "L", "L'", "L2", "L2'"
        , "R", "R'", "R2", "R2'"]

        final_scramble = []

        for i in range(5):
            random.shuffle(move_set)
            final_scramble.extend((move_set[0], move_set[1], move_set[2],
            move_set[3], move_set[4], move_set[5]))
            if(i == 1):
                final_scramble.append("\n")

        self.scramble = '  '.join([str(elem) for elem in final_scramble]) 


class TimerWindow(Screen):
    def show_popup(self):
        show = ScramblePopup()
        
        popupWindow = Popup(title="Random Scramble", title_align='center', content=show, size_hint=(None, None), size=('350sp', '350sp')) 

        popupWindow.open()


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