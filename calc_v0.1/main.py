# A simple calculator app
# @ belal_bh
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder



Builder.load_string('''
<CustButton@Button>:
    font_size: 75

<CalcGridLayout>:
    id: calculator
    display: entry
    rows: 6
    padding: 10
    spacing: 10

    BoxLayout:
        TextInput:
            id: entry
            font_size: 75
            multiline: True
            padding_x:[20,0]
            pos_hint: {'right': 1, 'top': 1}
    
    BoxLayout:
        spacing: 10
        CustButton:
            text: "AC"
            on_press: entry.text = ""

        CustButton:
            text: "("
            on_press: entry.text += self.text

        CustButton:
            text: ")"
            on_press: entry.text += self.text

        CustButton:
            text: "/"
            on_press: entry.text += self.text
    
    BoxLayout:
        spacing: 10
        CustButton:
            text: "7"
            on_press: entry.text += self.text

        CustButton:
            text: "8"
            on_press: entry.text += self.text

        CustButton:
            text: "9"
            on_press: entry.text += self.text

        CustButton:
            text: "*"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "4"
            on_press: entry.text += self.text

        CustButton:
            text: "5"
            on_press: entry.text += self.text

        CustButton:
            text: "6"
            on_press: entry.text += self.text

        CustButton:
            text: "-"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "1"
            on_press: entry.text += self.text

        CustButton:
            text: "2"
            on_press: entry.text += self.text

        CustButton:
            text: "3"
            on_press: entry.text += self.text

        CustButton:
            text: "+"
            on_press: entry.text += self.text

    BoxLayout:
        spacing: 10
        CustButton:
            text: "."
            on_press: entry.text += self.text

        CustButton:
            text: "0"
            on_press: entry.text += self.text

        CustButton:
            text: "DEL"
            on_press: entry.text = entry.text[:-1]

        CustButton:
            text: "="
            on_press: calculator.calculat(entry.text)

''')



class CalcGridLayout(GridLayout):
    def calculat(self, calculation):
        if calculation:
            try:
                ans = '{:10.4f}'.format(eval(calculation))
                if ans[-5:]=='.0000':
                    ans = ans[:-5]
                self.display.text = ans
            except Exception:
                self.display.text = "Oops Error >_< !!!"


class CalculatorApp(App):

     def build(self):
         return CalcGridLayout()


if __name__ == '__main__':
    CalculatorApp().run()
