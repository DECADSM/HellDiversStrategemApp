from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen

class Strategem(Screen):
    def pressed(self):
        print('Fuck you')
    pass

class Helldiver(App):
    def build(self):
        return Strategem()
    


if __name__ == '__main__':
    Helldiver().run()
