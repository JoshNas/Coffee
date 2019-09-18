from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
import db


class ErrorPopup(Popup):
    """Popup for incorrect log in information. Informs user they have entered an incorrect user name or password."""
    pass


class LoginScreen(Screen):
    """Screen for user to enter name and password. If incorrect combination is given prompt user with ErrorPopup. If
    receive correct combination ScreenManager moves to OrderScreen."""
    def login(self):
        if self.ids.username.text == 'admin' and self.ids.password.text == 'pass':
            # manager is the screen manager, current sets name of screen to display
            self.manager.current = 'order'
        else:
            self.ids.username.text = ''
            self.ids.password.text = ''
            ErrorPopup().open()


class OrderScreen(Screen):
    """Enter and display orders for Coffee Shop. On submit orders are stored in MySQL database."""
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
        """Add items to current order. Updates order list and total price. Displays both in window"""
        item = item.replace('\n', ' ')
        # allow for no table to be set for customers who will not be sitting
        self.order.append((self.table, item, price))
        self.order_window += f'{item} {price}\n\n'
        self.total += price
        self.price_window = str(self.total)

    def remove_last(self):
        """Remove most recent addition from order list. Updates total price and display windows."""
        removed = self.order.pop()
        self.order_window = ''
        for order in self.order:
            self.order_window += f'{order[1]} {order[2]}\n\n'
        self.total -= removed[2]
        self.price_window = str(self.total)

    def submit(self):
        """Submits current order to MySQl database and displays all orders in that database in console. Calls clear
        function to reset all variables associated with current order and display windows."""
        db.create_order(self.order)
        self.clear()
        db.get_orders()

    def clear(self):
        """Clear variables associated with current order and display windows."""
        self.order = []
        self.total = 0
        self.table = ''
        self.order_window = ''
        self.price_window = ''


class WindowManager(ScreenManager):
    """Manager class to control which window we view."""
    pass


kv = Builder.load_file("main.kv")


class CoffeeApp(App):
    """Main Application"""
    def build(self):
        return kv


if __name__ == "__main__":
    CoffeeApp().run()
