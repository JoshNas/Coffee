from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Create and add name input
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Create and add password input
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.login_button = Button(text='Log In')
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

    def login(self, instance):
        print(f'{self.username.text} logging in with {self.password.text}')


class MainApp(App):

    def build(self):
        self.title = 'Welcome to Coffee Shop'
        return LoginScreen()


if __name__ == "__main__":
    app = MainApp()
    app.run()
