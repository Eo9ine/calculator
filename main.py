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
        
    def add(self):
        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}+'
    
    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}-'
        

    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}x'

    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}/'

    
    def equals(self):
        prior = self.ids.calc_input.text

        operations = ['-', '+', '/', '*']

        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for num in num_list:
                answer = answer + int(num)

            self.ids.calc_input.text = f'{str(answer)}'

        elif "-" in prior:
            num_list = prior.split("-")
            answer = 0
            for num in num_list:
                answer = answer - int(num)

            self.ids.calc_input.text = f"{str(answer)}"

        elif "/" in prior:
            num_list = prior.split("/")
            answer = 0
            for num in num_list:
                answer = answer / int(num)
            
            self.ids.calc_input.text = f"{str(answer)}"

        elif "*" in prior:
            num_list = prior.split("*")
            answer = 0
            for num in num_list:
                answer = answer * int(num)

            self.ids.calc_input.text = f"{str(answer)}"

        else:
            self.ids.calc_input.text = prior

    
class MainApp(App):
    def build(self):
        Builder.load_file("calc.kv")
        Window.size = (500,700)
        return CalcWindow()


if __name__ == "__main__":
    MainApp().run()