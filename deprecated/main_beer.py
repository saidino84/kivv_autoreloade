import importlib
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivymd.uix.screen import MDScreen
from kivymd.material_resources import STANDARD_INCREMENT
from kivy.core.window import Window


class BeerListScreen(Screen):
    ...

Window.size=(350,630)
from kivymd.app import MDApp
class BeerListScreen(Screen):
    ...

class BeerApp(MDApp):
    def build(self):
        import beer_list_screen
        # Window.bind(on_keyboard=self._rebuild)
        importlib.reload(beer_list_screen)
        return BeerListScreen()


BeerApp().run()
