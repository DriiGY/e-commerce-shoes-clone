from kivy.lang.builder import Builder
from kivymd.app import MDApp 
from kivy.core.window import Window

from libs.screens.homepage import HomePage


class ECommerceShoeApp(MDApp):
    def build(self):
        Window.size = [330, 600]
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self):
        Builder.load_file("./libs/screens/homepage.kv")
        Builder.load_file("./libs/components/appbar.kv")
        Builder.load_file("./libs/components/products_dropdown.kv")
        Builder.load_file("./libs/components/categories.kv")
        Builder.load_file("./libs/components/circular_item.kv")


if __name__ == "__main__":
    ECommerceShoeApp().run()
