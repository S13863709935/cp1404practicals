from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class ConvertMilesKmApp(App):
    km_value = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, miles):
        try:
            self.km_value = str(float(miles) * MILES_TO_KM)
        except ValueError:
            self.km_value = "0.0"

    def handle_increment(self, change):
        try:
            miles = float(self.root.ids.input_miles.text) + change
        except ValueError:
            miles = change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert(str(miles))

ConvertMilesKmApp().run()