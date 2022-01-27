# kivimd_env\Scripts\Activate.ps1

# from kivy.lang import Builder

from kivymd.app import MDApp
import sys

from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDSwitch

class MainApp(MDApp):

    def calc(self, args):
        a=int(self.input_a.text, 2)
        b=int(self.input_b.text, 2)
        if self.switch_add.active:
            result =   bin(a + b)[2:]
        elif self.switch_sub.active:
            result =   bin(a - b)[2:]
        else:
            result = 'Select an ADD or SUB'
        self.label_res.text = result

    def exit(self, args):
        print('Exit')
        sys.exit()

    def switch_to_sub(self, args):
        self.switch_add.active = False

    def switch_to_add(self, args):
        self.switch_sub.active = False

    def build(self):
        screen = MDScreen()

        self.toolbar = MDToolbar(
            title="Binary calculator",
            elevation= 10
            )
        self.toolbar.pos_hint = {"top": 1}
        screen.add_widget(self.toolbar)

        self.label_a = MDLabel(
            text="Binary number A",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.80},
        )
        screen.add_widget(self.label_a)

        self.input_a = MDTextField(
            text="00100",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.7},
        )
        screen.add_widget(self.input_a)

        self.label_b = MDLabel(
            text="Binary number B",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.6},
        )
        screen.add_widget(self.label_b)

        self.input_b = MDTextField(
            text="00100",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
        )
        screen.add_widget(self.input_b)

        self.label_res = MDLabel(
            text="",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
        )
        screen.add_widget(self.label_res)


        self.bt_calc = MDFillRoundFlatButton(
            text="Calculate",
            font_size = 17,
            pos_hint = {"center_x": 0.4, "center_y":0.2},
            on_press = self.calc
        )
        screen.add_widget(self.bt_calc)

        self.bt_exit = MDFillRoundFlatButton(
            text="Exit",
            font_size = 17,
            pos_hint = {"center_x": 0.6, "center_y":0.2},
            on_press = self.exit
        )
        screen.add_widget(self.bt_exit)

        self.label_add = MDLabel(
            text="Add",
            halign="center",
            pos_hint = {"center_x": 0.3, "center_y":0.4},
        )
        screen.add_widget(self.label_add)

        self.switch_add = MDSwitch(
            active = True,
            pos_hint = {'center_x': .4, 'center_y': .4},
            on_press = self.switch_to_add
        )
        screen.add_widget(self.switch_add)

        self.label_sub = MDLabel(
            text="Sub",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.4},
        )
        screen.add_widget(self.label_sub)

        self.switch_sub = MDSwitch(
            active = False,
            pos_hint = {'center_x': 0.6, 'center_y': 0.4},
            on_press = self.switch_to_sub
        )
        screen.add_widget(self.switch_sub)

        return screen


MainApp().run()
