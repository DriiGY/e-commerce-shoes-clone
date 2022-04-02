from kivy.lang.builder import Builder
from kivymd.app import MDApp 
from kivy.core.window import Window

from libs.screens.homepage import HomePage


class ECommerceShoeApp(MDApp):
    def build(self):
        Window.size = [330, 600]
        print("ola mundo 2234252")
        return HomePage()


if __name__ == "__main__":
    ECommerceShoeApp().run()
