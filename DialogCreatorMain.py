from kivy.app import App
from kivy.uix.button import Button


class DialogCreatorMain(App):
    def build(self):
        return Button(text="Hello",
                      background_color=(0, 0, 1, 1),
                      font_size=150)

    pass


if __name__ == "__main__":
    DialogCreatorMain().run()