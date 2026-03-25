# Main entry point for the Kivy application

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        return BoxLayout()

if __name__ == '__main__':
    MainApp().run()