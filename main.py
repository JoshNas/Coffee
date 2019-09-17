from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, NumericProperty

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
    order_window = StringProperty()
    price_window = StringProperty()

    def __init__(self, **kwargs):
        super(OrderScreen, self).__init__(**kwargs)
        self.table = ''
        self.order = []
        self.total = 0

    def set_table(self, table):
        self.table = table

    def add_to_order(self, item, price):
        item = item.replace('\n', ' ')
        # allow for no table to be set for customers who will not be sitting
        self.order.append((self.table, item, price))
        self.order_window += f'{item} {price}\n\n'
        self.total += price
        self.price_window = str(self.total)

    def update_order(self):
        for order in self.order:
            for item in order:
                self.order_window += str(item)
                self.order_window += '\n'

    def remove_last(self):
        removed = self.order.pop()
        self.order_window = ''
        for order in self.order:
            self.order_window += f'{order[1]} {order[2]}\n\n'
        self.total -= removed[2]
        self.price_window = str(self.total)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")


class CoffeeApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    CoffeeApp().run()
