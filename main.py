from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder


class CalcWindow(Widget):
    

    def clear(self):
        self.ids.calc_input.text = '0'

    def number(self,number):
        prior = self.ids.calc_input.text

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{number}'

        else:
            result = self.ids.calc_input.text = f'{prior}{number}'
            return result

class MainApp(App):
    def build(self):
        Builder.load_file("calc.kv")
        Window.size = (500,700)
        return CalcWindow()


if __name__ == "__main__":
    MainApp().run()