from kivy.app import App
from kivy.uix.label import Label

class EscapeFromDarknessApp(App):
    def build(self):
        return Label(text='Escape from Darkness - Loading...', font_size=24)

if __name__ == '__main__':
    EscapeFromDarknessApp().run()
