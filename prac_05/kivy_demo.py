"""
Kivy Demo
Estimate: 20 minutes
Actual:   15 minutes
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RootWidget(BoxLayout):
    def do_something(self):
        print("Button clicked!")

class KivyDemoApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    KivyDemoApp().run()
