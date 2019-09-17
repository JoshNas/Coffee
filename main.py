from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


class SimplePopup(Popup):
    pass


class LoginScreen(Screen):

    def login(self):
        if self.ids.username.text == '' and self.ids.password.text == '':
            # manager is the screen manager, current sets name of screen to display
            self.manager.current = 'order'
        else:
            self.ids.username.text = ''
            self.ids.password.text = ''
            SimplePopup().open()


class OrderScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class CoffeeApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    CoffeeApp().run()
