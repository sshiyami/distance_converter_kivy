from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (300, 400)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = 'Конвертер расстояния'


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Конвертер ')
        self.miles = Label(text='Мили')
        self.meters = Label(text='Метры')
        self.santimeters = Label(text='Сантиметры')
        self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = f'Мили: {float(data)*0.62}'
            self.meters.text = f'Метры: {float(data) * 1000}'
            self.santimeters.text = f'Сантиметры: {float(data) * 100000}'
        else:
            self.input_data.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.meters)
        box.add_widget(self.santimeters)

        return box


if __name__ == '__main__':
    MyApp().run()
