from kivy.app import App
from kivy.lang import Builder

class SquaringApp(App):
    def build(self):
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0"

SquaringApp().run()