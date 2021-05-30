import importlib
import os
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp
import perguntas

Window.size=(360,740)


class Live(App, MDApp):
    KV_FILES = {
        os.path.join(os.getcwd(), "perguntas.kv"),
        # os.path.join(os.getcwd(), "card_item.kv"),
    }
    CLASSES = {
        "PerguntasScreen": "perguntas",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def on_start(self):
        print("Hello world")

    def build_app(
        self,
    ):
         

        self.theme_cls.theme_style = "Light"
        Window.bind(on_keyboard=self._rebuild)
        importlib.reload(perguntas)
        return perguntas.PerguntasScreen()

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()


Live().run()