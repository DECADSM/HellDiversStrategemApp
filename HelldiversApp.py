from kivy.app import App
from kivy.uix.widget import Widget


class Strategem(Widget):
    pass


class Helldiver(App):
    def build(self):
        return Strategem()


if __name__ == '__main__':
    Helldiver().run()
