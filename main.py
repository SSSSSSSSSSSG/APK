from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class APK(MDApp):
    def build(self):
        return MDLabel(text="пошел нахуй", halign="center")


APK().run()