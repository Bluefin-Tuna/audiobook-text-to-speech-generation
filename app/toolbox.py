from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Toolbox(App):
    
    def build(self):

        mainlayout = BoxLayout(orientation = "vertical")

        self.path_layout = GridLayout()
        self.path_layout.cols = 2
        self.path_layout.rows = 5
        self.path_layout.add_widget(Label(text = "Path to .txt file"))
        self.path_layout.add_widget(TextInput(multiline = True))
        self.path_layout.add_widget(Label(text = "Path to audio samples"))
        self.path_layout.add_widget(TextInput(multiline = True))
        self.path_layout.add_widget(Label(text = "Path to storage path"))
        self.path_layout.add_widget(TextInput(multiline = True))
        self.path_layout.add_widget(Label(text = "Identification"))
        self.path_layout.add_widget(TextInput(multiline = False))

        tempui = GridLayout()
        tempui.cols = 2
        tempui.rows = 1
        tempui.add_widget(Button(text = "Male"))
        tempui.add_widget(Button(text = "Female"))

        self.path_layout.add_widget(Label(text = "Gender"))
        self.path_layout.add_widget(tempui)

        # self.grid_layout = GridLayout(height = 50)
        # self.grid_layout.cols = 3
        # self.grid_layout.rows = 1
        # self.grid_layout.add_widget(Label(text = "Gender"))
        # self.grid_layout.add_widget(Button(text = "Male"))
        # self.grid_layout.add_widget(Button(text = "Female"))

        mainlayout.add_widget(self.path_layout)
        mainlayout.add_widget(Button(text = "Submit", size_hint = (1, 0.35)))

        return mainlayout

if __name__ == "__main__":
    toolbox = Toolbox()
    toolbox.run()
