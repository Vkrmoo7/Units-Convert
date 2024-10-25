from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class Converter(BoxLayout):
    def __init__(self, **kwargs):
        super(Converter, self).__init__(**kwargs)
        self.orientation = 'vertical'
        Window.clearcolor = (1, 1, 1, 1)  # Set background color

        self.add_widget(Label(text='Enter value to convert:', color=(0, 0, 1, 1), font_size='20sp'))
        self.input = TextInput(multiline=False, background_color=(0.9, 0.9, 0.9, 1))
        self.add_widget(self.input)

        self.add_widget(Label(text='Select conversion type:', color=(0, 0, 1, 1), font_size='20sp'))

        self.button_km_to_miles = Button(text='Km to Miles', background_color=(0.5, 0.7, 1, 1))
        self.button_km_to_miles.bind(on_press=self.km_to_miles)
        self.add_widget(self.button_km_to_miles)

        self.button_miles_to_km = Button(text='Miles to Km', background_color=(0.5, 0.7, 1, 1))
        self.button_miles_to_km.bind(on_press=self.miles_to_km)
        self.add_widget(self.button_miles_to_km)

        self.button_kg_to_pounds = Button(text='Kg to Pounds', background_color=(0.5, 0.7, 1, 1))
        self.button_kg_to_pounds.bind(on_press=self.kg_to_pounds)
        self.add_widget(self.button_kg_to_pounds)

        self.button_pounds_to_kg = Button(text='Pounds to Kg', background_color=(0.5, 0.7, 1, 1))
        self.button_pounds_to_kg.bind(on_press=self.pounds_to_kg)
        self.add_widget(self.button_pounds_to_kg)

        self.result = Label(text='Result:', color=(1, 0, 0, 1), font_size='24sp')
        self.add_widget(self.result)

    def km_to_miles(self, instance):
        value = float(self.input.text)
        self.result.text = f'Result: {value * 0.621371} miles'

    def miles_to_km(self, instance):
        value = float(self.input.text)
        self.result.text = f'Result: {value / 0.621371} km'

    def kg_to_pounds(self, instance):
        value = float(self.input.text)
        self.result.text = f'Result: {value * 2.20462} pounds'

    def pounds_to_kg(self, instance):
        value = float(self.input.text)
        self.result.text = f'Result: {value / 2.20462} kg'

class ConverterApp(App):
    def build(self):
        return Converter()

if __name__ == '__main__':
    ConverterApp().run()
